# import pytest
# from main import app

# def test_root_ok():
#     client = app.test_client()
#     r = client.get("/")
#     assert r.status_code == 200
#     assert "message" in r.get_json()


import pytest
from main import app

def test_root_ok():
    client = app.test_client()
    response = client.get("/")
    
    # Assert HTTP status code is 200 OK
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    # Parse JSON data from response
    json_data = response.get_json()
    
    # Assert that JSON data is not None
    assert json_data is not None, "Response did not return JSON"
    
    # Assert that 'message' key exists in the JSON response
    assert "message" in json_data, "'message' key not found in response JSON"
