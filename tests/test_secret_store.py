import json
import os

import pytest

from secretstore import SecretStore

# Review the README for settings these before running tests:
KEYFILE_PATH = os.getenv("KEYFILE_PATH")
CLOUD_RESOURCE = os.getenv("SECRET_RESOURCE_ID")
KEY_DATA = os.getenv("SECRET_KEY_DATA")


@pytest.fixture
def credentials():
    content = open(KEYFILE_PATH)
    return json.load(content)


@pytest.mark.webrequest
def test_should_authenticate_with_explicit_credentials(credentials):
    secrets = SecretStore(credentials)

    results = secrets.get_key_data(CLOUD_RESOURCE)

    assert results == KEY_DATA


@pytest.mark.webrequest
def test_should_authenticate_with_default_application_credentials_from_environment():
    """Review the README to set application default credentials."""
    secrets = SecretStore()

    results = secrets.get_key_data(CLOUD_RESOURCE)

    assert results == KEY_DATA
