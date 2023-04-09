import io
import os
import sys
from pathlib import Path
import pytest
import datetime

sys.path.append('../')
from main import app

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
    assert Path("utils/app.db").is_file()

def test_date():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")
    
    today = datetime.date.today()
    year = str(today.year)
    
    assert response.status_code == 200
    assert bytes(year, encoding='utf-8') in response.data

def test_page_title():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")
    
    title = response.data
    title = title[title.find(b'<title>') + 7 : title.find(b'</title>')]
    
    assert response.status_code == 200
    assert b"Home | harrysmith.dev" in title

if 'TEST' not in os.environ:
    def test_images():
        tester = app.test_client()
        response = tester.get(f"/images/1?pswdpin={ os.environ.get('password_hs') }", content_type="html/text")

        assert response.status_code == 200
        assert b"Images" in response.data


    def test_post_images():
        tester = app.test_client()
        rv = tester.post(
            "/api/v1.0/images/upload",
            data={"api_key": os.getenv("api_key_hs"), "api_image": (io.BytesIO(b"abcdef"), 'test.jpg')},
            follow_redirects=True,
        )

        assert b"image received" in rv.data
