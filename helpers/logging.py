import logging


class LoggerHelper:
    @staticmethod
    def get_logger(name: str, level: int = logging.DEBUG):
        logger = logging.getLogger(name)
        logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
