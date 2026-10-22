from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.embed_config import EmbedConfig


T = TypeVar("T", bound="NamespacePatch")


@_attrs_define
class NamespacePatch:
    """
    Attributes:
        embed (EmbedConfig | None): Set or change the embedding model (it must make vectors of the namespace's length),
            or null to stop embedding.
    """

    embed: EmbedConfig | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.embed_config import EmbedConfig

        embed: dict[str, Any] | None
        if isinstance(self.embed, EmbedConfig):
            embed = self.embed.to_dict()
        else:
            embed = self.embed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "embed": embed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed_config import EmbedConfig

        d = dict(src_dict)

        def _parse_embed(data: object) -> EmbedConfig | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                embed_type_0 = EmbedConfig.from_dict(data)

                return embed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EmbedConfig | None, data)

        embed = _parse_embed(d.pop("embed"))

        namespace_patch = cls(
            embed=embed,
        )

        namespace_patch.additional_properties = d
        return namespace_patch

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
