from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hit_meta import HitMeta


T = TypeVar("T", bound="Hit")


@_attrs_define
class Hit:
    """
    Attributes:
        id (str):
        meta (HitMeta):
        written_at (datetime.datetime):
        match (str | Unset): Text search: the matched text.
        line (str | Unset): Text search: the line around the match.
        score (float | Unset): Vector search: cosine similarity (cosine namespaces) or euclidean distance.
    """

    id: str
    meta: HitMeta
    written_at: datetime.datetime
    match: str | Unset = UNSET
    line: str | Unset = UNSET
    score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        meta = self.meta.to_dict()

        written_at = self.written_at.isoformat()

        match = self.match

        line = self.line

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "meta": meta,
                "written_at": written_at,
            }
        )
        if match is not UNSET:
            field_dict["match"] = match
        if line is not UNSET:
            field_dict["line"] = line
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hit_meta import HitMeta

        d = dict(src_dict)
        id = d.pop("id")

        meta = HitMeta.from_dict(d.pop("meta"))

        written_at = datetime.datetime.fromisoformat(d.pop("written_at"))

        match = d.pop("match", UNSET)

        line = d.pop("line", UNSET)

        score = d.pop("score", UNSET)

        hit = cls(
            id=id,
            meta=meta,
            written_at=written_at,
            match=match,
            line=line,
            score=score,
        )

        hit.additional_properties = d
        return hit

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
