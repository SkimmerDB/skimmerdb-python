from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WriteResult")


@_attrs_define
class WriteResult:
    """
    Attributes:
        written (int):
        deleted (int):
        version (int):
        stored_bytes (int):
        took_ms (int | Unset): NDJSON streams: milliseconds.
        lines (int | Unset): NDJSON streams: lines read.
        batches (int | Unset): NDJSON streams: batches written.
        created (bool | Unset): The namespace didn't exist: this write made it (with vectors of the first vector's
            length, cosine, when the documents have vectors; else text only). Check it to catch a mistyped name.
    """

    written: int
    deleted: int
    version: int
    stored_bytes: int
    took_ms: int | Unset = UNSET
    lines: int | Unset = UNSET
    batches: int | Unset = UNSET
    created: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        written = self.written

        deleted = self.deleted

        version = self.version

        stored_bytes = self.stored_bytes

        took_ms = self.took_ms

        lines = self.lines

        batches = self.batches

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "written": written,
                "deleted": deleted,
                "version": version,
                "stored_bytes": stored_bytes,
            }
        )
        if took_ms is not UNSET:
            field_dict["took_ms"] = took_ms
        if lines is not UNSET:
            field_dict["lines"] = lines
        if batches is not UNSET:
            field_dict["batches"] = batches
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        written = d.pop("written")

        deleted = d.pop("deleted")

        version = d.pop("version")

        stored_bytes = d.pop("stored_bytes")

        took_ms = d.pop("took_ms", UNSET)

        lines = d.pop("lines", UNSET)

        batches = d.pop("batches", UNSET)

        created = d.pop("created", UNSET)

        write_result = cls(
            written=written,
            deleted=deleted,
            version=version,
            stored_bytes=stored_bytes,
            took_ms=took_ms,
            lines=lines,
            batches=batches,
            created=created,
        )

        write_result.additional_properties = d
        return write_result

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
