from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyLimits")


@_attrs_define
class KeyLimits:
    """
    Attributes:
        namespaces (list[str] | Unset):
        rate_per_s (int | Unset):
        cap_queries (int | Unset):
        cap_writes (int | Unset):
    """

    namespaces: list[str] | Unset = UNSET
    rate_per_s: int | Unset = UNSET
    cap_queries: int | Unset = UNSET
    cap_writes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespaces: list[str] | Unset = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        rate_per_s = self.rate_per_s

        cap_queries = self.cap_queries

        cap_writes = self.cap_writes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        rate_per_s = d.pop("rate_per_s", UNSET)

        cap_queries = d.pop("cap_queries", UNSET)

        cap_writes = d.pop("cap_writes", UNSET)

        key_limits = cls(
            namespaces=namespaces,
            rate_per_s=rate_per_s,
            cap_queries=cap_queries,
            cap_writes=cap_writes,
        )

        key_limits.additional_properties = d
        return key_limits

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
