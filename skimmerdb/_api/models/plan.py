from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Plan")


@_attrs_define
class Plan:
    """
    Attributes:
        name (str):
        price_month (float):
        included_gb_months (float):
        included_write_gb (float):
        included_queries (int):
        included_writes (int):
        included_embed_tokens (int):
        per_gb_month (float):
        per_gb_written (float):
        per_million_queries (float):
        per_million_embed_tokens (float):
        per_million_store_gets (float):
        hard_limit (bool):
        qps (int):
        concurrency (int):
        storage_quota_gb (float):
        read_inflight_mb (int):
        sql_seconds (int):
        sql_concurrency (int):
        query_seconds (int):
        max_namespaces (int):
        included_cpu_seconds (float):
        included_store_gets (int):
        included_out_gb (float):
        max_creates_day (int):
        unverified_share (float):
        max_views (int):
        export_seconds (int):
        export_concurrency (int):
        exports_day (int):
        export_max_gb (float):
    """

    name: str
    price_month: float
    included_gb_months: float
    included_write_gb: float
    included_queries: int
    included_writes: int
    included_embed_tokens: int
    per_gb_month: float
    per_gb_written: float
    per_million_queries: float
    per_million_embed_tokens: float
    per_million_store_gets: float
    hard_limit: bool
    qps: int
    concurrency: int
    storage_quota_gb: float
    read_inflight_mb: int
    sql_seconds: int
    sql_concurrency: int
    query_seconds: int
    max_namespaces: int
    included_cpu_seconds: float
    included_store_gets: int
    included_out_gb: float
    max_creates_day: int
    unverified_share: float
    max_views: int
    export_seconds: int
    export_concurrency: int
    exports_day: int
    export_max_gb: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        price_month = self.price_month

        included_gb_months = self.included_gb_months

        included_write_gb = self.included_write_gb

        included_queries = self.included_queries

        included_writes = self.included_writes

        included_embed_tokens = self.included_embed_tokens

        per_gb_month = self.per_gb_month

        per_gb_written = self.per_gb_written

        per_million_queries = self.per_million_queries

        per_million_embed_tokens = self.per_million_embed_tokens

        per_million_store_gets = self.per_million_store_gets

        hard_limit = self.hard_limit

        qps = self.qps

        concurrency = self.concurrency

        storage_quota_gb = self.storage_quota_gb

        read_inflight_mb = self.read_inflight_mb

        sql_seconds = self.sql_seconds

        sql_concurrency = self.sql_concurrency

        query_seconds = self.query_seconds

        max_namespaces = self.max_namespaces

        included_cpu_seconds = self.included_cpu_seconds

        included_store_gets = self.included_store_gets

        included_out_gb = self.included_out_gb

        max_creates_day = self.max_creates_day

        unverified_share = self.unverified_share

        max_views = self.max_views

        export_seconds = self.export_seconds

        export_concurrency = self.export_concurrency

        exports_day = self.exports_day

        export_max_gb = self.export_max_gb

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "price_month": price_month,
                "included_gb_months": included_gb_months,
                "included_write_gb": included_write_gb,
                "included_queries": included_queries,
                "included_writes": included_writes,
                "included_embed_tokens": included_embed_tokens,
                "per_gb_month": per_gb_month,
                "per_gb_written": per_gb_written,
                "per_million_queries": per_million_queries,
                "per_million_embed_tokens": per_million_embed_tokens,
                "per_million_store_gets": per_million_store_gets,
                "hard_limit": hard_limit,
                "qps": qps,
                "concurrency": concurrency,
                "storage_quota_gb": storage_quota_gb,
                "read_inflight_mb": read_inflight_mb,
                "sql_seconds": sql_seconds,
                "sql_concurrency": sql_concurrency,
                "query_seconds": query_seconds,
                "max_namespaces": max_namespaces,
                "included_cpu_seconds": included_cpu_seconds,
                "included_store_gets": included_store_gets,
                "included_out_gb": included_out_gb,
                "max_creates_day": max_creates_day,
                "unverified_share": unverified_share,
                "max_views": max_views,
                "export_seconds": export_seconds,
                "export_concurrency": export_concurrency,
                "exports_day": exports_day,
                "export_max_gb": export_max_gb,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        price_month = d.pop("price_month")

        included_gb_months = d.pop("included_gb_months")

        included_write_gb = d.pop("included_write_gb")

        included_queries = d.pop("included_queries")

        included_writes = d.pop("included_writes")

        included_embed_tokens = d.pop("included_embed_tokens")

        per_gb_month = d.pop("per_gb_month")

        per_gb_written = d.pop("per_gb_written")

        per_million_queries = d.pop("per_million_queries")

        per_million_embed_tokens = d.pop("per_million_embed_tokens")

        per_million_store_gets = d.pop("per_million_store_gets")

        hard_limit = d.pop("hard_limit")

        qps = d.pop("qps")

        concurrency = d.pop("concurrency")

        storage_quota_gb = d.pop("storage_quota_gb")

        read_inflight_mb = d.pop("read_inflight_mb")

        sql_seconds = d.pop("sql_seconds")

        sql_concurrency = d.pop("sql_concurrency")

        query_seconds = d.pop("query_seconds")

        max_namespaces = d.pop("max_namespaces")

        included_cpu_seconds = d.pop("included_cpu_seconds")

        included_store_gets = d.pop("included_store_gets")

        included_out_gb = d.pop("included_out_gb")

        max_creates_day = d.pop("max_creates_day")

        unverified_share = d.pop("unverified_share")

        max_views = d.pop("max_views")

        export_seconds = d.pop("export_seconds")

        export_concurrency = d.pop("export_concurrency")

        exports_day = d.pop("exports_day")

        export_max_gb = d.pop("export_max_gb")

        plan = cls(
            name=name,
            price_month=price_month,
            included_gb_months=included_gb_months,
            included_write_gb=included_write_gb,
            included_queries=included_queries,
            included_writes=included_writes,
            included_embed_tokens=included_embed_tokens,
            per_gb_month=per_gb_month,
            per_gb_written=per_gb_written,
            per_million_queries=per_million_queries,
            per_million_embed_tokens=per_million_embed_tokens,
            per_million_store_gets=per_million_store_gets,
            hard_limit=hard_limit,
            qps=qps,
            concurrency=concurrency,
            storage_quota_gb=storage_quota_gb,
            read_inflight_mb=read_inflight_mb,
            sql_seconds=sql_seconds,
            sql_concurrency=sql_concurrency,
            query_seconds=query_seconds,
            max_namespaces=max_namespaces,
            included_cpu_seconds=included_cpu_seconds,
            included_store_gets=included_store_gets,
            included_out_gb=included_out_gb,
            max_creates_day=max_creates_day,
            unverified_share=unverified_share,
            max_views=max_views,
            export_seconds=export_seconds,
            export_concurrency=export_concurrency,
            exports_day=exports_day,
            export_max_gb=export_max_gb,
        )

        plan.additional_properties = d
        return plan

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
