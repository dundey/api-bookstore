import pytest

@pytest.mark.edge
@pytest.mark.parametrize("invalid_id", [-1, 0, 999999])
def test_get_book_with_invalid_ids(session, base_url, invalid_id):
    r = session.get(f"{base_url}/Books/{invalid_id}")
    assert r.status_code in (400, 404)
    assert "id" not in (r.json() or {})

@pytest.mark.edge
def test_create_book_with_minimal_payload(session, base_url):
    r = session.post(f"{base_url}/Books", json={"title": ""})
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data.get("id"), int)
    session.delete(f"{base_url}/Books/{data['id']}")
