import pytest
from starlette.testclient import TestClient

from app import main

@pytest.fixture(scope="module")
def test_app():
    with TestClient(main.app) as test_client:
        yield test_client