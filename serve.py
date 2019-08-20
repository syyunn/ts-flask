from flask import Flask
app = Flask(__name__)


@app.route('/')
def hell_world():
    return 'Hello, World'


@app.route('/data/<string:asset_class>')
def show_post(asset_class):
    # show the post with the given id, the id is an integer
    json_to_return = {"asset_class": asset_class,
                      "prices": 0}

    return json_to_return
