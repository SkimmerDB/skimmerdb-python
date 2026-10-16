from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_rpc_response_error import JsonRpcResponseError
    from ..models.json_rpc_response_result import JsonRpcResponseResult


T = TypeVar("T", bound="JsonRpcResponse")


@_attrs_define
class JsonRpcResponse:
    """
    Attributes:
        jsonrpc (str):
        id (int | None | str):
        result (JsonRpcResponseResult | Unset):
        error (JsonRpcResponseError | Unset):
    """

    jsonrpc: str
    id: int | None | str
    result: JsonRpcResponseResult | Unset = UNSET
    error: JsonRpcResponseError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jsonrpc = self.jsonrpc

        id: int | None | str
        id = self.id

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonrpc": jsonrpc,
                "id": id,
            }
        )
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.json_rpc_response_error import JsonRpcResponseError
        from ..models.json_rpc_response_result import JsonRpcResponseResult

        d = dict(src_dict)
        jsonrpc = d.pop("jsonrpc")

        def _parse_id(data: object) -> int | None | str:
            if data is None:
                return data
            return cast(int | None | str, data)

        id = _parse_id(d.pop("id"))

        _result = d.pop("result", UNSET)
        result: JsonRpcResponseResult | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = JsonRpcResponseResult.from_dict(_result)

        _error = d.pop("error", UNSET)
        error: JsonRpcResponseError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = JsonRpcResponseError.from_dict(_error)

        json_rpc_response = cls(
            jsonrpc=jsonrpc,
            id=id,
            result=result,
            error=error,
        )

        json_rpc_response.additional_properties = d
        return json_rpc_response

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
