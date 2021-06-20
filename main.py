import os

from flask import Flask, blueprints
from flask_cors import CORS

from src.blueprints import admin_bp, blog_bp, member_bp
from src.common import db, ma

app = Flask(__name__, static_folder="./build", static_url_path="/")
CORS(app, supports_credentials=True)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'app.sqlite')


app_blueprints = [admin_bp, blog_bp, member_bp]

for blueprint in app_blueprints:
    app.register_blueprint(blueprint)

db.init_app(app)
ma.init_app(app)


@app.route('/api/')
def hello():
    return "Hello Flask!"


@app.route('/')
def hi():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
