from __future__ import annotations
import logging
import requests

from helpers.logging import LoggerHelper
from helpers.dependency_injection import DependencyInjection, DependencyType, add_dependency

# from hassapi import Hass

logger = LoggerHelper.get_logger(__name__, logging.INFO)


@add_dependency(DependencyType.FAKE)
class MadeByStevenApiFake:
    internal_api: str
    response: str

    def __init__(self, response: any):
        self.internal_api = 'https://fake-url.com'
        self.response = response

    def healthcheck(self):
        return self.response


@add_dependency(DependencyType.REAL)
class MadeByStevenApiReal:
    internal_ip: str

    # def __init__(self):
    # self.internal_ip = Hass(hassurl="http://IP_ADDRESS:8123/", token="YOUR_HASS_TOKEN")

    def healthcheck(self):
        print(self.internal_ip)
        response = requests.get('https://192.168.2.34:8123/health')
        logger.error(response.text)


class MadeByStevenApi:
    def __init__(self, dependency_type=DependencyType.REAL):
        dependency_injection = DependencyInjection()
        self.api = dependency_injection.get_dependency(MadeByStevenApiFake)
        if dependency_type == DependencyType.REAL:
            self.api = dependency_injection.get_dependency(MadeByStevenApiReal)

    def healthcheck(self):
        return self.api.healthcheck()
