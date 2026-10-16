from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.namespace import Namespace


T = TypeVar("T", bound="NamespaceList")


@_attrs_define
class NamespaceList:
    """
    Attributes:
        namespaces (list[Namespace]):
        next_ (str): Pass as after for the next page (empty: no more).
    """

    namespaces: list[Namespace]
    next_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespaces = []
        for namespaces_item_data in self.namespaces:
            namespaces_item = namespaces_item_data.to_dict()
            namespaces.append(namespaces_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespaces": namespaces,
                "next": next_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.namespace import Namespace

        d = dict(src_dict)
        namespaces = []
        _namespaces = d.pop("namespaces")
        for namespaces_item_data in _namespaces:
            namespaces_item = Namespace.from_dict(namespaces_item_data)

            namespaces.append(namespaces_item)

        next_ = d.pop("next")

        namespace_list = cls(
            namespaces=namespaces,
            next_=next_,
        )

        namespace_list.additional_properties = d
        return namespace_list

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
