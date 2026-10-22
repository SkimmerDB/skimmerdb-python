from typing import Literal

ExportStatus = Literal["done", "expired", "failed", "queued", "running"]

EXPORT_STATUS_VALUES: set[ExportStatus] = {
    "done",
    "expired",
    "failed",
    "queued",
    "running",
}


def check_export_status(value: str) -> ExportStatus:
    if value in EXPORT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXPORT_STATUS_VALUES!r}"
    )
