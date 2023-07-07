from flask import request, jsonify
import os
import json
import requests
from .stat import get_stat

def register_apis(app):

    from .config import (
        HUGGINGFACE_BEARER, HUGGINGFACE_MODEL_ID, HUGGINGFACE_API_URL,
    )

    # comments

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

    # keyword analysis

    @app.route("/api/analysis/keywords/top100", methods=('GET', ))
    def get_keyword_top100():
        stat = get_stat('keyword_top100')
        return jsonify(stat)

    @app.route("/api/analysis/keywords/selected_words", methods=('GET', ))
    def get_keyword_selected_words():
        stat = get_stat('keyword_selected_words')
        return jsonify(stat)

    @app.route("/api/analysis/keywords/occurence", methods=('GET', ))
    def get_keyword_occurence():
        stat = get_stat('keyword_occurence')
        return jsonify(stat)