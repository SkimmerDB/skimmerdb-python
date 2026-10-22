from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmbeddingKey")


@_attrs_define
class EmbeddingKey:
    """
    Attributes:
        provider (str): openai or voyage.
        hint (str): The key's first and last characters: the key itself is never shown again.
        created_at (str):
        updated_at (str):
    """

    provider: str
    hint: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        hint = self.hint

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "hint": hint,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider = d.pop("provider")

        hint = d.pop("hint")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        embedding_key = cls(
            provider=provider,
            hint=hint,
            created_at=created_at,
            updated_at=updated_at,
        )

        embedding_key.additional_properties = d
        return embedding_key

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
