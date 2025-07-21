import pytest
import allure

allure.dynamic.suite("Authors - Happy Paths")

@allure.title("Listing all authors returns a non-empty list")
@pytest.mark.happy
def test_list_all_authors(session, base_url):
    with allure.step("GET /Authors"):
        r = session.get(f"{base_url}/Authors")
    with allure.step("Verify status code is 200 and list is non-empty"):
        assert r.status_code == 200
        authors = r.json()
        assert isinstance(authors, list)
        assert authors

@allure.title("Creating an author returns 200 and an id")
@pytest.mark.happy
def test_create_author(session, base_url):
    payload = {"idBook": 1, "firstName": "Jane", "lastName": "Doe"}
    with allure.step("POST /Authors to create an author"):
        r = session.post(f"{base_url}/Authors", json=payload)
    with allure.step("Verify creation returned 200 and author id"):
        assert r.status_code == 200
        data = r.json() or {}
        assert isinstance(data.get("id"), int)
    session.delete(f"{base_url}/Authors/{data['id']}")

@allure.title("Updating an author’s first name persists the change")
@pytest.mark.happy
def test_update_author(session, base_url):
    payload = {"idBook": 1, "firstName": "Jane", "lastName": "Doe"}
    create = session.post(f"{base_url}/Authors", json=payload)
    author_id = create.json()["id"]
    with allure.step(f"PUT /Authors/{author_id} to update firstName"):
        updated = session.put(
            f"{base_url}/Authors/{author_id}",
            json={**payload, "firstName": "John"}
        )
    with allure.step("Verify update returned 200 and new firstName"):
        assert updated.status_code == 200
        assert updated.json()["firstName"] == "John"
    session.delete(f"{base_url}/Authors/{author_id}")

@allure.title("Deleting an author returns 200")
@pytest.mark.happy
def test_delete_author(session, base_url):
    payload = {"idBook": 1, "firstName": "Jane", "lastName": "Doe"}
    create = session.post(f"{base_url}/Authors", json=payload)
    author_id = create.json()["id"]
    with allure.step(f"DELETE /Authors/{author_id}"):
        resp = session.delete(f"{base_url}/Authors/{author_id}")
    with allure.step("Verify delete returned 200"):
        assert resp.status_code == 200
