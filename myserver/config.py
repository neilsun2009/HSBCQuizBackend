import os

STATIC_URL_PREFIX = 'https://szbstorage.z20.web.core.windows.net/'

HUGGINGFACE_BEARER = os.environ.get('HF_BEARER')
HUGGINGFACE_MODEL_ID = 'neilsun2009/amz_movie_tv_distilgpt2_1k'
HUGGINGFACE_API_URL = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL_ID}"

STATS_BASE_DIR = './stats/'

OVERVIEW_PATH = os.path.join(STATS_BASE_DIR, 'overview/overview.json')

KEYWORD_TOP500_PATH = os.path.join(STATS_BASE_DIR, 'keyword/top500.json')
KEYWORD_SELECTED_WORDS_PATH = os.path.join(STATS_BASE_DIR, 'keyword/selected_words.json')
KEYWORD_OCCURRENCE_PATH = os.path.join(STATS_BASE_DIR, 'keyword/occurrence.json')

COMMENT_LENGTH_PATH = os.path.join(STATS_BASE_DIR, 'comment/length.json')
COMMENT_RATING_PATH = os.path.join(STATS_BASE_DIR, 'comment/rating.json')
COMMENT_SENTIMENT_PATH = os.path.join(STATS_BASE_DIR, 'comment/sentiment.json')

CUSTOMER_CLUSTER_POINTS_PATH = os.path.join(STATS_BASE_DIR, 'customer/cluster_points.json')
CUSTOMER_CLUSTERS_PATH = os.path.join(STATS_BASE_DIR, 'customer/clusters.json')

PRODUCT_BEST_PATH = os.path.join(STATS_BASE_DIR, 'product/best_products.json')
PRODUCT_WORST_PATH = os.path.join(STATS_BASE_DIR, 'product/worst_products.json')
PRODUCT_COMMENT_COUNT_PATH = os.path.join(STATS_BASE_DIR, 'product/comment_count.json')