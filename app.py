from flask import Flask, make_response, request, jsonify
import os
import requests

STATIC_URL_PREFIX = 'https://szbstorage.z20.web.core.windows.net/'
HUGGINGFACE_BEARER = os.environ.get('HF_BEARER')
HUGGINGFACE_MODEL_ID = 'neilsun2009/amz_movie_tv_distilgpt2_1k'
HUGGINGFACE_API_URL = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL_ID}"

app = Flask(__name__,
    # static_url_path='https://szbstorage.z20.web.core.windows.net/',
    # static_folder='static',
    # template_folder='static',
    instance_relative_config=True,
)

@app.route("/api/comments/auto_completion", methods=('GET', ))
def get_auto_completion_comment():
    comment = request.args.get('comment', '')
    result = {
        'comment': '',
        'isLoading': True,
    }
    if comment != '':
        res = requests.post(HUGGINGFACE_API_URL, 
            headers={
                "Authorization": f'Bearer {HUGGINGFACE_BEARER}'
            }, 
            json={
                "inputs": comment,
                # these params actually are not useable for PEFT models
                "parameters": {
                    "return_full_text": False,
                    "temperature": 5.0,
                    "repetition_penalty": 10.0,
                    "top_k": 5
                }
            }
        )
        json_result = res.json()
        print(json_result)
        if res.status_code == 200:
            result = {
                'comment': json_result[0].strip(),
                'isLoading': False,
            }
    return jsonify(result)

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
