# OstadKar User Manager

This is documentation for the interview project. It's a CRUD user manager with token authentication.

I use python programming with the Flask web framework and Postgres database. 

----
## Installing
First, you should install python3.x. 

For installing python3.x use this [link](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)

For installing Postgres database use this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

Befor isntalling the requirements, we need some extra package for psycopg:

    sudo apt-get install postgresql
    sudo apt-get install python-psycopg2
    sudo apt-get install libpq-dev

After installing Python and Postgres, you must install project requirements. 

    pip install -r requirements.txt

----
## Configs
Now, you must make a new database in your PG.

    sudo -u postgres psql
    create database ostadkar_user_manager;

Make a copy from *.env.exmaple* to *.env*. You must put your setting in this file. 
Edit your database settings and FLASK_ENV in .env file.
There is *production* and *development* types for FLASK_ENV. In production the DEBUG is off. You can add more configs type in app/config.py

    FLASK_ENV=development
    DATABASE_URL='postgres://DATABSE_USERNAME:DATABASE_PASSWORD@DATABASE_HOST:DATABASE_PORT/DATABASE_NAME'
    JWT_SECRET_KEY = hhgaghhgsdhdhdd

----
## Migrate
Change your directory to root of the project and migrate the tables:

    python manage.py db upgrade

## Run
Now you can run your app with this command:

    python run.py


## API 
This is a CRUD for users. This is token based authentication. You must put your token in header with *api-token*.

### Create
    URL: /api/v1/users
    METHOD: POST
    JSON Request Data:
        {
            "email": "USER_EMAIL",
            "first_name": "USER_FIRST_NAME",
            "last_name": "USER_LAST_NAME",
            "password": "USER_PASSWORD"
        }
    Response Data:
        {"jwt_token": "USER_JWT_TOKEN"}

### Lgin
    URL: /api/v1/users/login
    METHOD: POST
    JSON Request Data:
        {
            "email": "USER_EMAIL",
            "password": "USER_PASSWORD"
        }
    Response:
        200 : {"jwt_token": "USER_JWT_TOKEN"}
        400: { "error": "user doesn't exist" }
             {'error': 'you need email and password to sign in'}
             {'error': 'invalid credentials'}

### Get All users
    URL: /api/v1/users
    Authentication Requierd
    METHOD: GET
    JSON Request Data:
        None
    Header:
        {'api-token': 'USER_JWT_TOKEN'}
    Response:
        200 : [{
                    "created_at": "2019-09-05T13:07:29.529430",
                    "email": "EMAIL",
                    "first_name": "FIRSTNAME",
                    "id": ID,
                    "last_name": "LASTNAME",
                    "modified_at": "2019-09-05T13:07:29.529446",
                    "password": "HASHED_PASSWORD"
                },
             ... ]

### Get a user
    URL: /api/v1/users/<user_id: int>
    Authentication Requierd
    METHOD: GET
    JSON Request Data:
        {None
    Header:
        {'api-token': 'USER_JWT_TOKEN'}
    Response:
        200 : {
                    "created_at": "2019-09-05T13:07:29.529430",
                    "email": "EMAIL",
                    "first_name": "FIRSTNAME",
                    "id": ID,
                    "last_name": "LASTNAME",
                    "modified_at": "2019-09-05T13:07:29.529446",
                    "password": "HASHED_PASSWORD"
              }
        400: {'error': 'user not found'}

### Delete a user
    URL: /api/v1/users/<user_id: int>
    Authentication Requierd
    METHOD: DELETE
    JSON Request Data:
        None
    Header:
        {'api-token': 'USER_JWT_TOKEN'}
    Response:
        200 : { "status": "ok" } 
        400 : { "error": "user doesn't exist" }
              {'error': "you cant delete yourself"}

### Update a user
    URL: /api/v1/users/<user_id: int>
    Authentication Requierd
    METHOD: PUT
    JSON Request Data:
        {
            "email": "USER_EMAIL",
            "first_name": "USER_FIRST_NAME",
            "last_name": "USER_LAST_NAME",
            "password": "USER_PASSWORD"
        }
    Header:
        {'api-token': 'USER_JWT_TOKEN'}
    Response:
        200 : { "status": "ok" } 
        400 : { "error": "user doesn't exist" }
              {'error': "this email exist, you cant update this user's email"}


* The expiration data of the token is 1 day. It can be changed in Authentication/Authentication.py line 14.

----
## Author
* Mohammad Hosseini - mohammad.hoseyny@gmail.com
* V1.0.1
