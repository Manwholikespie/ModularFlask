import flask

app = flask.current_app
bp = flask.Blueprint('main', __name__)

@bp.route('/')
def index():
    return flask.render_template('index.html')