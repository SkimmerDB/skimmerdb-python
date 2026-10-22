from typing import Literal

SqlWriteStatement = Literal["create", "delete", "insert"]

SQL_WRITE_STATEMENT_VALUES: set[SqlWriteStatement] = {
    "create",
    "delete",
    "insert",
}


def check_sql_write_statement(value: str) -> SqlWriteStatement:
    if value in SQL_WRITE_STATEMENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SQL_WRITE_STATEMENT_VALUES!r}"
    )
