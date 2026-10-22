from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sql_write_statement import SqlWriteStatement, check_sql_write_statement

T = TypeVar("T", bound="SqlWrite")


@_attrs_define
class SqlWrite:
    """What a SQL write did (INSERT, CREATE TABLE, DELETE).

    Attributes:
        statement (SqlWriteStatement):
        namespace (str): The namespace written.
        inserted (int): Documents written (an id that existed is replaced).
        deleted (int):
        version (int): The namespace's version with the write.
        created (bool): The statement made the namespace.
    """

    statement: SqlWriteStatement
    namespace: str
    inserted: int
    deleted: int
    version: int
    created: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statement: str = self.statement

        namespace = self.namespace

        inserted = self.inserted

        deleted = self.deleted

        version = self.version

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "statement": statement,
                "namespace": namespace,
                "inserted": inserted,
                "deleted": deleted,
                "version": version,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        statement = check_sql_write_statement(d.pop("statement"))

        namespace = d.pop("namespace")

        inserted = d.pop("inserted")

        deleted = d.pop("deleted")

        version = d.pop("version")

        created = d.pop("created")

        sql_write = cls(
            statement=statement,
            namespace=namespace,
            inserted=inserted,
            deleted=deleted,
            version=version,
            created=created,
        )

        sql_write.additional_properties = d
        return sql_write

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
