import pytest, json


def test_status(test_client):
    res = test_client.get("/api/v1/status")
    assert res.status_code == 200
    expected = "diagnose app: Version 1"
    result = res.get_data().decode("utf-8")
    assert expected == result

def test_not_status(test_client):
    res = test_client.post("/api/v1/status")
    assert res.status_code == 405

# re-write create post test
def test_post(test_client):
    test_payload = {
        'code': 'X00',
        'short_desc': 'short description',
        'long_desc': 'long long long description',
        'type': 'ICD-10',
        'year':'2018'
    }
    pass