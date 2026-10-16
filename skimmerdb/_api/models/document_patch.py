from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_patch_meta import DocumentPatchMeta


T = TypeVar("T", bound="DocumentPatch")


@_attrs_define
class DocumentPatch:
    """
    Attributes:
        id (str):
        text (str | Unset): Replaces the text (kept when left out).
        meta (DocumentPatchMeta | Unset): Merged key by key; a null value removes the key.
        vector (list[float] | Unset): An embedding: as many numbers as the namespace's dims.
    """

    id: str
    text: str | Unset = UNSET
    meta: DocumentPatchMeta | Unset = UNSET
    vector: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        vector: list[float] | Unset = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if meta is not UNSET:
            field_dict["meta"] = meta
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.document_patch_meta import DocumentPatchMeta

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: DocumentPatchMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentPatchMeta.from_dict(_meta)

        vector = cast(list[float], d.pop("vector", UNSET))

        document_patch = cls(
            id=id,
            text=text,
            meta=meta,
            vector=vector,
        )

        document_patch.additional_properties = d
        return document_patch

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
