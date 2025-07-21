import pytest
import allure

allure.dynamic.suite("Books - Happy Paths")

@allure.title("Listing all books returns a non-empty list")
@pytest.mark.happy
def test_list_all_books(session, base_url):
    with allure.step("GET /Books"):
        r = session.get(f"{base_url}/Books")

    with allure.step("Verify status code is 200 and list is non-empty"):
        assert r.status_code == 200
        books = r.json()
        assert isinstance(books, list)
        assert books

@allure.title("Creating a book returns 200 and an id")
@pytest.mark.happy
def test_create_book(session, base_url):
    payload = {
        "title": "X",
        "description": "Y",
        "pageCount": 10,
        "excerpt": "",
        "publishDate": "2025-07-20T00:00:00Z"
    }
    with allure.step("POST /Books to create a book"):
        r = session.post(f"{base_url}/Books", json=payload)
    with allure.step("Verify creation returned 200 and book id"):
        assert r.status_code == 200
        data = r.json() or {}
        assert isinstance(data.get("id"), int)
    session.delete(f"{base_url}/Books/{data['id']}")

@allure.title("Updating a book's title persists the change")
@pytest.mark.happy
def test_update_book(session, base_url):
    payload = {
        "title": "X",
        "description": "Y",
        "pageCount": 10,
        "excerpt": "",
        "publishDate": "2025-07-20T00:00:00Z"
    }
    create = session.post(f"{base_url}/Books", json=payload)
    book_id = create.json()["id"]
    with allure.step(f"PUT /Books/{book_id} to update title"):
        updated = session.put(
            f"{base_url}/Books/{book_id}",
            json={**payload, "title": "X2"}
        )
    with allure.step("Verify update returned 200 and new title"):
        assert updated.status_code == 200
        assert updated.json()["title"] == "X2"
    session.delete(f"{base_url}/Books/{book_id}")

@allure.title("Deleting a book returns 200 or 204")
@pytest.mark.happy
def test_delete_book(session, base_url):
    payload = {
        "title": "X",
        "description": "Y",
        "pageCount": 10,
        "excerpt": "",
        "publishDate": "2025-07-20T00:00:00Z"
    }
    create = session.post(f"{base_url}/Books", json=payload)
    book_id = create.json()["id"]
    with allure.step(f"DELETE /Books/{book_id}"):
        resp = session.delete(f"{base_url}/Books/{book_id}")
    with allure.step("Verify delete returned 200 or 204"):
        assert resp.status_code in (200, 204)
