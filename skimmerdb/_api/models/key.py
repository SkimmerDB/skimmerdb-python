from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Key")


@_attrs_define
class Key:
    """
    Attributes:
        id (int):
        name (str):
        prefix (str):
        connected_app (bool): Made by an OAuth approval (an MCP client).
        scope (str):
        namespaces (list[str]):
        rate_per_s (int):
        cap_queries (int):
        cap_writes (int):
        created_at (str):
        last_used_at (str):
    """

    id: int
    name: str
    prefix: str
    connected_app: bool
    scope: str
    namespaces: list[str]
    rate_per_s: int
    cap_queries: int
    cap_writes: int
    created_at: str
    last_used_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        prefix = self.prefix

        connected_app = self.connected_app

        scope = self.scope

        namespaces = self.namespaces

        rate_per_s = self.rate_per_s

        cap_queries = self.cap_queries

        cap_writes = self.cap_writes

        created_at = self.created_at

        last_used_at = self.last_used_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "prefix": prefix,
                "connected_app": connected_app,
                "scope": scope,
                "namespaces": namespaces,
                "rate_per_s": rate_per_s,
                "cap_queries": cap_queries,
                "cap_writes": cap_writes,
                "created_at": created_at,
                "last_used_at": last_used_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        prefix = d.pop("prefix")

        connected_app = d.pop("connected_app")

        scope = d.pop("scope")

        namespaces = cast(list[str], d.pop("namespaces"))

        rate_per_s = d.pop("rate_per_s")

        cap_queries = d.pop("cap_queries")

        cap_writes = d.pop("cap_writes")

        created_at = d.pop("created_at")

        last_used_at = d.pop("last_used_at")

        key = cls(
            id=id,
            name=name,
            prefix=prefix,
            connected_app=connected_app,
            scope=scope,
            namespaces=namespaces,
            rate_per_s=rate_per_s,
            cap_queries=cap_queries,
            cap_writes=cap_writes,
            created_at=created_at,
            last_used_at=last_used_at,
        )

        key.additional_properties = d
        return key

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
