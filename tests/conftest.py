import pytest
from clients.integration_client import IntegrationClient
from clients.asset_client import AssetClient
from config.settings import USERS

@pytest.fixture
def integration_client():
    return IntegrationClient("test1", USERS["test1"])

@pytest.fixture
def asset_client():
    return AssetClient("test1", USERS["test1"])

@pytest.fixture
def user2_integration_client():
    return IntegrationClient("test2", USERS["test2"])