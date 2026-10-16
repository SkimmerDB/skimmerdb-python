from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hit import Hit


T = TypeVar("T", bound="SearchResult")


@_attrs_define
class SearchResult:
    """
    Attributes:
        namespace (str):
        hits (list[Hit]): Newest first (text) or nearest first (vector).
        docs (int): Documents in the namespace.
        took_ms (float):
        partial (bool): Object storage failed for some reads: hits may be missing.
        temperature (str): How warm the namespace was: warm (open), local (opened from the server's disk) or cold
            (opened from object storage).
        store_gets (int): Object-storage reads this query made (0 when warm).
        store_bytes (int): Bytes those reads fetched.
        cpu_ms (float): CPU the query used (metered, not billed).
        timed_out (bool): The query ran past the plan's time limit (query_seconds): the answer is partial.
        next_ (str | Unset): Text search: pass as cursor for the next page (empty: no more).
        scanned (int | Unset): Vector search: candidates estimated.
        reranked (int | Unset): Vector search: candidates reranked.
    """

    namespace: str
    hits: list[Hit]
    docs: int
    took_ms: float
    partial: bool
    temperature: str
    store_gets: int
    store_bytes: int
    cpu_ms: float
    timed_out: bool
    next_: str | Unset = UNSET
    scanned: int | Unset = UNSET
    reranked: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        hits = []
        for hits_item_data in self.hits:
            hits_item = hits_item_data.to_dict()
            hits.append(hits_item)

        docs = self.docs

        took_ms = self.took_ms

        partial = self.partial

        temperature = self.temperature

        store_gets = self.store_gets

        store_bytes = self.store_bytes

        cpu_ms = self.cpu_ms

        timed_out = self.timed_out

        next_ = self.next_

        scanned = self.scanned

        reranked = self.reranked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "hits": hits,
                "docs": docs,
                "took_ms": took_ms,
                "partial": partial,
                "temperature": temperature,
                "store_gets": store_gets,
                "store_bytes": store_bytes,
                "cpu_ms": cpu_ms,
                "timed_out": timed_out,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if scanned is not UNSET:
            field_dict["scanned"] = scanned
        if reranked is not UNSET:
            field_dict["reranked"] = reranked

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hit import Hit

        d = dict(src_dict)
        namespace = d.pop("namespace")

        hits = []
        _hits = d.pop("hits")
        for hits_item_data in _hits:
            hits_item = Hit.from_dict(hits_item_data)

            hits.append(hits_item)

        docs = d.pop("docs")

        took_ms = d.pop("took_ms")

        partial = d.pop("partial")

        temperature = d.pop("temperature")

        store_gets = d.pop("store_gets")

        store_bytes = d.pop("store_bytes")

        cpu_ms = d.pop("cpu_ms")

        timed_out = d.pop("timed_out")

        next_ = d.pop("next", UNSET)

        scanned = d.pop("scanned", UNSET)

        reranked = d.pop("reranked", UNSET)

        search_result = cls(
            namespace=namespace,
            hits=hits,
            docs=docs,
            took_ms=took_ms,
            partial=partial,
            temperature=temperature,
            store_gets=store_gets,
            store_bytes=store_bytes,
            cpu_ms=cpu_ms,
            timed_out=timed_out,
            next_=next_,
            scanned=scanned,
            reranked=reranked,
        )

        search_result.additional_properties = d
        return search_result

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
