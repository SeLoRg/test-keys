import logging
import sys


def get_logger(name: str = "main", level: int = logging.INFO) -> logging.Logger:
    """
    Возвращает настроенный логгер с выводом в stdout.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
