from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.s3_keys import S3Keys


T = TypeVar("T", bound="ExportDestination")


@_attrs_define
class ExportDestination:
    """Deliver the file to the tenant's own bucket (AWS S3, R2, B2, MinIO, ...) by multipart upload instead of keeping it
    here. The keys are checked at once (a small object is written and deleted) and kept in memory only while the export
    runs.

        Attributes:
            path (str): s3://bucket/key for the file; ending in / a name is made (export-<time>.<format>).
            s3 (S3Keys): Keys for the tenant's own bucket, on AWS S3 or an S3-compatible service. Used while the request (or
                export) runs, never stored. Without access_key_id and secret_access_key, requests go unsigned: a public bucket
                (such as AWS Open Data), for reading only.
    """

    path: str
    s3: S3Keys
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        s3 = self.s3.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "s3": s3,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.s3_keys import S3Keys

        d = dict(src_dict)
        path = d.pop("path")

        s3 = S3Keys.from_dict(d.pop("s3"))

        export_destination = cls(
            path=path,
            s3=s3,
        )

        export_destination.additional_properties = d
        return export_destination

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
