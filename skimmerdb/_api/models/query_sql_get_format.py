from typing import Literal

QuerySqlGetFormat = Literal["csv", "json", "ndjson"]

QUERY_SQL_GET_FORMAT_VALUES: set[QuerySqlGetFormat] = {
    "csv",
    "json",
    "ndjson",
}


def check_query_sql_get_format(value: str) -> QuerySqlGetFormat:
    if value in QUERY_SQL_GET_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUERY_SQL_GET_FORMAT_VALUES!r}"
    )
