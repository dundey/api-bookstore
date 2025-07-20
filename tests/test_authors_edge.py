import pytest

@pytest.mark.edge
@pytest.mark.parametrize("invalid_id", [-1, 0, 999999])
def test_get_author_with_invalid_ids(session, base_url, invalid_id):
    r = session.get(f"{base_url}/Authors/{invalid_id}")
    assert r.status_code in (400, 404)
    assert "id" not in (r.json() or {})

@pytest.mark.edge
def test_create_author_with_minimal_payload(session, base_url):
    r = session.post(f"{base_url}/Authors", json={"firstName": "", "lastName": ""})
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data.get("id"), int)
    session.delete(f"{base_url}/Authors/{data['id']}")
