from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bucket_import_request_format import (
    BucketImportRequestFormat,
    check_bucket_import_request_format,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.s3_keys import S3Keys


T = TypeVar("T", bound="BucketImportRequest")


@_attrs_define
class BucketImportRequest:
    """Files in the tenant's bucket to import.

    Attributes:
        path (str): s3://bucket/key (one file), s3://bucket/prefix/ (every file under it) or
            s3://bucket/prefix/*.parquet (those ending as the pattern after the *).
        s3 (S3Keys): Keys for the tenant's own bucket, on AWS S3 or an S3-compatible service. Used while the request (or
            export) runs, never stored. Without access_key_id and secret_access_key, requests go unsigned: a public bucket
            (such as AWS Open Data), for reading only.
        format_ (BucketImportRequestFormat | Unset): Empty: from each file's extension (.csv, .ndjson / .jsonl / .json,
            .parquet). Default: ''.
        id (str | Unset): The column holding document ids (default: row numbers).
        text (list[str] | Unset): Columns to index as text.
        schema (str | Unset): CSV: a CREATE TABLE giving the columns' types.
        after (str | Unset): Only keys after this one (a previous answer's next). Default: ''.
    """

    path: str
    s3: S3Keys
    format_: BucketImportRequestFormat | Unset = ""
    id: str | Unset = UNSET
    text: list[str] | Unset = UNSET
    schema: str | Unset = UNSET
    after: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        s3 = self.s3.to_dict()

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        id = self.id

        text: list[str] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text

        schema = self.schema

        after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "s3": s3,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if schema is not UNSET:
            field_dict["schema"] = schema
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.s3_keys import S3Keys

        d = dict(src_dict)
        path = d.pop("path")

        s3 = S3Keys.from_dict(d.pop("s3"))

        _format_ = d.pop("format", UNSET)
        format_: BucketImportRequestFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_bucket_import_request_format(_format_)

        id = d.pop("id", UNSET)

        text = cast(list[str], d.pop("text", UNSET))

        schema = d.pop("schema", UNSET)

        after = d.pop("after", UNSET)

        bucket_import_request = cls(
            path=path,
            s3=s3,
            format_=format_,
            id=id,
            text=text,
            schema=schema,
            after=after,
        )

        bucket_import_request.additional_properties = d
        return bucket_import_request

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
