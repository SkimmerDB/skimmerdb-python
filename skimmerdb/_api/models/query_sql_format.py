from typing import Literal

QuerySqlFormat = Literal["csv", "json", "ndjson"]

QUERY_SQL_FORMAT_VALUES: set[QuerySqlFormat] = {
    "csv",
    "json",
    "ndjson",
}


def check_query_sql_format(value: str) -> QuerySqlFormat:
    if value in QUERY_SQL_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUERY_SQL_FORMAT_VALUES!r}"
    )
