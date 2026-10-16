from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.key_request_scope import KeyRequestScope, check_key_request_scope
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyRequest")


@_attrs_define
class KeyRequest:
    """
    Attributes:
        name (str | Unset): A label (default: default).
        scope (KeyRequestScope | Unset): read: list namespaces, search, count, get documents, warm, SQL, usage. write:
            also create and delete namespaces, write, update, delete and import documents. admin: also make, list, change
            and revoke keys, and billing. Only an admin key without namespace limits or caps (or the owner's login) can
            manage keys, so a read or write key can't make more. Default: 'write'.
        namespaces (list[str] | Unset): The namespaces the key may use: names or prefix* (default: all).
        rate_per_s (int | Unset): Requests a second (0: no cap of its own).
        cap_queries (int | Unset): Queries a billing period (0: none).
        cap_writes (int | Unset): Documents written or deleted a billing period (0: none).
    """

    name: str | Unset = UNSET
    scope: KeyRequestScope | Unset = "write"
    namespaces: list[str] | Unset = UNSET
    rate_per_s: int | Unset = UNSET
    cap_queries: int | Unset = UNSET
    cap_writes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        namespaces: list[str] | Unset = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        rate_per_s = self.rate_per_s

        cap_queries = self.cap_queries

        cap_writes = self.cap_writes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces
        if rate_per_s is not UNSET:
            field_dict["rate_per_s"] = rate_per_s
        if cap_queries is not UNSET:
            field_dict["cap_queries"] = cap_queries
        if cap_writes is not UNSET:
            field_dict["cap_writes"] = cap_writes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: KeyRequestScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_key_request_scope(_scope)

        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        rate_per_s = d.pop("rate_per_s", UNSET)

        cap_queries = d.pop("cap_queries", UNSET)

        cap_writes = d.pop("cap_writes", UNSET)

        key_request = cls(
            name=name,
            scope=scope,
            namespaces=namespaces,
            rate_per_s=rate_per_s,
            cap_queries=cap_queries,
            cap_writes=cap_writes,
        )

        key_request.additional_properties = d
        return key_request

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
