from helpers.dependency_injection import DependencyType
from madebysteven_api.madebysteven_api import MadeByStevenApi


def test_response_from_healthcheck_returns_ok():
    madebysteven_api = MadeByStevenApi(DependencyType.FAKE)
    response = madebysteven_api.healthcheck()
    assert response == 'ok'
