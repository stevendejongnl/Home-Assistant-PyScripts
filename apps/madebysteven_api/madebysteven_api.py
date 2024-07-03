from __future__ import annotations

import logging

import aiohttp

from helpers.dependency_injection import DependencyInjection, DependencyType, register_dependency
from helpers.logging import LoggerHelper

logger = LoggerHelper.get_logger(__name__, logging.INFO)


@register_dependency(DependencyType.FAKE)
class MadeByStevenApiFake:
    internal_api: str
    response: dict = {}

    def __init__(self, response: dict | None = None):
        self.internal_api = 'https://fake-url.com'
        if response is not None:
            self.response = response

    async def healthcheck(self) -> str:
        status = self.response.get('status', 'No status found')
        if status == 'ok':
            return 'ok'
        return 'unhealthy'


@register_dependency(DependencyType.REAL)
class MadeByStevenApiReal:
    internal_url: str

    def __init__(self, internal_ip: str) -> None:
        self.internal_url = f"https://{internal_ip}/health"

    async def healthcheck(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.internal_url, ssl=False) as resp:
                content = await resp.json()
                status = content.get('status', 'No status found')
                logger.info(f'Response from MadeBySteven API: {status}')
                if resp.status == 200 and status == 'ok':
                    logger.info('MadeBySteven API Healthy')
                    return 'ok'

        logger.error('MadeBySteven API Unhealthy')
        return 'unhealthy'


class MadeByStevenApi:
    def __init__(self, dependency_type=DependencyType.REAL, *args, **kwargs):
        dependency_injection = DependencyInjection()
        dependency_injection.use_type(dependency_type)
        self.api = dependency_injection.get(MadeByStevenApiReal, MadeByStevenApiFake, *args, **kwargs)

    def healthcheck(self):
        return self.api.healthcheck()
