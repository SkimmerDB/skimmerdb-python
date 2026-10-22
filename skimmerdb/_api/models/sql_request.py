from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sql_request_format import SqlRequestFormat, check_sql_request_format
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlRequest")


@_attrs_define
class SqlRequest:
    """
    Attributes:
        sql (str): One query (SELECT, WITH, UNION ...) whose tables are namespaces (docs: the one in the path), SHOW
            COLUMNS, or a write (write scope): INSERT INTO ns [(columns)] VALUES (...) | SELECT ..., CREATE TABLE ns AS
            SELECT ..., DELETE FROM ns [WHERE ...].
        format_ (SqlRequestFormat | Unset): json: the answer below (at most 10,000 rows). ndjson or csv: the rows
            streamed as they're made, with no row cap (as ?format= or an Accept header). Default: 'json'.
    """

    sql: str
    format_: SqlRequestFormat | Unset = "json"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sql = self.sql

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sql": sql,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sql = d.pop("sql")

        _format_ = d.pop("format", UNSET)
        format_: SqlRequestFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_sql_request_format(_format_)

        sql_request = cls(
            sql=sql,
            format_=format_,
        )

        sql_request.additional_properties = d
        return sql_request

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
