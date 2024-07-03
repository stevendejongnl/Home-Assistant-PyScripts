import pytest

from madebysteven_api import MadeByStevenApi
from helpers.dependency_injection import DependencyType


@pytest.mark.asyncio
async def test_response_from_healthcheck_returns_ok():
    madebysteven_api = MadeByStevenApi(dependency_type=DependencyType.FAKE, response={'status': 'ok'})
    response = await madebysteven_api.healthcheck()
    assert response == 'ok'


@pytest.mark.asyncio
async def test_response_from_healthcheck_should_return_unhealthy():
    madebysteven_api = MadeByStevenApi(dependency_type=DependencyType.FAKE, response={})
    response = await madebysteven_api.healthcheck()
    assert response == 'unhealthy'
