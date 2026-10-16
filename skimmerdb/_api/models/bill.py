from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Bill")


@_attrs_define
class Bill:
    """
    Attributes:
        base (float):
        storage (float):
        writes (float):
        queries (float):
        embedding (float):
        reads (float):
        usage (float):
        total (float):
    """

    base: float
    storage: float
    writes: float
    queries: float
    embedding: float
    reads: float
    usage: float
    total: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        storage = self.storage

        writes = self.writes

        queries = self.queries

        embedding = self.embedding

        reads = self.reads

        usage = self.usage

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base": base,
                "storage": storage,
                "writes": writes,
                "queries": queries,
                "embedding": embedding,
                "reads": reads,
                "usage": usage,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        base = d.pop("base")

        storage = d.pop("storage")

        writes = d.pop("writes")

        queries = d.pop("queries")

        embedding = d.pop("embedding")

        reads = d.pop("reads")

        usage = d.pop("usage")

        total = d.pop("total")

        bill = cls(
            base=base,
            storage=storage,
            writes=writes,
            queries=queries,
            embedding=embedding,
            reads=reads,
            usage=usage,
            total=total,
        )

        bill.additional_properties = d
        return bill

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
