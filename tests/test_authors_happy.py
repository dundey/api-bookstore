import pytest
import allure

allure.dynamic.suite("Authors - Happy Paths")

@pytest.mark.happy
@allure.title("Listing all authors")
def test_list_all_authors(session, base_url):
    with allure.step("GET /Authors"):
        r = session.get(f"{base_url}/Authors")

    with allure.step("Verify status code is 200 and list is non-empty"):
        assert r.status_code == 200
        authors = r.json()
        assert isinstance(authors, list) and authors

@pytest.mark.happy
@allure.title("Retrieving an author by ID")
def test_get_author_by_id(session, base_url, author_keys):
    author_id = 1
    with allure.step(f"GET /Authors/{author_id}"):
        r = session.get(f"{base_url}/Authors/{author_id}")

    with allure.step("Verify status code is 200 and JSON keys"):
        assert r.status_code == 200
        data = r.json()
        assert set(data.keys()) == author_keys

@pytest.mark.happy
@allure.title("Creating an author")
def test_create_author(session, base_url, sample_author_payload):
    with allure.step("POST /Authors to create an author"):
        r = session.post(f"{base_url}/Authors", json=sample_author_payload)

    with allure.step("Verify creation returned 200 and author id"):
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data.get("id"), int)

    with allure.step("Clean up by deleting the new author"):
        session.delete(f"{base_url}/Authors/{data['id']}")

@pytest.mark.happy
@allure.title("Updating an author’s first name")
def test_update_author(session, base_url, sample_author_payload):
    with allure.step("POST /Authors to create an author"):
        create = session.post(f"{base_url}/Authors", json=sample_author_payload)
    author_id = create.json()["id"]

    with allure.step(f"PUT /Authors/{author_id} to update firstName"):
        updated = session.put(
            f"{base_url}/Authors/{author_id}",
            json={**sample_author_payload, "firstName": "John"}
        )

    with allure.step("Verify update returned 200 and new firstName"):
        assert updated.status_code == 200
        assert updated.json()["firstName"] == "John"

    with allure.step("Clean up by deleting the updated author"):
        session.delete(f"{base_url}/Authors/{author_id}")

@pytest.mark.happy
@allure.title("Deleting an author")
def test_delete_author(session, base_url, sample_author_payload):
    with allure.step("POST /Authors to create an author"):
        create = session.post(f"{base_url}/Authors", json=sample_author_payload)
    author_id = create.json()["id"]

    with allure.step(f"DELETE /Authors/{author_id}"):
        resp = session.delete(f"{base_url}/Authors/{author_id}")

    with allure.step("Verify delete returned 200"):
        assert resp.status_code == 200
