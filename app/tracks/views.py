from flask import  render_template
from app.tracks import track_blueprint
from app.models import  Track
# create view ---> display all tracks

@track_blueprint.route('/home', methods=['GET'], endpoint='home')
def track_home():
    return "<h1>Welcome to Tracks Home</h1>"


@track_blueprint.route('/', methods=['GET'], endpoint='index')
def track_index():
    tracks = Track.get_all_tracks()
    return render_template("tracks/index.html",
                           tracks=tracks)
