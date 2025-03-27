from locust import HttpUser, task


class Object(HttpUser):
    object_id = None

    def on_start(self):
        payload = {
            "name": "qa_initial",
            "data": {"cat": "dusa"}}
        headers = {"Content-Type": "application/json"}

        response = self.client.post("/object", json=payload, headers=headers)
        response_data = response.json()
        self.object_id = response_data.get("id")

    @task(1)
    def create_object(self):
        # Создан для проверки производительности
        # создавая множество объектов для пользователя

        payload = {
            "name": "qa_initial",
            "data": {"cat": "dusa"}}
        headers = {"Content-Type": "application/json"}

        response = self.client.post("/object", json=payload, headers=headers)
        response_data = response.json()
        self.object_id = response_data.get("id")

    @task(2)
    def get_all_objects(self):
        headers = {"Content-Type": "application/json"}
        self.client.get("/object", headers=headers)

    @task(3)
    def get_object_by_id(self):
        headers = {"Content-Type": "application/json"}
        self.client.get(f"/object/{self.object_id}", headers=headers)

    @task(4)
    def change_object_method_put(self):
        headers = {"Content-Type": "application/json"}
        payload = {
            "name": "qa_put",
            "data": {"cat": "dusa_2"}}
        self.client.put(f"/object/{self.object_id}", headers=headers, json=payload)

    @task(5)
    def change_object_method_patch(self):
        headers = {"Content-Type": "application/json"}
        payload = {"name": "qa_patch"}
        self.client.patch(f"/object/{self.object_id}", headers=headers, json=payload)

    def on_stop(self):
        self.client.delete(f'/object/{self.object_id}')
