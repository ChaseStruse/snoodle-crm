import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = Path("./logs/company_management_logs.log")

def setup_logger(name: str) -> logging.Logger:
    """
    Sets up a logger with console + rotating file handlers.
    Each module can call this with its __name__.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG) 

    if not logger.handlers:
        # Format
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Console handler (INFO+)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # File handler with rotation (DEBUG+)
        file_handler = RotatingFileHandler(
            LOG_FILE, maxBytes=1_000_000, backupCount=5, encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
