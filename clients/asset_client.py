from clients.base_client import BaseClient

class AssetClient(BaseClient):

    def list_assets(self, integration_id):
        return self.get("/assets", params={"integrationId": integration_id})

    def get_asset(self, asset_id):
        return self.get(f"/assets/{asset_id}")

    def create_asset(self, payload):
        return self.post("/assets", json=payload)

    def update_asset(self, payload):
        return self.patch("/assets", json=payload)

    def delete_asset(self, asset_id):
        return self.delete(f"/assets/{asset_id}")