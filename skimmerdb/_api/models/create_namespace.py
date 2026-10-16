from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vector_config import VectorConfig


T = TypeVar("T", bound="CreateNamespace")


@_attrs_define
class CreateNamespace:
    """
    Attributes:
        name (str): 1 to 64 of a-z, 0-9, '-', '_' and '.'.
        vector (VectorConfig | Unset):
    """

    name: str
    vector: VectorConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        vector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vector_config import VectorConfig

        d = dict(src_dict)
        name = d.pop("name")

        _vector = d.pop("vector", UNSET)
        vector: VectorConfig | Unset
        if isinstance(_vector, Unset):
            vector = UNSET
        else:
            vector = VectorConfig.from_dict(_vector)

        create_namespace = cls(
            name=name,
            vector=vector,
        )

        create_namespace.additional_properties = d
        return create_namespace

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
