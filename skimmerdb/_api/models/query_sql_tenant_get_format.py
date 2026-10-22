from typing import Literal

QuerySqlTenantGetFormat = Literal["csv", "json", "ndjson"]

QUERY_SQL_TENANT_GET_FORMAT_VALUES: set[QuerySqlTenantGetFormat] = {
    "csv",
    "json",
    "ndjson",
}


def check_query_sql_tenant_get_format(value: str) -> QuerySqlTenantGetFormat:
    if value in QUERY_SQL_TENANT_GET_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUERY_SQL_TENANT_GET_FORMAT_VALUES!r}"
    )
