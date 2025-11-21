import os
from pathlib import Path
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

# If using sqlite, force absolute path so dashboard + pipeline use same file
db_url = os.getenv("DB_URL", "sqlite:///retail.db")

if db_url.startswith("sqlite:///") and "///" in db_url:
    # convert sqlite:///retail.db  -> sqlite:////ABS/PATH/retail.db
    DB_URL = f"sqlite:///{(ROOT / 'retail.db').resolve()}"
else:
    DB_URL = db_url

STREAM_DELAY = int(os.getenv("STREAM_DELAY", 3))
