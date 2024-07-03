import logging

from pyscript.helpers.logging import LoggerHelper
from pyscript.apps.madebysteven_api.madebysteven_api import MadeByStevenApi


##
# documentation
# https://hacs-pyscript.readthedocs.io/en/latest/reference.html
##

logger = LoggerHelper.get_logger(__name__, logging.INFO)

INTERNAL_IP_NOT_SET = 'INTERNAL_IP NOT SET'


@service
async def made_by_steven_api():
    config = pyscript.app_config
    internal_ip = config.get('internal_ip', INTERNAL_IP_NOT_SET)
    status = await MadeByStevenApi(
        internal_ip=internal_ip
    ).healthcheck()
    state.set('sensor.made_by_steven_api', value=status)
