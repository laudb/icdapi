import pytest, json


def test_status(test_client):
    res = test_client.get("/api/v1/status")
    assert res.status_code == 200
    expected = "diagnose app: Version 1"
    result = res.get_data().decode("utf-8")
    assert expected == result
