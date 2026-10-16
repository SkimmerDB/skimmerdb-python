from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_fields import ErrorFields


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """Every error answer, whatever the status.

    Attributes:
        error (str): What went wrong, in a sentence.
        code (str): A word to act on. By status: bad_request (400), unauthorized (401), payment_required (402),
            forbidden (403), not_found (404), conflict (409), too_large (413), invalid (422; fields says which),
            rate_limited (429), internal (500), not_implemented (501), bad_gateway (502), unavailable (503), quota_full
            (507). More precise ones: namespace_limit (402: the plan's namespace count), query_timeout (422: past the plan's
            time limit), scan_refused (422: a regex the index can't narrow on a big namespace; send scan: true), write_busy
            (429: writes arrive faster than the namespace commits them; nothing was written), write_unknown (503: the write
            may or may not have been applied; retrying is safe).
        fields (ErrorFields | Unset): invalid: field -> what's wrong with it.
        retry_after (int | Unset): write_busy: seconds to wait (as Retry-After).
    """

    error: str
    code: str
    fields: ErrorFields | Unset = UNSET
    retry_after: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        code = self.code

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        retry_after = self.retry_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "code": code,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if retry_after is not UNSET:
            field_dict["retry_after"] = retry_after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.error_fields import ErrorFields

        d = dict(src_dict)
        error = d.pop("error")

        code = d.pop("code")

        _fields = d.pop("fields", UNSET)
        fields: ErrorFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = ErrorFields.from_dict(_fields)

        retry_after = d.pop("retry_after", UNSET)

        error = cls(
            error=error,
            code=code,
            fields=fields,
            retry_after=retry_after,
        )

        error.additional_properties = d
        return error

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
