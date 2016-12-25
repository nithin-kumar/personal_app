"""Import flask and template operators."""
from flask import Flask

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import Flask-MySQLdb
from flask_mysqldb import MySQL

# Define the WSGI application object
app = Flask(__name__)
# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_portfolio.controllers import mod_portfolio as prortfolio_module

# Register blueprint(s)
app.register_blueprint(prortfolio_module)

db.create_all()
