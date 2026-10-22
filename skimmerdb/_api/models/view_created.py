from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ViewCreated")


@_attrs_define
class ViewCreated:
    """
    Attributes:
        name (str):
        namespace (str):
        sql (str):
        created_at (str):
        columns (list[str]):
        types (list[str]):
    """

    name: str
    namespace: str
    sql: str
    created_at: str
    columns: list[str]
    types: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace = self.namespace

        sql = self.sql

        created_at = self.created_at

        columns = self.columns

        types = self.types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "namespace": namespace,
                "sql": sql,
                "created_at": created_at,
                "columns": columns,
                "types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        namespace = d.pop("namespace")

        sql = d.pop("sql")

        created_at = d.pop("created_at")

        columns = cast(list[str], d.pop("columns"))

        types = cast(list[str], d.pop("types"))

        view_created = cls(
            name=name,
            namespace=namespace,
            sql=sql,
            created_at=created_at,
            columns=columns,
            types=types,
        )

        view_created.additional_properties = d
        return view_created

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
