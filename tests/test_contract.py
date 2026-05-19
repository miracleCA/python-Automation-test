def test_integrations_contract(integration_client):
    res = integration_client.list_integrations()

    assert res.status_code == 200

    data = res.json()

    assert isinstance(data, list), (
        f"Contract violation: /integrations must return list, "
        f"got {type(data)} with value {data}"
    )

