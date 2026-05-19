from clients.base_client import BaseClient

class IntegrationClient(BaseClient):

    def list_integrations(self):
        return self.get("/integrations")

    def get_integration(self, integration_id):
        return self.get(f"/integrations/{integration_id}")

    def create_integration(self, payload):
        return self.post("/integrations", json=payload)

    def update_integration(self, payload):
        return self.put("/integrations", json=payload)

    def delete_integration(self, integration_id):
        return self.delete(f"/integrations/{integration_id}")