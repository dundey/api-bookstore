import pytest
import allure

allure.dynamic.suite("Authors - Edge Cases") 

@allure.title("Requesting an author with invalid ID returns 400 or 404 and no 'id' key")
@pytest.mark.edge
@pytest.mark.parametrize("invalid_id", [-1, 0, 999999])
def test_get_author_with_invalid_ids(session, base_url, invalid_id):
    with allure.step(f"GET /Authors/{invalid_id}"):
        r = session.get(f"{base_url}/Authors/{invalid_id}")

    with allure.step("Verify status code is 400 or 404"):
        assert r.status_code in (400, 404)

    with allure.step("Verify response has no 'id' key"):
        data = r.json() or {}
        assert "id" not in data

@allure.title("Creating an author with minimal payload returns 200 and an id")
@pytest.mark.edge
def test_create_author_with_minimal_payload(session, base_url):
    with allure.step("POST /Authors with minimal payload"):
        r = session.post(
            f"{base_url}/Authors",
            json={"firstName": "", "lastName": ""}
        )

    with allure.step("Verify status code is 200 and an id is returned"):
        assert r.status_code == 200
        data = r.json() or {}
        assert isinstance(data.get("id"), int)

    with allure.step("Clean up by deleting the new author"):
        session.delete(f"{base_url}/Authors/{data['id']}")