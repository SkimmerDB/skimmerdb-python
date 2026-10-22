from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sql_result_partials_kind import (
    SqlResultPartialsKind,
    check_sql_result_partials_kind,
)

T = TypeVar("T", bound="SqlResultPartials")


@_attrs_define
class SqlResultPartials:
    """Present when the query ran from per-segment partials (one namespace and aggregates that merge from parts, or a
    view): which view's partials answered it and how many segments' partials were computed for it or reused. Always
    exact.

        Attributes:
            view (None | str): The named view read (several: comma-separated), or null.
            kind (SqlResultPartialsKind): named: a view's kept partials; auto: an automatic view's (a query shape repeated
                on a big namespace); none: partials kept in memory only.
            computed (int): Segments whose partials were computed for this query.
            reused (int): Segments whose partials were reused (unchanged since computed).
            remote (int): Of those computed, how many on other servers of the cluster.
    """

    view: None | str
    kind: SqlResultPartialsKind
    computed: int
    reused: int
    remote: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        view: None | str
        view = self.view

        kind: str = self.kind

        computed = self.computed

        reused = self.reused

        remote = self.remote

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "view": view,
                "kind": kind,
                "computed": computed,
                "reused": reused,
                "remote": remote,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_view(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        view = _parse_view(d.pop("view"))

        kind = check_sql_result_partials_kind(d.pop("kind"))

        computed = d.pop("computed")

        reused = d.pop("reused")

        remote = d.pop("remote")

        sql_result_partials = cls(
            view=view,
            kind=kind,
            computed=computed,
            reused=reused,
            remote=remote,
        )

        sql_result_partials.additional_properties = d
        return sql_result_partials

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
