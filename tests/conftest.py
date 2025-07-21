import os
import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default=os.getenv("API_BASE_URL", "https://fakerestapi.azurewebsites.net/api/v1"),
        help="Base URL for the API under test"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base-url")

@pytest.fixture
def session():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s

@pytest.fixture(scope="session")
def book_keys():
    return {"id", "title", "description", "pageCount", "excerpt", "publishDate"}

@pytest.fixture(scope="session")
def author_keys():
    return {"id", "idBook", "firstName", "lastName"}

@pytest.fixture
def sample_book_payload():
    return {
        "title": "X",
        "description": "Y",
        "pageCount": 10,
        "excerpt": "",
        "publishDate": "2025-07-20T00:00:00Z"
    }

@pytest.fixture
def sample_author_payload():
    return {"idBook": 1, "firstName": "Jane", "lastName": "Doe"}
