import json
import os

import pytest

from secretstore import SecretStore
from secretstore.exceptions import InvalidInputError

# Review `docs/tests` on setting these environment variables before running tests:
PROJECT_ID = os.getenv("PROJECT_ID")
SECRET_NAME = os.getenv("SECRET_NAME")
SECRET_VERSION = os.getenv("SECRET_VERSION")
KEY_DATA = os.getenv("KEY_DATA")
KEYFILE_PATH = os.getenv("KEYFILE_PATH")

RESOURCE_ID = f"projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/{SECRET_VERSION}"


@pytest.fixture
def keyfile():
    content = open(KEYFILE_PATH)
    return json.load(content)


@pytest.mark.webrequest
def test_should_authenticate_with_explicit_credentials(keyfile):
    secret = SecretStore(credentials=keyfile)

    secret.resource_id(RESOURCE_ID).fetch()

    assert secret.key_data == KEY_DATA


@pytest.mark.webrequest
def test_should_authenticate_with_default_application_credentials_from_environment():
    """Review the README to set application default credentials."""
    secret = SecretStore()

    secret.resource_id(RESOURCE_ID).fetch()

    assert secret.key_data == KEY_DATA


@pytest.mark.webrequest
@pytest.mark.parametrize("input, status_code, kind, message", [
    ("BAD_INPUT", "403", "project", "Permission denied"),
    (f"projects/{PROJECT_ID}/BAD/INPUT", "400", "Resource ID", "not in a valid format"),
    (f"projects/{PROJECT_ID}/secrets/BAD_INPUT/versions/{SECRET_VERSION}", "404", "secret", "not found"),
    (f"projects/{PROJECT_ID}/secrets/{SECRET_NAME}/versions/100000000000", "404", "version", "not found")
])
def test_should_raise_InvalidInputError(input, status_code, kind, message):
    secrets = SecretStore()

    with pytest.raises(InvalidInputError) as exc_info:
        secrets.resource_id(input).fetch()

    assert status_code in str(exc_info.value)
    assert kind in str(exc_info.value)
    assert message in str(exc_info.value)
