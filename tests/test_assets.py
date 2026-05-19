def test_assets_requires_integration_id(asset_client):
    res = asset_client.get("/assets")
    assert res.status_code == 400
    assert "integrationId" in res.json()["error"]

def test_list_assets(asset_client):
    res = asset_client.list_assets("1")
    assert res.status_code in [200, 404]