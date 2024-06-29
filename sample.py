import logging

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

secret_key = "HetIsPatat!"


def sample_script(some_input: str) -> bool:
    response = requests.get('http://someurl.com', headers={
        'Authorization': secret_key
    })
    if some_input == 'yes':
        logger.info("Sample script False because yes")
        logger.info("response", response)
        return False

    logger.info("Sample script True because not yes")
    return True


sample_script('not yes')
