import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_slope():
    response = client.get("/api/v1/cartesian/slope?x1=1&x2=3&y1=2&y2=6")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 200
    assert data["message"] == "2.0"

def test_calculate_slope_negative():
    response = client.get("/api/v1/cartesian/slope?x1=1&x2=4&y1=3&y2=0")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 200
    assert data["message"] == "-1.0"

def test_calculate_slope_vertical_line():
    with pytest.raises(ZeroDivisionError):
        client.get("/api/v1/cartesian/slope?x1=1&x2=1&y1=0&y2=5")

def test_calculate_slope_zero():
    response = client.get("/api/v1/cartesian/slope?x1=1&x2=5&y1=2&y2=2")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == 200
    assert data["message"] == "0.0"
