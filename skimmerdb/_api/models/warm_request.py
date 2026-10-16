from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WarmRequest")


@_attrs_define
class WarmRequest:
    """
    Attributes:
        queries (list[str] | Unset): Searches about to be made: their document lists are fetched now.
        regex (bool | Unset):  Default: False.
    """

    queries: list[str] | Unset = UNSET
    regex: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queries: list[str] | Unset = UNSET
        if not isinstance(self.queries, Unset):
            queries = self.queries

        regex = self.regex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if queries is not UNSET:
            field_dict["queries"] = queries
        if regex is not UNSET:
            field_dict["regex"] = regex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        queries = cast(list[str], d.pop("queries", UNSET))

        regex = d.pop("regex", UNSET)

        warm_request = cls(
            queries=queries,
            regex=regex,
        )

        warm_request.additional_properties = d
        return warm_request

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
