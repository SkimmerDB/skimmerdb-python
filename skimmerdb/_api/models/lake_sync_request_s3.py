from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LakeSyncRequestS3")


@_attrs_define
class LakeSyncRequestS3:
    """Keys that can read the lake's data_path (s3://...), on AWS or the endpoint given. Used for this sync only, never
    stored.

        Attributes:
            region (str):  Default: 'us-east-1'.
            access_key_id (str):
            secret_access_key (str):
            session_token (str | Unset):
            endpoint (str | Unset): An S3-compatible service instead of AWS: an https URL of scheme, host and optional port,
                no path (requests are path-style). Cloudflare R2: <account>.r2.cloudflarestorage.com with region auto; also
                MinIO, Backblaze B2, Wasabi, Google Cloud Storage's XML API. Its host must resolve to a public address. Empty:
                AWS S3 in region. Default: ''.
    """

    access_key_id: str
    secret_access_key: str
    region: str = "us-east-1"
    session_token: str | Unset = UNSET
    endpoint: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        access_key_id = self.access_key_id

        secret_access_key = self.secret_access_key

        session_token = self.session_token

        endpoint = self.endpoint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "access_key_id": access_key_id,
                "secret_access_key": secret_access_key,
            }
        )
        if session_token is not UNSET:
            field_dict["session_token"] = session_token
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        region = d.pop("region")

        access_key_id = d.pop("access_key_id")

        secret_access_key = d.pop("secret_access_key")

        session_token = d.pop("session_token", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        lake_sync_request_s3 = cls(
            region=region,
            access_key_id=access_key_id,
            secret_access_key=secret_access_key,
            session_token=session_token,
            endpoint=endpoint,
        )

        lake_sync_request_s3.additional_properties = d
        return lake_sync_request_s3

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
