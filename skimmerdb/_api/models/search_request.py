from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """Text search, or with vector (or vector_b64) a vector search: the nearest documents among those passing filter and q.

    Attributes:
        q (str | Unset): Plain text, matched literally and ignoring case; with regex an RE2 pattern. Empty: list
            documents, newest first. With a vector: only documents containing it (hybrid). Default: ''.
        regex (bool | Unset):  Default: False.
        filter_ (Filter | Unset): Every key must hold. {"status": "open"} equal; {"status": ["open", "pending"]} or
            {"status": {"in": [...]}} one of; {"priority": {"gte": 2, "lt": 5}} a numeric range (gt, gte, lt, lte); {"team":
            {"ne": "api"}} not equal (a missing key counts as not equal). Numbers compare as numbers.
        limit (int | Unset): Hits a page (20; vector search 10).
        cursor (str | Unset): The next of the previous page.
        scan (bool | Unset): Allow a regex the index can't narrow to scan a big namespace (otherwise 422 scan_refused).
            Default: False.
        vector (list[float] | Unset): An embedding: as many numbers as the namespace's dims.
        vector_b64 (str | Unset): The vector as base64 of little-endian float32s (smaller than JSON numbers).
        nprobe (int | Unset): Vector search: clusters probed in the biggest index (48).
        rerank (int | Unset): Vector search: candidates reranked (64).
        full (bool | Unset): Vector search: rerank with the float32 vectors as written. Default: False.
    """

    q: str | Unset = ""
    regex: bool | Unset = False
    filter_: Filter | Unset = UNSET
    limit: int | Unset = UNSET
    cursor: str | Unset = UNSET
    scan: bool | Unset = False
    vector: list[float] | Unset = UNSET
    vector_b64: str | Unset = UNSET
    nprobe: int | Unset = UNSET
    rerank: int | Unset = UNSET
    full: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        regex = self.regex

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        limit = self.limit

        cursor = self.cursor

        scan = self.scan

        vector: list[float] | Unset = UNSET
        if not isinstance(self.vector, Unset):
            vector = self.vector

        vector_b64 = self.vector_b64

        nprobe = self.nprobe

        rerank = self.rerank

        full = self.full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if q is not UNSET:
            field_dict["q"] = q
        if regex is not UNSET:
            field_dict["regex"] = regex
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if limit is not UNSET:
            field_dict["limit"] = limit
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if scan is not UNSET:
            field_dict["scan"] = scan
        if vector is not UNSET:
            field_dict["vector"] = vector
        if vector_b64 is not UNSET:
            field_dict["vector_b64"] = vector_b64
        if nprobe is not UNSET:
            field_dict["nprobe"] = nprobe
        if rerank is not UNSET:
            field_dict["rerank"] = rerank
        if full is not UNSET:
            field_dict["full"] = full

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_ import Filter

        d = dict(src_dict)
        q = d.pop("q", UNSET)

        regex = d.pop("regex", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Filter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        limit = d.pop("limit", UNSET)

        cursor = d.pop("cursor", UNSET)

        scan = d.pop("scan", UNSET)

        vector = cast(list[float], d.pop("vector", UNSET))

        vector_b64 = d.pop("vector_b64", UNSET)

        nprobe = d.pop("nprobe", UNSET)

        rerank = d.pop("rerank", UNSET)

        full = d.pop("full", UNSET)

        search_request = cls(
            q=q,
            regex=regex,
            filter_=filter_,
            limit=limit,
            cursor=cursor,
            scan=scan,
            vector=vector,
            vector_b64=vector_b64,
            nprobe=nprobe,
            rerank=rerank,
            full=full,
        )

        search_request.additional_properties = d
        return search_request

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
