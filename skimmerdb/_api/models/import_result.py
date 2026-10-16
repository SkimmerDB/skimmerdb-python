from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ImportResult")


@_attrs_define
class ImportResult:
    """
    Attributes:
        written (int):
        deleted (int):
        version (int):
        stored_bytes (int):
        rows (int):
        took_ms (float):
        created (bool): The namespace didn't exist: this import made it (text only).
    """

    written: int
    deleted: int
    version: int
    stored_bytes: int
    rows: int
    took_ms: float
    created: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        written = self.written

        deleted = self.deleted

        version = self.version

        stored_bytes = self.stored_bytes

        rows = self.rows

        took_ms = self.took_ms

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "written": written,
                "deleted": deleted,
                "version": version,
                "stored_bytes": stored_bytes,
                "rows": rows,
                "took_ms": took_ms,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        written = d.pop("written")

        deleted = d.pop("deleted")

        version = d.pop("version")

        stored_bytes = d.pop("stored_bytes")

        rows = d.pop("rows")

        took_ms = d.pop("took_ms")

        created = d.pop("created")

        import_result = cls(
            written=written,
            deleted=deleted,
            version=version,
            stored_bytes=stored_bytes,
            rows=rows,
            took_ms=took_ms,
            created=created,
        )

        import_result.additional_properties = d
        return import_result

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
