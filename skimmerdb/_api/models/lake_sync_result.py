from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LakeSyncResult")


@_attrs_define
class LakeSyncResult:
    """
    Attributes:
        snapshot (int): The snapshot the namespace now holds.
        previous (int): The snapshot it held before (-1: none).
        full (bool): Every live row was written (the first sync, or the table's columns, key or text changed).
        upserted (int):
        deleted (int):
        key (str): The key column (empty: row ids).
        skipped (list[str]): Columns not kept (nested types, blobs).
        took_ms (float):
        created (bool): The namespace didn't exist: this sync made it.
    """

    snapshot: int
    previous: int
    full: bool
    upserted: int
    deleted: int
    key: str
    skipped: list[str]
    took_ms: float
    created: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot = self.snapshot

        previous = self.previous

        full = self.full

        upserted = self.upserted

        deleted = self.deleted

        key = self.key

        skipped = self.skipped

        took_ms = self.took_ms

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot": snapshot,
                "previous": previous,
                "full": full,
                "upserted": upserted,
                "deleted": deleted,
                "key": key,
                "skipped": skipped,
                "took_ms": took_ms,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snapshot = d.pop("snapshot")

        previous = d.pop("previous")

        full = d.pop("full")

        upserted = d.pop("upserted")

        deleted = d.pop("deleted")

        key = d.pop("key")

        skipped = cast(list[str], d.pop("skipped"))

        took_ms = d.pop("took_ms")

        created = d.pop("created")

        lake_sync_result = cls(
            snapshot=snapshot,
            previous=previous,
            full=full,
            upserted=upserted,
            deleted=deleted,
            key=key,
            skipped=skipped,
            took_ms=took_ms,
            created=created,
        )

        lake_sync_result.additional_properties = d
        return lake_sync_result

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
