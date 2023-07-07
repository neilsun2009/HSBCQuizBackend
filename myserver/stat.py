import json
import os
from .config import (
    KEYWORD_TOP100_PATH, KEYWORD_SELECTED_WORDS_PATH, KEYWORD_OCCURRENCE_PATH,
    
)

stat_map = dict()

def prepare_stats():
    
    # keyword analysis
    with open(KEYWORD_TOP100_PATH) as f:
        keyword_top100 = json.load(f)
    stat_map['keyword_top100'] = keyword_top100
    
    with open(KEYWORD_SELECTED_WORDS_PATH) as f:
        keyword_selected_words = json.load(f)
    stat_map['keyword_selected_words'] = keyword_selected_words
    
    with open(KEYWORD_OCCURRENCE_PATH) as f:
        keyword_occurence = json.load(f)
    stat_map['keyword_occurrence'] = keyword_occurence


def get_stat(key):
    if key not in stat_map:
        raise ValueError(f'key {key} not found in stat map')
    return stat_map[key]
