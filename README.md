# OstadKar User Manager

This is documentation for the interview project. It's a CRUD user manager with token authentication.

I use python programming with the Flask web framework and Postgres database. 

----
## Installing
First, you should install python3.x. 

For installing python3.x use this [link](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)

For installing Postgres database use this [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

After installing Python and Postgres, you must install project requirements. 

    pip -r requirements.txt

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
Change your directory to root of the project and migrate tables:

    python manage.py db upgrade

## Run
Now you can run your app with this command:

    python run.py

----
## Author
* Mohammad Hosseini - mohammad.hoseyny@gmail.com

