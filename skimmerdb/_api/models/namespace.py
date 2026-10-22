from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embed_config import EmbedConfig
    from ..models.vector_config import VectorConfig


T = TypeVar("T", bound="Namespace")


@_attrs_define
class Namespace:
    """
    Attributes:
        name (str):
        docs_written (int): Documents written to it so far (puts and deletes).
        bytes_written (int):
        stored_bytes (int): What its objects take in object storage now (metered as storage).
        created_at (str): RFC 3339, UTC.
        embed (EmbedConfig | Unset): Documents written with text and no vector are embedded with this model (with the
            tenant's own provider key, or hosted); search takes semantic.
        vector (VectorConfig | Unset):
    """

    name: str
    docs_written: int
    bytes_written: int
    stored_bytes: int
    created_at: str
    embed: EmbedConfig | Unset = UNSET
    vector: VectorConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        docs_written = self.docs_written

        bytes_written = self.bytes_written

        stored_bytes = self.stored_bytes

        created_at = self.created_at

        embed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embed, Unset):
            embed = self.embed.to_dict()

        vector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "docs_written": docs_written,
                "bytes_written": bytes_written,
                "stored_bytes": stored_bytes,
                "created_at": created_at,
            }
        )
        if embed is not UNSET:
            field_dict["embed"] = embed
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.embed_config import EmbedConfig
        from ..models.vector_config import VectorConfig

        d = dict(src_dict)
        name = d.pop("name")

        docs_written = d.pop("docs_written")

        bytes_written = d.pop("bytes_written")

        stored_bytes = d.pop("stored_bytes")

        created_at = d.pop("created_at")

        _embed = d.pop("embed", UNSET)
        embed: EmbedConfig | Unset
        if isinstance(_embed, Unset):
            embed = UNSET
        else:
            embed = EmbedConfig.from_dict(_embed)

        _vector = d.pop("vector", UNSET)
        vector: VectorConfig | Unset
        if isinstance(_vector, Unset):
            vector = UNSET
        else:
            vector = VectorConfig.from_dict(_vector)

        namespace = cls(
            name=name,
            docs_written=docs_written,
            bytes_written=bytes_written,
            stored_bytes=stored_bytes,
            created_at=created_at,
            embed=embed,
            vector=vector,
        )

        namespace.additional_properties = d
        return namespace

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
