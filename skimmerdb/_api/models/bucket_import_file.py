from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BucketImportFile")


@_attrs_define
class BucketImportFile:
    """
    Attributes:
        key (str):
        bytes_ (int):
        rows (int):
        written (int):
    """

    key: str
    bytes_: int
    rows: int
    written: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        bytes_ = self.bytes_

        rows = self.rows

        written = self.written

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "bytes": bytes_,
                "rows": rows,
                "written": written,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        bytes_ = d.pop("bytes")

        rows = d.pop("rows")

        written = d.pop("written")

        bucket_import_file = cls(
            key=key,
            bytes_=bytes_,
            rows=rows,
            written=written,
        )

        bucket_import_file.additional_properties = d
        return bucket_import_file

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
