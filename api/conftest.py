import pytest
import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com"

import os

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")

@pytest.fixture(scope="session")
def api_client():
    """
    Session-level API client
    """
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()


@pytest.fixture
def get_response(api_client):
    """
    Generic GET request fixture
    Usage: get_response("/posts")
    """
    def _get(endpoint):
        return api_client.get(f"{BASE_URL}{endpoint}")
    
    return _get


def load_schema(path):
    with open(path) as f:
        return json.load(f)