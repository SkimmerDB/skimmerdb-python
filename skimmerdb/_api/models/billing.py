from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.plan import Plan
    from ..models.usage import Usage


T = TypeVar("T", bound="Billing")


@_attrs_define
class Billing:
    """
    Attributes:
        plan (Plan):
        stripe (bool):
        customer (bool):
        subscribed (bool):
        usage (Usage):
    """

    plan: Plan
    stripe: bool
    customer: bool
    subscribed: bool
    usage: Usage
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan = self.plan.to_dict()

        stripe = self.stripe

        customer = self.customer

        subscribed = self.subscribed

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "plan": plan,
                "stripe": stripe,
                "customer": customer,
                "subscribed": subscribed,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plan import Plan
        from ..models.usage import Usage

        d = dict(src_dict)
        plan = Plan.from_dict(d.pop("plan"))

        stripe = d.pop("stripe")

        customer = d.pop("customer")

        subscribed = d.pop("subscribed")

        usage = Usage.from_dict(d.pop("usage"))

        billing = cls(
            plan=plan,
            stripe=stripe,
            customer=customer,
            subscribed=subscribed,
            usage=usage,
        )

        billing.additional_properties = d
        return billing

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
