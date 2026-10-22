from typing import Literal

QuerySqlTenantFormat = Literal["csv", "json", "ndjson"]

QUERY_SQL_TENANT_FORMAT_VALUES: set[QuerySqlTenantFormat] = {
    "csv",
    "json",
    "ndjson",
}


def check_query_sql_tenant_format(value: str) -> QuerySqlTenantFormat:
    if value in QUERY_SQL_TENANT_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {QUERY_SQL_TENANT_FORMAT_VALUES!r}"
    )
