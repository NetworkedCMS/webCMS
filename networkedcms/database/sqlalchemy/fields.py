from sqlalchemy import String, Boolean, Integer, Text, DateTime
from typing import Any
from sqlalchemy_utils.types import ScalarListType


class StringField(String):
    """Stores an object of string (VARCHAR) to database"""

    def __init__(self, length: Any | None = ..., collation: Any | None = ...,
                 convert_unicode: bool = ..., unicode_error: Any | None = ..., _warn_on_bytestring: bool = ..., _expect_unicode: bool = ...) -> None:
        super(StringField, self).__init__(length, collation, convert_unicode, unicode_error,
                                          _warn_on_bytestring, _expect_unicode)


class IntegerField(Integer):
    """Creates an sql object of integer type"""
    pass


class BooleanField(Boolean):
    """Creates an SQL object of boolean type"""

    def __init__(self, create_constraint: bool = ..., name: Any | None = ..., _create_events: bool = ...) -> None:
        super(BooleanField, self).__init__(
            create_constraint, name, _create_events)


class TextField(Text):
    """Creates an SQL object of (VARCHAR) with more content length"""

    def __init__(self, length: Any | None = ..., collation: Any | None = ..., convert_unicode: bool = ..., unicode_error: Any | None = ..., _warn_on_bytestring: bool = ..., _expect_unicode: bool = ...) -> None:
        super(TextField, self).__init__(length, collation, convert_unicode,
                                        unicode_error, _warn_on_bytestring, _expect_unicode)


class ListField(ScalarListType):
    """Stores a pythonic list object in database """

    def __init__(self, coerce_func=..., separator=','):
        super(ListField, self).__init__(coerce_func, separator)


class DateTimeField(DateTime):
    """Maps a datetime object to SQL"""

    def __init__(self, timezone: bool = ...) -> None:
        super(DateTimeField, self).__init__(timezone)