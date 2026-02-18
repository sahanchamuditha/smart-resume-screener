from datetime import timedelta
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://resume_user:resume_pass@db:5432/resume_screener")

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_THIS_TO_A_LONG_RANDOM_STRING")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60