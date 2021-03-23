import os

from .secretstore import SecretStore

__version__ = open(os.path.join(".", "VERSION")).read().strip()
