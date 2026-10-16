from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_meta import DocumentMeta


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        id (str): Any string up to 512 bytes, one line. Writing an id again replaces the document.
        text (str | Unset): Up to 2 MB. May be left out when the document has a vector.
        meta (DocumentMeta | Unset): Metadata: a JSON object of strings, numbers and booleans you can filter on (up to
            16 KB).
        vector (list[float] | Unset): An embedding: as many numbers as the namespace's dims.
        vector_b64 (str | Unset): The vector as base64 of little-endian float32s (smaller than JSON numbers).
    """

    id: str
    text: str | Unset = UNSET
    meta: DocumentMeta | Unset = UNSET
    vector: list[float] | Unset = UNSET
    vector_b64: str | Unset = UNSET
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

        vector_b64 = self.vector_b64

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
        if vector_b64 is not UNSET:
            field_dict["vector_b64"] = vector_b64

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.document_meta import DocumentMeta

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text", UNSET)

        _meta = d.pop("meta", UNSET)
        meta: DocumentMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = DocumentMeta.from_dict(_meta)

        vector = cast(list[float], d.pop("vector", UNSET))

        vector_b64 = d.pop("vector_b64", UNSET)

        document = cls(
            id=id,
            text=text,
            meta=meta,
            vector=vector,
            vector_b64=vector_b64,
        )

        document.additional_properties = d
        return document

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
