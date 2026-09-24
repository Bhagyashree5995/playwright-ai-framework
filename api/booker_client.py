import requests

BASE_URL = "https://restful-booker.herokuapp.com"


class BookerClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def create_token(self, username="admin", password="password123"):
        return requests.post(
            f"{self.base_url}/auth",
            json={"username": username, "password": password},
            timeout=30,
        )

    def create_booking(self, booking):
        return requests.post(f"{self.base_url}/booking", json=booking, timeout=30)

    def get_booking(self, booking_id):
        return requests.get(
            f"{self.base_url}/booking/{booking_id}",
            headers={"Accept": "application/json"},
            timeout=30,
        )

    def update_booking(self, booking_id, booking, token):
        return requests.put(
            f"{self.base_url}/booking/{booking_id}",
            json=booking,
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Cookie": f"token={token}",
            },
            timeout=30,
        )

    def delete_booking(self, booking_id, token):
        return requests.delete(
            f"{self.base_url}/booking/{booking_id}",
            headers={"Cookie": f"token={token}"},
            timeout=30,
        )