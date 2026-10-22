from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_status import ExportStatus, check_export_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="Export")


@_attrs_define
class Export:
    """
    Attributes:
        id (str):
        status (ExportStatus):
        format_ (str):
        sql (str):
        rows (int): Rows written so far (all, once done).
        bytes_ (int): The file's size so far (all, once done).
        error (str): failed: why.
        created_at (str):
        finished_at (None | str):
        expires_at (str): 24 hours after it was made: the file is deleted then.
        download (str | Unset): done: where to download it.
        destination (str | Unset): Delivered to the tenant's bucket: the file's s3:// path (no download here).
    """

    id: str
    status: ExportStatus
    format_: str
    sql: str
    rows: int
    bytes_: int
    error: str
    created_at: str
    finished_at: None | str
    expires_at: str
    download: str | Unset = UNSET
    destination: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str = self.status

        format_ = self.format_

        sql = self.sql

        rows = self.rows

        bytes_ = self.bytes_

        error = self.error

        created_at = self.created_at

        finished_at: None | str
        finished_at = self.finished_at

        expires_at = self.expires_at

        download = self.download

        destination = self.destination

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "format": format_,
                "sql": sql,
                "rows": rows,
                "bytes": bytes_,
                "error": error,
                "created_at": created_at,
                "finished_at": finished_at,
                "expires_at": expires_at,
            }
        )
        if download is not UNSET:
            field_dict["download"] = download
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        status = check_export_status(d.pop("status"))

        format_ = d.pop("format")

        sql = d.pop("sql")

        rows = d.pop("rows")

        bytes_ = d.pop("bytes")

        error = d.pop("error")

        created_at = d.pop("created_at")

        def _parse_finished_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))

        expires_at = d.pop("expires_at")

        download = d.pop("download", UNSET)

        destination = d.pop("destination", UNSET)

        export = cls(
            id=id,
            status=status,
            format_=format_,
            sql=sql,
            rows=rows,
            bytes_=bytes_,
            error=error,
            created_at=created_at,
            finished_at=finished_at,
            expires_at=expires_at,
            download=download,
            destination=destination,
        )

        export.additional_properties = d
        return export

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
