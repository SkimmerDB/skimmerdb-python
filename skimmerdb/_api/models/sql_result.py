from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sql_result_partials import SqlResultPartials
    from ..models.sql_write import SqlWrite


T = TypeVar("T", bound="SqlResult")


@_attrs_define
class SqlResult:
    """
    Attributes:
        namespace (str): The namespace in the path ("" for /v1/sql).
        columns (list[str]):
        types (list[str]): int, float, text, date, time, decimal (its values as strings, exact) or null (every value
            NULL), one a column.
        rows (list[list[float | None | str]]):
        chunks (int): Column blocks in the namespaces read.
        scanned (int): Column blocks read.
        partial (bool): Reserved for response compatibility; incomplete SQL text reads fail with 503.
        truncated (bool): More than 10,000 rows: these are the first.
        took_ms (float):
        temperature (str): How warm the namespace was: warm (open), local (opened from the server's disk) or cold
            (opened from object storage).
        store_gets (int): Object-storage reads this query made (0 when warm).
        store_bytes (int): Bytes those reads fetched.
        cpu_ms (float): CPU the query used (metered, not billed).
        timed_out (bool): The query ran past the plan's time limit (query_seconds): the answer is partial.
        dml (SqlWrite | Unset): What a SQL write did (INSERT, CREATE TABLE, DELETE).
        partials (SqlResultPartials | Unset): Present when the query ran from per-segment partials (one namespace and
            aggregates that merge from parts, or a view): which view's partials answered it and how many segments' partials
            were computed for it or reused. Always exact.
    """

    namespace: str
    columns: list[str]
    types: list[str]
    rows: list[list[float | None | str]]
    chunks: int
    scanned: int
    partial: bool
    truncated: bool
    took_ms: float
    temperature: str
    store_gets: int
    store_bytes: int
    cpu_ms: float
    timed_out: bool
    dml: SqlWrite | Unset = UNSET
    partials: SqlResultPartials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        columns = self.columns

        types = self.types

        rows = []
        for rows_item_data in self.rows:
            rows_item = []
            for rows_item_item_data in rows_item_data:
                rows_item_item: float | None | str
                rows_item_item = rows_item_item_data
                rows_item.append(rows_item_item)

            rows.append(rows_item)

        chunks = self.chunks

        scanned = self.scanned

        partial = self.partial

        truncated = self.truncated

        took_ms = self.took_ms

        temperature = self.temperature

        store_gets = self.store_gets

        store_bytes = self.store_bytes

        cpu_ms = self.cpu_ms

        timed_out = self.timed_out

        dml: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dml, Unset):
            dml = self.dml.to_dict()

        partials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partials, Unset):
            partials = self.partials.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "columns": columns,
                "types": types,
                "rows": rows,
                "chunks": chunks,
                "scanned": scanned,
                "partial": partial,
                "truncated": truncated,
                "took_ms": took_ms,
                "temperature": temperature,
                "store_gets": store_gets,
                "store_bytes": store_bytes,
                "cpu_ms": cpu_ms,
                "timed_out": timed_out,
            }
        )
        if dml is not UNSET:
            field_dict["dml"] = dml
        if partials is not UNSET:
            field_dict["partials"] = partials

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sql_result_partials import SqlResultPartials
        from ..models.sql_write import SqlWrite

        d = dict(src_dict)
        namespace = d.pop("namespace")

        columns = cast(list[str], d.pop("columns"))

        types = cast(list[str], d.pop("types"))

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = []
            _rows_item = rows_item_data
            for rows_item_item_data in _rows_item:

                def _parse_rows_item_item(data: object) -> float | None | str:
                    if data is None:
                        return data
                    return cast(float | None | str, data)

                rows_item_item = _parse_rows_item_item(rows_item_item_data)

                rows_item.append(rows_item_item)

            rows.append(rows_item)

        chunks = d.pop("chunks")

        scanned = d.pop("scanned")

        partial = d.pop("partial")

        truncated = d.pop("truncated")

        took_ms = d.pop("took_ms")

        temperature = d.pop("temperature")

        store_gets = d.pop("store_gets")

        store_bytes = d.pop("store_bytes")

        cpu_ms = d.pop("cpu_ms")

        timed_out = d.pop("timed_out")

        _dml = d.pop("dml", UNSET)
        dml: SqlWrite | Unset
        if isinstance(_dml, Unset):
            dml = UNSET
        else:
            dml = SqlWrite.from_dict(_dml)

        _partials = d.pop("partials", UNSET)
        partials: SqlResultPartials | Unset
        if isinstance(_partials, Unset):
            partials = UNSET
        else:
            partials = SqlResultPartials.from_dict(_partials)

        sql_result = cls(
            namespace=namespace,
            columns=columns,
            types=types,
            rows=rows,
            chunks=chunks,
            scanned=scanned,
            partial=partial,
            truncated=truncated,
            took_ms=took_ms,
            temperature=temperature,
            store_gets=store_gets,
            store_bytes=store_bytes,
            cpu_ms=cpu_ms,
            timed_out=timed_out,
            dml=dml,
            partials=partials,
        )

        sql_result.additional_properties = d
        return sql_result

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
