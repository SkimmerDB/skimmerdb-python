from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stored_document_meta import StoredDocumentMeta


T = TypeVar("T", bound="StoredDocument")


@_attrs_define
class StoredDocument:
    """
    Attributes:
        id (str):
        text (str):
        meta (StoredDocumentMeta):
        written_at (datetime.datetime):
        temperature (str): How warm the namespace was: warm (open), local (opened from the server's disk) or cold
            (opened from object storage).
        store_gets (int): Object-storage reads this query made (0 when warm).
        store_bytes (int): Bytes those reads fetched.
        cpu_ms (float): CPU the query used (metered, not billed).
        timed_out (bool): The query ran past the plan's time limit (query_seconds): the answer is partial.
        vector (list[float] | Unset):
    """

    id: str
    text: str
    meta: StoredDocumentMeta
    written_at: datetime.datetime
    temperature: str
    store_gets: int
    store_bytes: int
    cpu_ms: float
    timed_out: bool
    vector: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        meta = self.meta.to_dict()

        written_at = self.written_at.isoformat()

        temperature = self.temperature

        store_gets = self.store_gets

        store_bytes = self.store_bytes

        cpu_ms = self.cpu_ms

        timed_out = self.timed_out

        vector: list[float] | Unset = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "meta": meta,
                "written_at": written_at,
                "temperature": temperature,
                "store_gets": store_gets,
                "store_bytes": store_bytes,
                "cpu_ms": cpu_ms,
                "timed_out": timed_out,
            }
        )
        if vector is not UNSET:
            field_dict["vector"] = vector

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stored_document_meta import StoredDocumentMeta

        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        meta = StoredDocumentMeta.from_dict(d.pop("meta"))

        written_at = datetime.datetime.fromisoformat(d.pop("written_at"))

        temperature = d.pop("temperature")

        store_gets = d.pop("store_gets")

        store_bytes = d.pop("store_bytes")

        cpu_ms = d.pop("cpu_ms")

        timed_out = d.pop("timed_out")

        vector = cast(list[float], d.pop("vector", UNSET))

        stored_document = cls(
            id=id,
            text=text,
            meta=meta,
            written_at=written_at,
            temperature=temperature,
            store_gets=store_gets,
            store_bytes=store_bytes,
            cpu_ms=cpu_ms,
            timed_out=timed_out,
            vector=vector,
        )

        stored_document.additional_properties = d
        return stored_document

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
