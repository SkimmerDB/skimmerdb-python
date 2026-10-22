from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_request_format import (
    ExportRequestFormat,
    check_export_request_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_destination import ExportDestination


T = TypeVar("T", bound="ExportRequest")


@_attrs_define
class ExportRequest:
    """
    Attributes:
        sql (str): A query (as POST /v1/sql: tables are the tenant's namespaces by name).
        format_ (ExportRequestFormat | Unset): CSV (a header line, RFC 4180), NDJSON (an object a row) or Parquet (one
            file: row groups of up to 131,072 rows, ZSTD; every column nullable; int as INT64, float DOUBLE, text STRING,
            date DATE, time TIMESTAMP (microseconds, not UTC-adjusted), decimal DECIMAL(18, s)). Default: 'csv'.
        destination (ExportDestination | Unset): Deliver the file to the tenant's own bucket (AWS S3, R2, B2, MinIO,
            ...) by multipart upload instead of keeping it here. The keys are checked at once (a small object is written and
            deleted) and kept in memory only while the export runs.
    """

    sql: str
    format_: ExportRequestFormat | Unset = "csv"
    destination: ExportDestination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sql = self.sql

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql": sql,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.export_destination import ExportDestination

        d = dict(src_dict)
        sql = d.pop("sql")

        _format_ = d.pop("format", UNSET)
        format_: ExportRequestFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_export_request_format(_format_)

        _destination = d.pop("destination", UNSET)
        destination: ExportDestination | Unset
        if isinstance(_destination, Unset):
            destination = UNSET
        else:
            destination = ExportDestination.from_dict(_destination)

        export_request = cls(
            sql=sql,
            format_=format_,
            destination=destination,
        )

        export_request.additional_properties = d
        return export_request

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
