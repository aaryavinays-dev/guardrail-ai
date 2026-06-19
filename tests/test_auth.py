import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient

from auth import verify_api_key
from main import app


client = TestClient(app)


def test_verify_api_key_allows_valid_key(monkeypatch):
    monkeypatch.setenv("GUARDRAIL_API_KEY", "test-key")

    result = verify_api_key(api_key="test-key")

    assert result is None


def test_verify_api_key_rejects_missing_key(monkeypatch):
    monkeypatch.setenv("GUARDRAIL_API_KEY", "test-key")

    with pytest.raises(HTTPException) as error:
        verify_api_key(api_key=None)

    assert error.value.status_code == 401
    assert error.value.detail == "Invalid or missing API key"


def test_verify_api_key_rejects_wrong_key(monkeypatch):
    monkeypatch.setenv("GUARDRAIL_API_KEY", "test-key")

    with pytest.raises(HTTPException) as error:
        verify_api_key(api_key="wrong-key")

    assert error.value.status_code == 401
    assert error.value.detail == "Invalid or missing API key"


def test_verify_api_key_requires_server_config(monkeypatch):
    monkeypatch.delenv("GUARDRAIL_API_KEY", raising=False)

    with pytest.raises(HTTPException) as error:
        verify_api_key(api_key="test-key")

    assert error.value.status_code == 500
    assert error.value.detail == "API key is not configured on the server"


def test_analyze_endpoint_requires_api_key(monkeypatch):
    monkeypatch.setenv("GUARDRAIL_API_KEY", "test-key")

    response = client.post(
        "/analyze",
        json={"prompt": "hello",
              "user_id": "user_test",
              "department": "Engineering"},

    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or missing API key"


def test_audit_summary_endpoint_requires_api_key(monkeypatch):
    monkeypatch.setenv("GUARDRAIL_API_KEY", "test-key")

    response = client.get("/audit-summary")

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or missing API key"