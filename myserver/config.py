import os

STATIC_URL_PREFIX = 'https://szbstorage.z20.web.core.windows.net/'

HUGGINGFACE_BEARER = os.environ.get('HF_BEARER')
HUGGINGFACE_MODEL_ID = 'neilsun2009/amz_movie_tv_distilgpt2_1k'
HUGGINGFACE_API_URL = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL_ID}"

STATS_BASE_DIR = './stats/'

KEYWORD_TOP100_PATH = os.path.join(STATS_BASE_DIR, 'keyword/top100.json')
KEYWORD_SELECTED_WORDS_PATH = os.path.join(STATS_BASE_DIR, 'keyword/selected_words.json')
KEYWORD_OCCURRENCE_PATH = os.path.join(STATS_BASE_DIR, 'keyword/occurrence.json')