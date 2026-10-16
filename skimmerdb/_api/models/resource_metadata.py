from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResourceMetadata")


@_attrs_define
class ResourceMetadata:
    """
    Attributes:
        resource (str):
        authorization_servers (list[str]):
        scopes_supported (list[str]):
        bearer_methods_supported (list[str]):
        resource_name (str):
        resource_documentation (str):
    """

    resource: str
    authorization_servers: list[str]
    scopes_supported: list[str]
    bearer_methods_supported: list[str]
    resource_name: str
    resource_documentation: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        authorization_servers = self.authorization_servers

        scopes_supported = self.scopes_supported

        bearer_methods_supported = self.bearer_methods_supported

        resource_name = self.resource_name

        resource_documentation = self.resource_documentation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "authorization_servers": authorization_servers,
                "scopes_supported": scopes_supported,
                "bearer_methods_supported": bearer_methods_supported,
                "resource_name": resource_name,
                "resource_documentation": resource_documentation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        resource = d.pop("resource")

        authorization_servers = cast(list[str], d.pop("authorization_servers"))

        scopes_supported = cast(list[str], d.pop("scopes_supported"))

        bearer_methods_supported = cast(list[str], d.pop("bearer_methods_supported"))

        resource_name = d.pop("resource_name")

        resource_documentation = d.pop("resource_documentation")

        resource_metadata = cls(
            resource=resource,
            authorization_servers=authorization_servers,
            scopes_supported=scopes_supported,
            bearer_methods_supported=bearer_methods_supported,
            resource_name=resource_name,
            resource_documentation=resource_documentation,
        )

        resource_metadata.additional_properties = d
        return resource_metadata

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
