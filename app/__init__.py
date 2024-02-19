
from flask import  Flask
from app.config import config_options as AppConfig
from app.models import  db

def create_app(config_name='dev'):
    # create app
    app = Flask(__name__)
    # define configuration
    current_config = AppConfig[config_name]
    print(current_config)
    ## read database configuration from config class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)




    return app