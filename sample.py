import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def sample_script(some_input: str) -> bool:
    if some_input == 'yes':
        logger.info("Sample script False because yes")
        return False

    logger.info("Sample script True because not yes")
    return True


sample_script('not yes')
