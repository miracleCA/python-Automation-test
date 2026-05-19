from clients.integration_client import IntegrationClient

def test_invalid_auth():
    client = IntegrationClient("wrong", "wrong")
    res = client.list_integrations()
    assert res.status_code == 401