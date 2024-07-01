import logging

from pyscript.helpers.logging import LoggerHelper
from pyscript.madebysteven_api.madebysteven_api import MadeByStevenApi


logger = LoggerHelper.get_logger(__name__, logging.INFO)


@service
def made_by_steven_api():
    logger.error("init")
    MadeByStevenApi().healthcheck()
