import json

from flask import Flask
from flask import jsonify

from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def get_app_version():
    return jsonify(
        {
            "service": "Public Toilets API",
            "version": 1.0
        }
    )


@app.route("/toilets")
def get_toilets():
    with open('toilets.json') as data_file:
        data = json.load(data_file)
        return jsonify(data)


@app.route("/toilets/<string:toilet_id>")
def get_toilet(toilet_id):
    with open('toilets.json') as data_file:
        data = json.load(data_file)

    selected_toilet = None
    for toilet in data.get('toilets'):
        if toilet.get('id') == toilet_id:
            selected_toilet = toilet

    if selected_toilet:
        return jsonify(selected_toilet)
    else:
        return jsonify(
            {
                "error": "Not Found",
                "message": "Toilet not found.",
                "status": 404
            }
        )


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
