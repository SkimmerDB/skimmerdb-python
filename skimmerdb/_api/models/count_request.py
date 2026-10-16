from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_ import Filter


T = TypeVar("T", bound="CountRequest")


@_attrs_define
class CountRequest:
    """
    Attributes:
        q (str | Unset):  Default: ''.
        regex (bool | Unset):  Default: False.
        filter_ (Filter | Unset): Every key must hold. {"status": "open"} equal; {"status": ["open", "pending"]} or
            {"status": {"in": [...]}} one of; {"priority": {"gte": 2, "lt": 5}} a numeric range (gt, gte, lt, lte); {"team":
            {"ne": "api"}} not equal (a missing key counts as not equal). Numbers compare as numbers.
        exact (bool | Unset): false: estimate from a sample of the candidates (fast on big namespaces; no filters).
            Default: True.
        sample (int | Unset): Estimates: candidates checked (2,000).
        scan (bool | Unset): Allow a regex the index can't narrow to scan a big namespace (otherwise 422 scan_refused).
            Default: False.
    """

    q: str | Unset = ""
    regex: bool | Unset = False
    filter_: Filter | Unset = UNSET
    exact: bool | Unset = True
    sample: int | Unset = UNSET
    scan: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        regex = self.regex

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        exact = self.exact

        sample = self.sample

        scan = self.scan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if q is not UNSET:
            field_dict["q"] = q
        if regex is not UNSET:
            field_dict["regex"] = regex
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if exact is not UNSET:
            field_dict["exact"] = exact
        if sample is not UNSET:
            field_dict["sample"] = sample
        if scan is not UNSET:
            field_dict["scan"] = scan

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

        exact = d.pop("exact", UNSET)

        sample = d.pop("sample", UNSET)

        scan = d.pop("scan", UNSET)

        count_request = cls(
            q=q,
            regex=regex,
            filter_=filter_,
            exact=exact,
            sample=sample,
            scan=scan,
        )

        count_request.additional_properties = d
        return count_request

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
