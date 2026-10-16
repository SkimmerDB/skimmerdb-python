from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan import Plan


T = TypeVar("T", bound="Me")


@_attrs_define
class Me:
    """
    Attributes:
        id (int):
        email (str):
        name (str):
        org_id (int):
        org_name (str):
        plan (Plan):
        tenant_id (int): The tenant this call acts for.
        scope (str): read, write or admin.
        key_id (int): The key used (0: a login).
        namespaces (list[str]):
        is_admin (bool):
    """

    id: int
    email: str
    name: str
    org_id: int
    org_name: str
    plan: Plan
    tenant_id: int
    scope: str
    key_id: int
    namespaces: list[str]
    is_admin: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        name = self.name

        org_id = self.org_id

        org_name = self.org_name

        plan = self.plan.to_dict()

        tenant_id = self.tenant_id

        scope = self.scope

        key_id = self.key_id

        namespaces = self.namespaces

        is_admin = self.is_admin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "name": name,
                "org_id": org_id,
                "org_name": org_name,
                "plan": plan,
                "tenant_id": tenant_id,
                "scope": scope,
                "key_id": key_id,
                "namespaces": namespaces,
                "is_admin": is_admin,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plan import Plan

        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        name = d.pop("name")

        org_id = d.pop("org_id")

        org_name = d.pop("org_name")

        plan = Plan.from_dict(d.pop("plan"))

        tenant_id = d.pop("tenant_id")

        scope = d.pop("scope")

        key_id = d.pop("key_id")

        namespaces = cast(list[str], d.pop("namespaces"))

        is_admin = d.pop("is_admin")

        me = cls(
            id=id,
            email=email,
            name=name,
            org_id=org_id,
            org_name=org_name,
            plan=plan,
            tenant_id=tenant_id,
            scope=scope,
            key_id=key_id,
            namespaces=namespaces,
            is_admin=is_admin,
        )

        me.additional_properties = d
        return me

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
