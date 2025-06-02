import logging


def get_log(name: str, level: int = logging.DEBUG) -> logging.Logger:
    logger = logging.getLogger(name=name)
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(level)
    return logger
