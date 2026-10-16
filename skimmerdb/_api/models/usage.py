from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bill import Bill
    from ..models.plan import Plan
    from ..models.usage_day import UsageDay


T = TypeVar("T", bound="Usage")


@_attrs_define
class Usage:
    """
    Attributes:
        period_start (str): This billing period's first day (UTC).
        month (str):
        queries (int): Searches, counts, reads, warms and SQL queries (metered).
        writes (int): Documents written or deleted.
        write_bytes (int):
        docs_written (int):
        store_gets (int): Object-storage reads made by queries (cold queries cost more).
        store_bytes (int):
        mcp_queries (int):
        mcp_writes (int):
        embed_tokens (int):
        cpu_ms (float):
        stored_bytes (int):
        gb_months (float): Storage so far this period.
        plan (Plan):
        bill (Bill):
        days (list[UsageDay] | Unset):
    """

    period_start: str
    month: str
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
    stored_bytes: int
    gb_months: float
    plan: Plan
    bill: Bill
    days: list[UsageDay] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_start = self.period_start

        month = self.month

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

        stored_bytes = self.stored_bytes

        gb_months = self.gb_months

        plan = self.plan.to_dict()

        bill = self.bill.to_dict()

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period_start": period_start,
                "month": month,
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
                "stored_bytes": stored_bytes,
                "gb_months": gb_months,
                "plan": plan,
                "bill": bill,
            }
        )
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bill import Bill
        from ..models.plan import Plan
        from ..models.usage_day import UsageDay

        d = dict(src_dict)
        period_start = d.pop("period_start")

        month = d.pop("month")

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

        stored_bytes = d.pop("stored_bytes")

        gb_months = d.pop("gb_months")

        plan = Plan.from_dict(d.pop("plan"))

        bill = Bill.from_dict(d.pop("bill"))

        _days = d.pop("days", UNSET)
        days: list[UsageDay] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = UsageDay.from_dict(days_item_data)

                days.append(days_item)

        usage = cls(
            period_start=period_start,
            month=month,
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
            stored_bytes=stored_bytes,
            gb_months=gb_months,
            plan=plan,
            bill=bill,
            days=days,
        )

        usage.additional_properties = d
        return usage

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
