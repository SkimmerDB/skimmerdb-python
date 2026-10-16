from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CountResult")


@_attrs_define
class CountResult:
    """
    Attributes:
        namespace (str):
        count (int):
        exact (bool): false: count is an estimate (lo..hi is its 95% interval).
        sample (list[str]): Some matching ids.
        docs (int):
        took_ms (float):
        partial (bool):
        temperature (str): How warm the namespace was: warm (open), local (opened from the server's disk) or cold
            (opened from object storage).
        store_gets (int):
        store_bytes (int):
        lo (int):
        hi (int):
        candidates (int):
        cpu_ms (float):
    """

    namespace: str
    count: int
    exact: bool
    sample: list[str]
    docs: int
    took_ms: float
    partial: bool
    temperature: str
    store_gets: int
    store_bytes: int
    lo: int
    hi: int
    candidates: int
    cpu_ms: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        count = self.count

        exact = self.exact

        sample = self.sample

        docs = self.docs

        took_ms = self.took_ms

        partial = self.partial

        temperature = self.temperature

        store_gets = self.store_gets

        store_bytes = self.store_bytes

        lo = self.lo

        hi = self.hi

        candidates = self.candidates

        cpu_ms = self.cpu_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "count": count,
                "exact": exact,
                "sample": sample,
                "docs": docs,
                "took_ms": took_ms,
                "partial": partial,
                "temperature": temperature,
                "store_gets": store_gets,
                "store_bytes": store_bytes,
                "lo": lo,
                "hi": hi,
                "candidates": candidates,
                "cpu_ms": cpu_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        namespace = d.pop("namespace")

        count = d.pop("count")

        exact = d.pop("exact")

        sample = cast(list[str], d.pop("sample"))

        docs = d.pop("docs")

        took_ms = d.pop("took_ms")

        partial = d.pop("partial")

        temperature = d.pop("temperature")

        store_gets = d.pop("store_gets")

        store_bytes = d.pop("store_bytes")

        lo = d.pop("lo")

        hi = d.pop("hi")

        candidates = d.pop("candidates")

        cpu_ms = d.pop("cpu_ms")

        count_result = cls(
            namespace=namespace,
            count=count,
            exact=exact,
            sample=sample,
            docs=docs,
            took_ms=took_ms,
            partial=partial,
            temperature=temperature,
            store_gets=store_gets,
            store_bytes=store_bytes,
            lo=lo,
            hi=hi,
            candidates=candidates,
            cpu_ms=cpu_ms,
        )

        count_result.additional_properties = d
        return count_result

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
