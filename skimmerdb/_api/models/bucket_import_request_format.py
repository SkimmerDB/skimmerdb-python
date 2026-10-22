from typing import Literal

BucketImportRequestFormat = Literal["", "csv", "ndjson", "parquet"]

BUCKET_IMPORT_REQUEST_FORMAT_VALUES: set[BucketImportRequestFormat] = {
    "",
    "csv",
    "ndjson",
    "parquet",
}


def check_bucket_import_request_format(value: str) -> BucketImportRequestFormat:
    if value in BUCKET_IMPORT_REQUEST_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BUCKET_IMPORT_REQUEST_FORMAT_VALUES!r}"
    )
