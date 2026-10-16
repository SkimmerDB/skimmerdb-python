from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="WriteRequest")


@_attrs_define
class WriteRequest:
    """1 to 10,000 documents and deletes a request, 64 MB at most.

    Attributes:
        docs (list[Document] | Unset): Documents to put (insert or replace).
        deletes (list[str] | Unset): Ids to delete.
        wait (bool | Unset): Answer only once the write is searchable on this server (it is durable either way).
            Default: False.
    """

    docs: list[Document] | Unset = UNSET
    deletes: list[str] | Unset = UNSET
    wait: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        docs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.docs, Unset):
            docs = []
            for docs_item_data in self.docs:
                docs_item = docs_item_data.to_dict()
                docs.append(docs_item)

        deletes: list[str] | Unset = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        wait = self.wait

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docs is not UNSET:
            field_dict["docs"] = docs
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if wait is not UNSET:
            field_dict["wait"] = wait

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.document import Document

        d = dict(src_dict)
        _docs = d.pop("docs", UNSET)
        docs: list[Document] | Unset = UNSET
        if _docs is not UNSET:
            docs = []
            for docs_item_data in _docs:
                docs_item = Document.from_dict(docs_item_data)

                docs.append(docs_item)

        deletes = cast(list[str], d.pop("deletes", UNSET))

        wait = d.pop("wait", UNSET)

        write_request = cls(
            docs=docs,
            deletes=deletes,
            wait=wait,
        )

        write_request.additional_properties = d
        return write_request

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
