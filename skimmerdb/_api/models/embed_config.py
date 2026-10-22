from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.embed_config_provider import (
    EmbedConfigProvider,
    check_embed_config_provider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbedConfig")


@_attrs_define
class EmbedConfig:
    """Documents written with text and no vector are embedded with this model (with the tenant's own provider key, or
    hosted); search takes semantic.

        Attributes:
            provider (EmbedConfigProvider): openai, voyage, gemini or cohere: with the tenant's own key for it (PUT
                /v1/embedding-keys/{provider}; the provider bills the tenant, SkimmerDB charges nothing). skimmerdb: hosted,
                SkimmerDB embeds with voyage-3.5-lite at Voyage's price, no margin (metered as embed_tokens; the free plan
                includes some).
            model (str | Unset): The provider's embedding model (default: text-embedding-3-small for openai, voyage-3.5-lite
                for voyage and skimmerdb, gemini-embedding-001 for gemini, embed-v4.0 for cohere). skimmerdb takes
                voyage-3.5-lite only.
            dims (int | Unset): At creation: the vectors' length to ask the model for (default: the model's own, up to
                2,048). Models that make several lengths (OpenAI's text-embedding-3, Voyage's 3.5, Gemini's, Cohere's
                embed-v4.0) take it.
    """

    provider: EmbedConfigProvider
    model: str | Unset = UNSET
    dims: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str = self.provider

        model = self.model

        dims = self.dims

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if dims is not UNSET:
            field_dict["dims"] = dims

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = check_embed_config_provider(d.pop("provider"))

        model = d.pop("model", UNSET)

        dims = d.pop("dims", UNSET)

        embed_config = cls(
            provider=provider,
            model=model,
            dims=dims,
        )

        embed_config.additional_properties = d
        return embed_config

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
