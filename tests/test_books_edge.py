import pytest
import allure

allure.dynamic.suite("Books - Edge Cases")

@allure.title("Requesting a book with invalid ID returns 400 or 404 and no 'id' key")
@pytest.mark.edge
@pytest.mark.parametrize("invalid_id", [-1, 0, 999999])
def test_get_book_with_invalid_ids(session, base_url, invalid_id):
    with allure.step(f"GET /Books/{invalid_id}"):
        r = session.get(f"{base_url}/Books/{invalid_id}")

    with allure.step("Verify status code is 400 or 404"):
        assert r.status_code in (400, 404)

    with allure.step("Verify response has no 'id' key"):
        data = r.json() or {}
        assert "id" not in data

@allure.title("Creating a book with minimal payload returns 200 and an id")
@pytest.mark.edge
def test_create_book_with_minimal_payload(session, base_url):
    with allure.step("POST /Books with minimal payload"):
        r = session.post(f"{base_url}/Books", json={"title": ""})

    with allure.step("Verify status code is 200 and an id is returned"):
        assert r.status_code == 200
        data = r.json() or {}
        assert isinstance(data.get("id"), int)

    with allure.step("Clean up by deleting the new book"):
        session.delete(f"{base_url}/Books/{data['id']}")