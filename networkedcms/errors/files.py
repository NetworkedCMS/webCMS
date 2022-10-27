
class ServerHTTPException(Exception):
    """Raises a 500 (internal server error flag)"""
    def __init__(self, error: str = None):
        super(ServerHTTPException, self).__init__(status_code=500, detail=error)


class InvalidResource(ServerHTTPException):
    """
    raise when has invalid resource
    """


class NoSuchFieldFound(ServerHTTPException):
    """
    raise when no such field for the given
    """


class FileMaxSizeLimit(ServerHTTPException):
    """
    raise when the upload file exceeds the max size
    """


class FileExtNotAllowed(ServerHTTPException):
    """
    raise when the upload file ext not allowed
    """