import os
from dotenv import load_dotenv
load_dotenv()


# app settings
PROJECT_TITLE = "ML api"
API_PREFIX = "/api"
DOCS_URL = API_PREFIX + "/docs"

# celery / redis settings
REDIS_URL = os.getenv("REDIS_URL")

# AWS S3 settings
FROM_S3 = os.getenv("FROM_S3")
AWS_SERVER_PUBLIC_KEY = os.getenv("AWS_SERVER_PUBLIC_KEY")
AWS_SERVER_SECRET_KEY = os.getenv("AWS_SERVER_SECRET_KEY")
REGION_NAME = os.getenv("REGION_NAME")
MODELS_FILES_BUCKET_NAME = os.getenv("MODELS_FILES_BUCKET_NAME")