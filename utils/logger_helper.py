import logging
from pathlib import Path


LOG_FILE = Path(__file__).resolve().parents[1] / "logs" / "logs_outcome.log"


def get_logger(name="pytest_tests"):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger
