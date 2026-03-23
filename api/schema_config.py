import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMAS_DIR = os.path.join(BASE_DIR, "api", "schemas")


def _load_schema(file_name):
    path = os.path.join(SCHEMAS_DIR, file_name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


POST_SCHEMA = _load_schema("post.json")
COMMENT_SCHEMA = _load_schema("comments.json")
USER_SCHEMA = _load_schema("users.json")
