
import os

from app.app import create_app
import environ

env = environ.Env()
environ.Env.read_env('.env')



if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)
  # run app
  app.run()