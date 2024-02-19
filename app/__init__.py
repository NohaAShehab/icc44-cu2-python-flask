
from flask import  Flask
from app.config import config_options as AppConfig
from app.models import  db
from flask_migrate import Migrate


def create_app(config_name='dev'):
    # create app
    app = Flask(__name__)
    # define configuration
    current_config = AppConfig[config_name]
    print(current_config)
    ## read database configuration from config class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI



    # define db to the app
    db.init_app(app)
    ## init migration
    migrate = Migrate(app, db, render_as_batch=True)

    ## in project ---> 1- init migration directory
    """
        cd app 
        export FLASK_APP=flasky
        flask db init  ## initialize migration directory
        # to create migration file
        flask db migrate -m 'migrate message '
        # to apply changes to database
        flask db upgrade         
    """





    return app