from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.filter_ops import FilterOps


T = TypeVar("T", bound="Filter")


@_attrs_define
class Filter:
    """Every key must hold. {"status": "open"} equal; {"status": ["open", "pending"]} or {"status": {"in": [...]}} one of;
    {"priority": {"gte": 2, "lt": 5}} a numeric range (gt, gte, lt, lte); {"team": {"ne": "api"}} not equal (a missing
    key counts as not equal). Numbers compare as numbers.

    """

    additional_properties: dict[
        str, bool | FilterOps | float | list[bool | float | str] | str
    ] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_ops import FilterOps

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, list):
                field_dict[prop_name] = []
                for additional_property_type_3_item_data in prop:
                    additional_property_type_3_item: bool | float | str
                    additional_property_type_3_item = (
                        additional_property_type_3_item_data
                    )
                    field_dict[prop_name].append(additional_property_type_3_item)

            elif isinstance(prop, FilterOps):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_ops import FilterOps

        d = dict(src_dict)
        filter_ = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> bool | FilterOps | float | list[bool | float | str] | str:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    additional_property_type_3 = []
                    _additional_property_type_3 = data
                    for (
                        additional_property_type_3_item_data
                    ) in _additional_property_type_3:

                        def _parse_additional_property_type_3_item(
                            data: object,
                        ) -> bool | float | str:
                            return cast(bool | float | str, data)

                        additional_property_type_3_item = (
                            _parse_additional_property_type_3_item(
                                additional_property_type_3_item_data
                            )
                        )

                        additional_property_type_3.append(
                            additional_property_type_3_item
                        )

                    return additional_property_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_4 = FilterOps.from_dict(data)

                    return additional_property_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(
                    bool | FilterOps | float | list[bool | float | str] | str, data
                )

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        filter_.additional_properties = additional_properties
        return filter_

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> bool | FilterOps | float | list[bool | float | str] | str:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: bool | FilterOps | float | list[bool | float | str] | str
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
