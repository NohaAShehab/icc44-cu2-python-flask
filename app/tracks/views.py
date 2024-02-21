
from app.tracks import track_blueprint
# create view ---> display all tracks

@track_blueprint.route('/home', methods=['GET'], endpoint='home')
def track_home():
    return "<h1>Welcome to Tracks Home</h1>"
