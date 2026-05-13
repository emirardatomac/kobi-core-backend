import os
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("CORE_BACKEND_URL")


def get_order_status(order_id: int):

    print("ORDER API CALLED:", order_id)

    response = requests.get(
        f"{BASE_URL}/api/v1/orders/{order_id}"
    )

    return response.json()


def check_inventory():

    print("INVENTORY API CALLED")

    response = requests.get(
        f"{BASE_URL}/api/v1/inventory/critical"
    )

    return response.json()


def get_cargo_status(tracking_id: str):

    print("CARGO API CALLED:", tracking_id)

    response = requests.get(
        f"{BASE_URL}/api/v1/cargo/{tracking_id}"
    )

    return response.json()


def get_dashboard_summary():

    print("DASHBOARD API CALLED")

    response = requests.get(
        f"{BASE_URL}/api/v1/dashboard/summary"
    )

    return response.json()