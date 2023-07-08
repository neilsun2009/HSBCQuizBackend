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
    
    # overview
    
    @app.route("/api/analysis/overview", methods=('GET', ))
    def get_keyword_top100():
        stat = get_stat('overview')
        return jsonify(stat)

    # keyword analysis

    @app.route("/api/analysis/keywords/top500", methods=('GET', ))
    def get_keyword_top500():
        stat = get_stat('keyword_top500')
        return jsonify(stat)

    @app.route("/api/analysis/keywords/selected_words", methods=('GET', ))
    def get_keyword_selected_words():
        stat = get_stat('keyword_selected_words')
        return jsonify(stat)

    @app.route("/api/analysis/keywords/occurrences", methods=('GET', ))
    def get_keyword_occurences():
        stat = get_stat('keyword_occurrences')
        return jsonify(stat)
    
    # comment analysis
    
    @app.route("/api/analysis/comments/lengths", methods=('GET', ))
    def get_comment_lengths():
        stat = get_stat('comment_lengths')
        return jsonify(stat)
    
    @app.route("/api/analysis/comments/ratings", methods=('GET', ))
    def get_comment_ratings():
        stat = get_stat('comment_ratings')
        return jsonify(stat)
    
    @app.route("/api/analysis/comments/sentiments", methods=('GET', ))
    def get_comment_sentiments():
        stat = get_stat('comment_sentiments')
        return jsonify(stat)
    
    # customer clustering
    
    @app.route("/api/analysis/customers/cluster_points", methods=('GET', ))
    def get_customer_cluster_points():
        stat = get_stat('customer_cluster_points')
        return jsonify(stat)
    
    @app.route("/api/analysis/customers/clusters", methods=('GET', ))
    def get_customer_clusters():
        stat = get_stat('customer_clusters')
        return jsonify(stat)
    
    # product analysis
    @app.route("/api/analysis/products/bests", methods=('GET', ))
    def get_best_products():
        stat = get_stat('product_best_products')
        return jsonify(stat)
    
    @app.route("/api/analysis/products/worsts", methods=('GET', ))
    def get_worst_products():
        stat = get_stat('product_worst_products')
        return jsonify(stat)
    
    @app.route("/api/analysis/products/comment_counts", methods=('GET', ))
    def get_product_comment_counts():
        stat = get_stat('product_comment_counts')
        return jsonify(stat)
    
    