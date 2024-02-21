
from flask import  Flask
from app.config import config_options as AppConfig
from app.models import  db
from flask_migrate import Migrate
from flask_restful import  Api

def create_app(config_name="prd"):
    # create app
    app = Flask(__name__)
    # define configuration
    current_config = AppConfig[config_name]
    print(current_config)
    ## read database configuration from config class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)


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
    ## add url
    # from app.students.views import  get_index
    # app.add_url_rule("/", view_func=get_index, endpoint="landing")

    # create architecture // views , templates
    # introduce  blueprint to the application
    from app.students import student_blueprint
    app.register_blueprint(student_blueprint)
    from app.tracks import  track_blueprint
    app.register_blueprint(track_blueprint)

    ### we need to add the API urls
    api = Api(app) # generate apis for this project
    # add the class student resource to the api
    from app.students.api_views import  StudentList, StudentResource
    api.add_resource(StudentList,'/api/students' )
    api.add_resource(StudentResource, '/api/students/<int:std_id>')


    return app