# import pytest
# from main import app

# def test_root_ok():
#     client = app.test_client()
#     r = client.get("/")
#     assert r.status_code == 200
#     assert "message" in r.get_json()


import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200, f"Expected 200 OK but got {response.status_code}"

def test_home_contains_expected_html(client):
    response = client.get("/")
    html = response.get_data(as_text=True)
    # Basic check: page contains a known string from your index.html, e.g., title text in Hindi
    assert "जय श्री राम" in html, "Home page does not contain expected title"

def test_content_type_html(client):
    response = client.get("/")
    assert "text/html" in response.content_type, "Response is not HTML"
