from typing import Literal

SqlResultPartialsKind = Literal["auto", "named", "none"]

SQL_RESULT_PARTIALS_KIND_VALUES: set[SqlResultPartialsKind] = {
    "auto",
    "named",
    "none",
}


def check_sql_result_partials_kind(value: str) -> SqlResultPartialsKind:
    if value in SQL_RESULT_PARTIALS_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SQL_RESULT_PARTIALS_KIND_VALUES!r}"
    )
