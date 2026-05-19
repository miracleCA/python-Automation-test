from locust import HttpUser, task

class APIUser(HttpUser):

    def auth(self):
        self.client.auth = ("test1", "test123")

    @task
    def get_integrations(self):
        self.client.get("/api/v1/integrations")