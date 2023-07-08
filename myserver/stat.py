import json
import os
from .config import (
    OVERVIEW_PATH,
    KEYWORD_TOP500_PATH, KEYWORD_SELECTED_WORDS_PATH, KEYWORD_OCCURRENCE_PATH,
    COMMENT_LENGTH_PATH, COMMENT_RATING_PATH, COMMENT_SENTIMENT_PATH,
    CUSTOMER_CLUSTER_POINTS_PATH, CUSTOMER_CLUSTERS_PATH,
    PRODUCT_BEST_PATH, PRODUCT_WORST_PATH, PRODUCT_COMMENT_COUNT_PATH,
)

stat_map = dict()

def prepare_stats():
    
    # overview
    with open(OVERVIEW_PATH) as f:
        overview = json.load(f)
    stat_map['overview'] = overview
    
    # keyword analysis
    with open(KEYWORD_TOP500_PATH) as f:
        keyword_top500 = json.load(f)
    stat_map['keyword_top500'] = keyword_top500
    
    with open(KEYWORD_SELECTED_WORDS_PATH) as f:
        keyword_selected_words = json.load(f)
    stat_map['keyword_selected_words'] = keyword_selected_words
    
    with open(KEYWORD_OCCURRENCE_PATH) as f:
        keyword_occurences = json.load(f)
    stat_map['keyword_occurrences'] = keyword_occurences
    
    # comment analysis
    with open(COMMENT_LENGTH_PATH) as f:
        comment_lengths = json.load(f)
    stat_map['comment_lengths'] = comment_lengths
    
    with open(COMMENT_RATING_PATH) as f:
        comment_ratings = json.load(f)
    stat_map['comment_ratings'] = comment_ratings
    
    with open(COMMENT_SENTIMENT_PATH) as f:
        comment_sentiments = json.load(f)
    stat_map['comment_sentiments'] = comment_sentiments
    
    # customer clustering
    with open(CUSTOMER_CLUSTER_POINTS_PATH) as f:
        customer_cluster_points = json.load(f)
    stat_map['customer_cluster_points'] = customer_cluster_points
    
    with open(CUSTOMER_CLUSTERS_PATH) as f:
        customer_clusters = json.load(f)
    stat_map['customer_clusters'] = customer_clusters
    
    # product analysis
    with open(PRODUCT_BEST_PATH) as f:
        product_best_products = json.load(f)
    stat_map['product_best_products'] = product_best_products
    
    with open(PRODUCT_WORST_PATH) as f:
        product_worst_products = json.load(f)
    stat_map['product_worst_products'] = product_worst_products
    
    with open(PRODUCT_COMMENT_COUNT_PATH) as f:
        product_comment_counts = json.load(f)
    stat_map['product_comment_counts'] = product_comment_counts
    


def get_stat(key):
    if key not in stat_map:
        raise ValueError(f'key {key} not found in stat map')
    return stat_map[key]
