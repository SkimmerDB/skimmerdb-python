from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageDay")


@_attrs_define
class UsageDay:
    """
    Attributes:
        day (str):
        queries (int):
        writes (int):
        write_bytes (int):
        docs_written (int):
        store_gets (int):
        store_bytes (int):
        mcp_queries (int):
        mcp_writes (int):
        embed_tokens (int):
        cpu_ms (float):
        gb_months (float):
    """

    day: str
    queries: int
    writes: int
    write_bytes: int
    docs_written: int
    store_gets: int
    store_bytes: int
    mcp_queries: int
    mcp_writes: int
    embed_tokens: int
    cpu_ms: float
    gb_months: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        queries = self.queries

        writes = self.writes

        write_bytes = self.write_bytes

        docs_written = self.docs_written

        store_gets = self.store_gets

        store_bytes = self.store_bytes

        mcp_queries = self.mcp_queries

        mcp_writes = self.mcp_writes

        embed_tokens = self.embed_tokens

        cpu_ms = self.cpu_ms

        gb_months = self.gb_months

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "queries": queries,
                "writes": writes,
                "write_bytes": write_bytes,
                "docs_written": docs_written,
                "store_gets": store_gets,
                "store_bytes": store_bytes,
                "mcp_queries": mcp_queries,
                "mcp_writes": mcp_writes,
                "embed_tokens": embed_tokens,
                "cpu_ms": cpu_ms,
                "gb_months": gb_months,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day = d.pop("day")

        queries = d.pop("queries")

        writes = d.pop("writes")

        write_bytes = d.pop("write_bytes")

        docs_written = d.pop("docs_written")

        store_gets = d.pop("store_gets")

        store_bytes = d.pop("store_bytes")

        mcp_queries = d.pop("mcp_queries")

        mcp_writes = d.pop("mcp_writes")

        embed_tokens = d.pop("embed_tokens")

        cpu_ms = d.pop("cpu_ms")

        gb_months = d.pop("gb_months")

        usage_day = cls(
            day=day,
            queries=queries,
            writes=writes,
            write_bytes=write_bytes,
            docs_written=docs_written,
            store_gets=store_gets,
            store_bytes=store_bytes,
            mcp_queries=mcp_queries,
            mcp_writes=mcp_writes,
            embed_tokens=embed_tokens,
            cpu_ms=cpu_ms,
            gb_months=gb_months,
        )

        usage_day.additional_properties = d
        return usage_day

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
