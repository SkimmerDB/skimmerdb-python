from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewKey")


@_attrs_define
class NewKey:
    """
    Attributes:
        id (int):
        name (str):
        key (str): The key itself: shown only here. Send it as Authorization: Bearer <key>.
        prefix (str):
        scope (str):
        namespaces (list[str]):
    """

    id: int
    name: str
    key: str
    prefix: str
    scope: str
    namespaces: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        key = self.key

        prefix = self.prefix

        scope = self.scope

        namespaces = self.namespaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "key": key,
                "prefix": prefix,
                "scope": scope,
                "namespaces": namespaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        key = d.pop("key")

        prefix = d.pop("prefix")

        scope = d.pop("scope")

        namespaces = cast(list[str], d.pop("namespaces"))

        new_key = cls(
            id=id,
            name=name,
            key=key,
            prefix=prefix,
            scope=scope,
            namespaces=namespaces,
        )

        new_key.additional_properties = d
        return new_key

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
