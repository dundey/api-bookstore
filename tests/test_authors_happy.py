import pytest

@pytest.mark.happy
def test_list_all_authors(session, base_url):
    r = session.get(f"{base_url}/Authors")
    assert r.status_code == 200
    authors = r.json()
    assert isinstance(authors, list)
    assert authors

@pytest.mark.happy
def test_create_update_delete_author(session, base_url):
    payload = {"idBook": 1, "firstName": "Jane", "lastName": "Doe"}
    # Create
    r = session.post(f"{base_url}/Authors", json=payload)
    assert r.status_code == 200
    author_id = r.json()["id"]

    # Update
    r = session.put(f"{base_url}/Authors/{author_id}", json={**payload, "firstName": "John"})
    assert r.status_code == 200
    assert r.json()["firstName"] == "John"

    # Delete
    assert session.delete(f"{base_url}/Authors/{author_id}").status_code == 200
