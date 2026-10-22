from typing import Literal

SqlRequestFormat = Literal["csv", "json", "ndjson"]

SQL_REQUEST_FORMAT_VALUES: set[SqlRequestFormat] = {
    "csv",
    "json",
    "ndjson",
}


def check_sql_request_format(value: str) -> SqlRequestFormat:
    if value in SQL_REQUEST_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SQL_REQUEST_FORMAT_VALUES!r}"
    )
