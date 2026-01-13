# src/utils/logger.py
import logging
import os

LOG_FILE = os.path.join("logs", "app.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Make logging available for import
logger = logging
