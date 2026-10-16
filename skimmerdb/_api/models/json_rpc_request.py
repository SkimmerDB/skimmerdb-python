from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    Self,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_rpc_request_params import JsonRpcRequestParams


T = TypeVar("T", bound="JsonRpcRequest")


@_attrs_define
class JsonRpcRequest:
    """
    Attributes:
        jsonrpc (Literal['2.0']):
        method (str): initialize, ping, tools/list or tools/call.
        id (int | str | Unset):
        params (JsonRpcRequestParams | Unset):
    """

    jsonrpc: Literal["2.0"]
    method: str
    id: int | str | Unset = UNSET
    params: JsonRpcRequestParams | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        jsonrpc = self.jsonrpc

        method = self.method

        id: int | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "jsonrpc": jsonrpc,
                "method": method,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.json_rpc_request_params import JsonRpcRequestParams

        d = dict(src_dict)
        jsonrpc = cast(Literal["2.0"], d.pop("jsonrpc"))
        if jsonrpc != "2.0":
            raise ValueError(f"jsonrpc must match const '2.0', got '{jsonrpc}'")

        method = d.pop("method")

        def _parse_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _params = d.pop("params", UNSET)
        params: JsonRpcRequestParams | Unset
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = JsonRpcRequestParams.from_dict(_params)

        json_rpc_request = cls(
            jsonrpc=jsonrpc,
            method=method,
            id=id,
            params=params,
        )

        json_rpc_request.additional_properties = d
        return json_rpc_request

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
