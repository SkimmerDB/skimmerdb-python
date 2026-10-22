from typing import Literal

ExportRequestFormat = Literal["csv", "ndjson", "parquet"]

EXPORT_REQUEST_FORMAT_VALUES: set[ExportRequestFormat] = {
    "csv",
    "ndjson",
    "parquet",
}


def check_export_request_format(value: str) -> ExportRequestFormat:
    if value in EXPORT_REQUEST_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_REQUEST_FORMAT_VALUES!r}"
    )
