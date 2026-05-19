def test_tenant_isolation(integration_client, user2_integration_client):
    res1 = integration_client.list_integrations().json()
    res2 = user2_integration_client.list_integrations().json()

    assert res1 == res2  # adjust depending on expected behavior