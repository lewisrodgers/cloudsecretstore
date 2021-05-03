import os

from setuptools import setup

with open(os.path.join(".", "VERSION")) as version_file:
    version = version_file.read().strip()

setup(
    name="cloudsecretstore",
    version=version,
    description="Fetch secrets stored in Google Cloud Secret Manager.",
    author="Lewis Rodgers",
    author_email="lrodgers04@gmail.com",
    packages=["secretstore"],
    install_requires=["google-auth", "google-cloud-secret-manager"]
)
