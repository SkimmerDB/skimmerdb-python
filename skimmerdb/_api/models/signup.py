from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Signup")


@_attrs_define
class Signup:
    """
    Attributes:
        id (int): Your user id.
        tenant_id (int): Your first tenant (it owns namespaces, keys and usage).
        key (str): Your first API key, full access (scope admin): shown only here. Send it as Authorization: Bearer
            <key>. Make narrower keys for apps and agents with POST /v1/keys.
        key_id (int):
        key_prefix (str): The key's first characters, as key listings show it.
        scope (str): admin.
    """

    id: int
    tenant_id: int
    key: str
    key_id: int
    key_prefix: str
    scope: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tenant_id = self.tenant_id

        key = self.key

        key_id = self.key_id

        key_prefix = self.key_prefix

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "tenant_id": tenant_id,
                "key": key,
                "key_id": key_id,
                "key_prefix": key_prefix,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        tenant_id = d.pop("tenant_id")

        key = d.pop("key")

        key_id = d.pop("key_id")

        key_prefix = d.pop("key_prefix")

        scope = d.pop("scope")

        signup = cls(
            id=id,
            tenant_id=tenant_id,
            key=key,
            key_id=key_id,
            key_prefix=key_prefix,
            scope=scope,
        )

        signup.additional_properties = d
        return signup

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
