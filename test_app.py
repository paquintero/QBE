import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_validate_success():
    response = client.post("/validate", json={
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "Validation passed"}

def test_validate_invalid_var_name():
    response = client.post("/validate", json={
        "data": [
            {"var_name": "invalid_var", "category": "UK"}
        ]
    })
    assert response.status_code == 422  # Unprocessable Entity

def test_validate_invalid_category():
    response = client.post("/validate", json={
        "data": [
            {"var_name": "country", "category": "InvalidCategory"}
        ]
    })
    assert response.status_code == 422  # Unprocessable Entity

def test_get_factors_success():
    response = client.post("/get_factors", json={
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    })
    assert response.status_code == 200
    assert response.json() == {
        "results": [
            {"var_name": "country", "category": "UK", "factor": 0.25},
            {"var_name": "age_group", "category": "30-50", "factor": 0.33}
        ]
    }
