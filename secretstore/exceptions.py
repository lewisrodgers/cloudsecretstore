class Error(Exception):
    pass


class InvalidInputError(Error):
    def __init__(self, err):
        self.msg = f'{err} The expected resource ID format is: "projects/PROJECT_ID/secrets/SECRET/versions/VERSION". Check for typos and verify that PROJECT_ID, SECRET, and VERSION resources exist.'
        super().__init__(self.msg)