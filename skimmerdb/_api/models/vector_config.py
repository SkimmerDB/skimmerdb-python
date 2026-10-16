from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vector_config_metric import VectorConfigMetric, check_vector_config_metric
from ..types import UNSET, Unset

T = TypeVar("T", bound="VectorConfig")


@_attrs_define
class VectorConfig:
    """
    Attributes:
        dims (int): Your embeddings' length.
        metric (VectorConfigMetric | Unset):  Default: 'cosine'.
    """

    dims: int
    metric: VectorConfigMetric | Unset = "cosine"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dims = self.dims

        metric: str | Unset = UNSET
        if not isinstance(self.metric, Unset):
            metric = self.metric

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dims": dims,
            }
        )
        if metric is not UNSET:
            field_dict["metric"] = metric

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dims = d.pop("dims")

        _metric = d.pop("metric", UNSET)
        metric: VectorConfigMetric | Unset
        if isinstance(_metric, Unset):
            metric = UNSET
        else:
            metric = check_vector_config_metric(_metric)

        vector_config = cls(
            dims=dims,
            metric=metric,
        )

        vector_config.additional_properties = d
        return vector_config

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
