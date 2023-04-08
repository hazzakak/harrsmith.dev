import io
import sys
from pathlib import Path
import sys

import pytest
import requests
sys.path.append('../')

from main import app
import config

@pytest.fixture
def client():
    BASE_DIR = Path(__file__).resolve().parent.parent
    app.config["TESTING"] = True

    yield app.test_client() # tests run here

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert b"Harry Smith" in response.data

def test_database():
    assert Path("../utils/app.db").is_file()

def test_images():
    tester = app.test_client()
    response = tester.get("/images/1?pswdpin=0p;1043%<AJ832£LD9nSuw%27Cjsh%3", content_type="html/text")

    assert response.status_code == 200
    assert b"Images" in response.data


def test_post_images():
    tester = app.test_client()
    rv = tester.post(
        "/api/v1.0/images/upload",
        data={"api_key": config.api_key, "api_image": (io.BytesIO(b"abcdef"), 'test.jpg')},
        follow_redirects=True,
    )

    assert b"image received" in rv.data