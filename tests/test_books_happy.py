import pytest

@pytest.mark.happy
def test_list_all_books(session, base_url):
    r = session.get(f"{base_url}/Books")
    assert r.status_code == 200
    books = r.json()
    assert isinstance(books, list)
    assert books 

@pytest.mark.happy
def test_create_update_delete_book(session, base_url):
    payload = {
        "title": "X",
        "description": "Y",
        "pageCount": 10,
        "excerpt": "",
        "publishDate": "2025-07-20T00:00:00Z"
    }
    # Create
    r = session.post(f"{base_url}/Books", json=payload)
    assert r.status_code == 200
    book_id = r.json()["id"]

    # Update
    r = session.put(f"{base_url}/Books/{book_id}", json={**payload, "title": "X2"})
    assert r.status_code == 200
    assert r.json()["title"] == "X2"

    # Delete
    assert session.delete(f"{base_url}/Books/{book_id}").status_code == 200
