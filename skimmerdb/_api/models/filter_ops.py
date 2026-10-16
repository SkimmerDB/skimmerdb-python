from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterOps")


@_attrs_define
class FilterOps:
    """
    Attributes:
        eq (bool | float | str | Unset):
        ne (bool | float | str | Unset):
        in_ (list[bool | float | str] | Unset):
        gt (float | Unset):
        gte (float | Unset):
        lt (float | Unset):
        lte (float | Unset):
    """

    eq: bool | float | str | Unset = UNSET
    ne: bool | float | str | Unset = UNSET
    in_: list[bool | float | str] | Unset = UNSET
    gt: float | Unset = UNSET
    gte: float | Unset = UNSET
    lt: float | Unset = UNSET
    lte: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        eq: bool | float | str | Unset
        if isinstance(self.eq, Unset):
            eq = UNSET
        else:
            eq = self.eq

        ne: bool | float | str | Unset
        if isinstance(self.ne, Unset):
            ne = UNSET
        else:
            ne = self.ne

        in_: list[bool | float | str] | Unset = UNSET
        if not isinstance(self.in_, Unset):
            in_ = []
            for in_item_data in self.in_:
                in_item: bool | float | str
                in_item = in_item_data
                in_.append(in_item)

        gt = self.gt

        gte = self.gte

        lt = self.lt

        lte = self.lte

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if eq is not UNSET:
            field_dict["eq"] = eq
        if ne is not UNSET:
            field_dict["ne"] = ne
        if in_ is not UNSET:
            field_dict["in"] = in_
        if gt is not UNSET:
            field_dict["gt"] = gt
        if gte is not UNSET:
            field_dict["gte"] = gte
        if lt is not UNSET:
            field_dict["lt"] = lt
        if lte is not UNSET:
            field_dict["lte"] = lte

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_eq(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        eq = _parse_eq(d.pop("eq", UNSET))

        def _parse_ne(data: object) -> bool | float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(bool | float | str | Unset, data)

        ne = _parse_ne(d.pop("ne", UNSET))

        _in_ = d.pop("in", UNSET)
        in_: list[bool | float | str] | Unset = UNSET
        if _in_ is not UNSET:
            in_ = []
            for in_item_data in _in_:

                def _parse_in_item(data: object) -> bool | float | str:
                    return cast(bool | float | str, data)

                in_item = _parse_in_item(in_item_data)

                in_.append(in_item)

        gt = d.pop("gt", UNSET)

        gte = d.pop("gte", UNSET)

        lt = d.pop("lt", UNSET)

        lte = d.pop("lte", UNSET)

        filter_ops = cls(
            eq=eq,
            ne=ne,
            in_=in_,
            gt=gt,
            gte=gte,
            lt=lt,
            lte=lte,
        )

        return filter_ops
