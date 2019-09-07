from flask import request, json, Response, Blueprint, g
from ..models.UserModel import UserModel, UserSchema
from ..Authentication.Authentication import Auth

user_api = Blueprint('user_api', __name__)
user_schema = UserSchema()


@user_api.route('', methods=['POST'])
def create():
    req_data = request.get_json()
    data = user_schema.load(req_data)
    user_in_db = UserModel.get_user_by_email(data.get('email'))
    if user_in_db:
      message = {'error': 'User already exist, please supply another email address'}
      return custom_response(message, 400)
    user = UserModel(data)
    user.save()
    ser_data = user_schema.dump(user)
    token = Auth.generate_token(ser_data.get('id'))
    return custom_response({'jwt_token': token}, 201)


@user_api.route('', methods=['GET'])
@Auth.auth_required
def get_all():
    users = UserModel.get_all_users()
    ser_users = user_schema.dump(users, many=True)
    return custom_response(ser_users, 200)


@user_api.route('/<int:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
    user = UserModel.get_one_user(user_id)
    if not user:
      return custom_response({'error': 'user not found'}, 404)
    
    ser_user = user_schema.dump(user)
    return custom_response(ser_user, 200)


@user_api.route('/<int:user_id>', methods=['PUT'])
@Auth.auth_required
def update(user_id):
    req_data = request.get_json()
    data = user_schema.load(req_data, partial=True)
    user = UserModel.get_one_user(user_id)
    if not user:
      return custom_response({'error': "user doesn't exist"}, 400)
    if 'email' in data.keys():
      dup_user = UserModel.get_user_by_email(data['email']) 
      if dup_user.id != user_id:
        return custom_response({'error': "this email exist, you cant update this user's email"}, 400)
    user.update(data)
    ser_user = user_schema.dump(user)
    return custom_response(ser_user, 200)


@user_api.route('/<int:user_id>', methods=['DELETE'])
@Auth.auth_required
def delete(user_id):
    if g.user.get('id') == user_id:
      return custom_response({'error': "you cant delete yourself"}, 400)
    user = UserModel.get_one_user(user_id)
    if not user:
      return custom_response({'error': "user doesn't exist"}, 400)
    user.delete()
    return custom_response({"status": "ok"}, 200)


@user_api.route('/login', methods=['POST'])
def login():
    req_data = request.get_json()

    data = user_schema.load(req_data, partial=True)
    if not data.get('email') or not data.get('password'):
      return custom_response({'error': 'you need email and password to sign in'}, 400)
    user = UserModel.get_user_by_email(data.get('email'))
    if not user:
      return custom_response({'error': "user doesn't exist"}, 400)
    if not user.check_hash(data.get('password')):
      return custom_response({'error': 'invalid credentials'}, 400)
    ser_data = user_schema.dump(user)
    token = Auth.generate_token(ser_data.get('id'))
    return custom_response({'jwt_token': token}, 200)


def custom_response(res, status_code):
    return Response(
      mimetype="application/json",
      response=json.dumps(res),
      status=status_code
    )