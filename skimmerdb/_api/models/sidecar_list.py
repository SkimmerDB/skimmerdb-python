from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sidecar import Sidecar


T = TypeVar("T", bound="SidecarList")


@_attrs_define
class SidecarList:
    """
    Attributes:
        namespace (str):
        sidecars (list[Sidecar]):
    """

    namespace: str
    sidecars: list[Sidecar]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        sidecars = []
        for sidecars_item_data in self.sidecars:
            sidecars_item = sidecars_item_data.to_dict()
            sidecars.append(sidecars_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "sidecars": sidecars,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sidecar import Sidecar

        d = dict(src_dict)
        namespace = d.pop("namespace")

        sidecars = []
        _sidecars = d.pop("sidecars")
        for sidecars_item_data in _sidecars:
            sidecars_item = Sidecar.from_dict(sidecars_item_data)

            sidecars.append(sidecars_item)

        sidecar_list = cls(
            namespace=namespace,
            sidecars=sidecars,
        )

        sidecar_list.additional_properties = d
        return sidecar_list

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
