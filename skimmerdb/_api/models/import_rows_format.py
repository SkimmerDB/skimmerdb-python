from typing import Literal

ImportRowsFormat = Literal["csv", "ndjson", "parquet"]

IMPORT_ROWS_FORMAT_VALUES: set[ImportRowsFormat] = {
    "csv",
    "ndjson",
    "parquet",
}


def check_import_rows_format(value: str) -> ImportRowsFormat:
    if value in IMPORT_ROWS_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IMPORT_ROWS_FORMAT_VALUES!r}"
    )
