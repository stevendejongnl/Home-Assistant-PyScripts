from __future__ import annotations
import logging
import requests

from helpers.logging import LoggerHelper
from helpers.dependency_injection import DependencyInjection, DependencyType, register_dependency

# from hassapi import Hass

logger = LoggerHelper.get_logger(__name__, logging.INFO)


@register_dependency(DependencyType.FAKE)
class MadeByStevenApiFake:
    internal_api: str
    response: str = ''

    def __init__(self, response: str | None = None):
        self.internal_api = 'https://fake-url.com'
        if response:
            self.response = response

    def healthcheck(self):
        return self.response


@register_dependency(DependencyType.REAL)
class MadeByStevenApiReal:
    # internal_ip: str

    # def __init__(self):
    #     self.internal_ip = Hass(hassurl="http://IP_ADDRESS:8123/", token="YOUR_HASS_TOKEN")

    @staticmethod
    def healthcheck():
        # print(self.internal_ip)
        response = requests.get('https://192.168.2.34:8123/health')
        logger.error(response.text)


class MadeByStevenApi:
    def __init__(self, dependency_type=DependencyType.REAL, *args, **kwargs):
        dependency_injection = DependencyInjection()
        dependency_injection.use_type(dependency_type)
        self.api = dependency_injection.get(MadeByStevenApiReal, MadeByStevenApiFake, *args, **kwargs)

    def healthcheck(self):
        return self.api.healthcheck()
