import pytest
import allure

allure.dynamic.suite("Books - Happy Paths")

@pytest.mark.happy
@allure.title("Listing all books")
def test_list_all_books(session, base_url):
    with allure.step("GET /Books"):
        r = session.get(f"{base_url}/Books")

    with allure.step("Verify status code is 200 and list is non-empty"):
        assert r.status_code == 200
        books = r.json()
        assert isinstance(books, list) and books

@pytest.mark.happy
@allure.title("Retrieving a book by ID")
def test_get_book_by_id(session, base_url, book_keys):
    book_id = 1  
    with allure.step(f"GET /Books/{book_id}"):
        r = session.get(f"{base_url}/Books/{book_id}")

    with allure.step("Verify status code is 200 and JSON keys"):
        assert r.status_code == 200
        data = r.json()
        assert set(data.keys()) == book_keys

@pytest.mark.happy
@allure.title("Creating a book")
def test_create_book(session, base_url, sample_book_payload):
    with allure.step("POST /Books to create a book"):
        r = session.post(f"{base_url}/Books", json=sample_book_payload)

    with allure.step("Verify creation returned 200 and book id"):
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data.get("id"), int)

    with allure.step("Clean up by deleting the new book"):
        session.delete(f"{base_url}/Books/{data['id']}")

@pytest.mark.happy
@allure.title("Updating a book's title")
def test_update_book(session, base_url, sample_book_payload):
    with allure.step("POST /Books to create a book"):
        create = session.post(f"{base_url}/Books", json=sample_book_payload)
    book_id = create.json()["id"]

    with allure.step(f"PUT /Books/{book_id} to update title"):
        updated = session.put(
            f"{base_url}/Books/{book_id}",
            json={**sample_book_payload, "title": "X2"}
        )

    with allure.step("Verify update returned 200 and new title"):
        assert updated.status_code == 200
        assert updated.json()["title"] == "X2"

    with allure.step("Clean up by deleting the updated book"):
        session.delete(f"{base_url}/Books/{book_id}")

@pytest.mark.happy
@allure.title("Deleting a book")
def test_delete_book(session, base_url, sample_book_payload):
    with allure.step("POST /Books to create a book"):
        create = session.post(f"{base_url}/Books", json=sample_book_payload)
    book_id = create.json()["id"]

    with allure.step(f"DELETE /Books/{book_id}"):
        resp = session.delete(f"{base_url}/Books/{book_id}")

    with allure.step("Verify delete returned 200 or 204"):
        assert resp.status_code in (200, 204)
