from flask import Flask, make_response, request, jsonify
import os
import requests

STATIC_URL_PREFIX = 'https://szbstorage.z20.web.core.windows.net/'

app = Flask(__name__,
    # static_url_path='https://szbstorage.z20.web.core.windows.net/',
    # static_folder='static',
    # template_folder='static',
    instance_relative_config=True,
)

@app.route("/api/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # if path != "" and os.path.exists(app.static_folder + '/' + path):
    #     return send_from_directory(app.static_folder, path)
    # else:
    #     return send_from_directory(app.static_folder, 'index.html')
    # return render_template('index.html')
    res = requests.get(STATIC_URL_PREFIX + path)
    response = make_response(res.content)
    response.headers = dict(res.headers)
    return response
