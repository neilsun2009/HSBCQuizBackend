from flask import Flask, render_template, request, g, jsonify, send_from_directory
import os

app = Flask(__name__,
    static_url_path='/public',
    static_folder='static',
    template_folder='static',
    instance_relative_config=True,
)

@app.route("/api/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    # return render_template('index.html')
