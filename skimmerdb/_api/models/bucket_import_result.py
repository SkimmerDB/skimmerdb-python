from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bucket_import_file import BucketImportFile


T = TypeVar("T", bound="BucketImportResult")


@_attrs_define
class BucketImportResult:
    """
    Attributes:
        files (list[BucketImportFile]): The files imported, in order (each committed on its own).
        written (int):
        rows (int):
        bytes_ (int):
        next_ (str): More files remain: pass this as after. Empty: done.
        took_ms (float):
        created (bool): The namespace didn't exist: this import made it (text only).
    """

    files: list[BucketImportFile]
    written: int
    rows: int
    bytes_: int
    next_: str
    took_ms: float
    created: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)

        written = self.written

        rows = self.rows

        bytes_ = self.bytes_

        next_ = self.next_

        took_ms = self.took_ms

        created = self.created

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "files": files,
                "written": written,
                "rows": rows,
                "bytes": bytes_,
                "next": next_,
                "took_ms": took_ms,
                "created": created,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bucket_import_file import BucketImportFile

        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in _files:
            files_item = BucketImportFile.from_dict(files_item_data)

            files.append(files_item)

        written = d.pop("written")

        rows = d.pop("rows")

        bytes_ = d.pop("bytes")

        next_ = d.pop("next")

        took_ms = d.pop("took_ms")

        created = d.pop("created")

        bucket_import_result = cls(
            files=files,
            written=written,
            rows=rows,
            bytes_=bytes_,
            next_=next_,
            took_ms=took_ms,
            created=created,
        )

        bucket_import_result.additional_properties = d
        return bucket_import_result

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
