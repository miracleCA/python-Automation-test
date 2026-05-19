from data.test_payloads import valid_integration

def test_list_integrations(integration_client):
    res = integration_client.list_integrations()
    assert res.status_code == 200

def test_create_integration(integration_client):
    res = integration_client.create_integration(valid_integration)
    assert res.status_code in [200, 201]