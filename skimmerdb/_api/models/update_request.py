from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_patch import DocumentPatch


T = TypeVar("T", bound="UpdateRequest")


@_attrs_define
class UpdateRequest:
    """
    Attributes:
        docs (list[DocumentPatch]):
        wait (bool | Unset):  Default: False.
    """

    docs: list[DocumentPatch]
    wait: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        docs = []
        for docs_item_data in self.docs:
            docs_item = docs_item_data.to_dict()
            docs.append(docs_item)

        wait = self.wait

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "docs": docs,
            }
        )
        if wait is not UNSET:
            field_dict["wait"] = wait

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.document_patch import DocumentPatch

        d = dict(src_dict)
        docs = []
        _docs = d.pop("docs")
        for docs_item_data in _docs:
            docs_item = DocumentPatch.from_dict(docs_item_data)

            docs.append(docs_item)

        wait = d.pop("wait", UNSET)

        update_request = cls(
            docs=docs,
            wait=wait,
        )

        update_request.additional_properties = d
        return update_request

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
