import requests

base_url = "https://x-clients-be.onrender.com"

def test_simple_req():

    resp = requests.get(base_url + '/company')
    response_body = resp.json()
    first_company = response_body[0]

    assert first_company["name"] == "Барбершоп 'ЦирюльникЪ'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
