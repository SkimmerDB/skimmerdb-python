from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lake_sync_request_s3 import LakeSyncRequestS3


T = TypeVar("T", bound="LakeSyncRequest")


@_attrs_define
class LakeSyncRequest:
    """A DuckLake table to keep in the namespace.

    Attributes:
        catalog (str): The lake's catalog: a postgres:// URL (DuckLake's Postgres catalog), reachable at a public
            address. Used for this sync only, never stored.
        table (str): The table: name (schema main) or schema.name.
        s3 (LakeSyncRequestS3): Keys that can read the lake's data_path (s3://...), on AWS or the endpoint given. Used
            for this sync only, never stored.
        key (str | Unset): The column whose value is a document's id. Default: id when the table has one, else the
            DuckLake row id; rowid: the row id. Default: ''.
        text (list[str] | Unset): Columns whose values are the searchable text (default: every text column).
        snapshot (int | Unset): The snapshot to sync to (-1: the latest). Never older than the one synced. Default: -1.
    """

    catalog: str
    table: str
    s3: LakeSyncRequestS3
    key: str | Unset = ""
    text: list[str] | Unset = UNSET
    snapshot: int | Unset = -1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog = self.catalog

        table = self.table

        s3 = self.s3.to_dict()

        key = self.key

        text: list[str] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text

        snapshot = self.snapshot

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog": catalog,
                "table": table,
                "s3": s3,
            }
        )
        if key is not UNSET:
            field_dict["key"] = key
        if text is not UNSET:
            field_dict["text"] = text
        if snapshot is not UNSET:
            field_dict["snapshot"] = snapshot

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lake_sync_request_s3 import LakeSyncRequestS3

        d = dict(src_dict)
        catalog = d.pop("catalog")

        table = d.pop("table")

        s3 = LakeSyncRequestS3.from_dict(d.pop("s3"))

        key = d.pop("key", UNSET)

        text = cast(list[str], d.pop("text", UNSET))

        snapshot = d.pop("snapshot", UNSET)

        lake_sync_request = cls(
            catalog=catalog,
            table=table,
            s3=s3,
            key=key,
            text=text,
            snapshot=snapshot,
        )

        lake_sync_request.additional_properties = d
        return lake_sync_request

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
