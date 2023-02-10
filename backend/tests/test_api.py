from typing import Iterator, cast

import pytest
from flask import Flask
from flask.testing import FlaskClient

from spp.app import app


@pytest.fixture
def test_app() -> Iterator[Flask]:
    client_app: Flask = cast(Flask, app.app)
    client_app.testing = True
    yield client_app


@pytest.fixture
def client(test_app: Flask) -> FlaskClient:
    return test_app.test_client()


def test_sample_endpoint(client: FlaskClient):
    response = client.get("/api/")
    assert response.json == []
