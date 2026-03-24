import pytest
import time
from jsonschema import validate

from schema_config import POST_SCHEMA, COMMENT_SCHEMA, USER_SCHEMA


@pytest.mark.parametrize("endpoint", ["/posts", "/comments", "/users"])
def test_response_time(get_response, endpoint):
    start = time.time()
    response = get_response(endpoint)
    end = time.time()

    assert response.status_code == 200
    assert (end - start) < 2


# ---------------------------
# Test 2: Schema Validation
# ---------------------------

@pytest.mark.parametrize(
    "endpoint,schema",
    [
        ("/posts", POST_SCHEMA),
        ("/comments", COMMENT_SCHEMA),
        ("/users", USER_SCHEMA),
    ],
)
def test_schema_validation(get_response, endpoint, schema):
    response = get_response(endpoint)

    assert response.status_code == 200

    for item in response.json():
        validate(instance=item, schema=schema)