from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.query_sql_tenant_format import (
    QuerySqlTenantFormat,
)
from ...models.sql_request import SqlRequest
from ...models.sql_result import SqlResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SqlRequest,
    format_: QuerySqlTenantFormat | Unset = "json",
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sql",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SqlResult | None:
    if response.status_code == 200:
        response_200 = SqlResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if response.status_code == 507:
        response_507 = Error.from_dict(response.json())

        return response_507

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SqlResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SqlRequest,
    format_: QuerySqlTenantFormat | Unset = "json",
) -> Response[Error | SqlResult]:
    """SQL across namespaces (beta)

     Beta. A query whose tables are the tenant's namespaces, each by name (quoted when it has - or .:
    "web-logs"); no table is docs here. A key limited to some namespaces sees only those: any other name
    is no table, like one nobody has. Columns: id and every top-level meta key, typed from the values:
    int (booleans 1/0), float, text, date or time; missing is NULL; SHOW COLUMNS lists a namespace's.
    contains(text, '...') and grep(text, 'regex') go through the text index (in WHERE, on one table:
    contains(e.text, ...) when there are several). SELECT, WITH, UNION / INTERSECT / EXCEPT [ALL]; joins
    (INNER, LEFT, RIGHT, FULL, CROSS, USING, NATURAL); subqueries (IN, EXISTS, scalar, in FROM;
    correlated as [NOT] EXISTS / IN with = conditions); GROUP BY (ROLLUP, CUBE, GROUPING SETS), HAVING,
    QUALIFY, DISTINCT, ORDER BY, LIMIT / OFFSET; window functions (ROW_NUMBER, RANK, DENSE_RANK, NTILE,
    PERCENT_RANK, CUME_DIST, LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE, aggregates OVER (PARTITION
    BY ... ORDER BY ... ROWS BETWEEN ...)); aggregates COUNT, COUNT(DISTINCT), SUM, AVG, MIN, MAX,
    STDDEV, VARIANCE, MEDIAN, QUANTILE, PERCENTILE_CONT / _DISC, MODE, STRING_AGG, ARG_MIN / ARG_MAX,
    BOOL_AND / BOOL_OR, COUNT_IF, CORR, with FILTER (WHERE ...); + - * / (a float; NULL dividing by 0)
    // %; CASE, COALESCE, NULLIF, CAST / TRY_CAST, text, math and date functions (LOWER, SUBSTRING,
    CONCAT, ||, REPLACE, SPLIT_PART, REGEXP_*, ROUND, EXTRACT, DATE_TRUNC, DATE_DIFF, INTERVAL,
    STRFTIME, ...). LENGTH counts bytes, CHAR_LENGTH characters. A query reads at most 16 tables; JSON
    answers stop at 10,000 rows (truncated): format=ndjson or csv (or Accept: application/x-ndjson /
    text/csv) streams every row instead (a plain scan of one namespace any number, window by window;
    other shapes up to their row cap, then a last too_many_rows line and a broken transfer), and POST
    /v1/sql/exports writes an answer to a file. Writes (write scope): INSERT INTO ns [(columns)] VALUES
    (...) | SELECT ..., CREATE TABLE ns AS SELECT ..., DELETE FROM ns [WHERE ...]; a row's id column
    names the document (an existing id is replaced), its text column is its text, the rest metadata;
    each statement is one commit (all rows or none; a DELETE removes at most 1,000,000), metered as
    writes, and the answer has dml. Reference: https://docs.skimmerdb.com/reference/sql. A time limit
    per plan (10 s free, 30 s pro) and SQL queries in flight per tenant (2 free, 8 pro; 429 past it).
    Errors in the SQL are 422 with the reason; 413 when it would read too much. One query is metered,
    however many namespaces it reads. Counts as one query (metered; see Usage).

    Args:
        format_ (QuerySqlTenantFormat | Unset):  Default: 'json'.
        body (SqlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SqlResult]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SqlRequest,
    format_: QuerySqlTenantFormat | Unset = "json",
) -> Error | SqlResult | None:
    """SQL across namespaces (beta)

     Beta. A query whose tables are the tenant's namespaces, each by name (quoted when it has - or .:
    "web-logs"); no table is docs here. A key limited to some namespaces sees only those: any other name
    is no table, like one nobody has. Columns: id and every top-level meta key, typed from the values:
    int (booleans 1/0), float, text, date or time; missing is NULL; SHOW COLUMNS lists a namespace's.
    contains(text, '...') and grep(text, 'regex') go through the text index (in WHERE, on one table:
    contains(e.text, ...) when there are several). SELECT, WITH, UNION / INTERSECT / EXCEPT [ALL]; joins
    (INNER, LEFT, RIGHT, FULL, CROSS, USING, NATURAL); subqueries (IN, EXISTS, scalar, in FROM;
    correlated as [NOT] EXISTS / IN with = conditions); GROUP BY (ROLLUP, CUBE, GROUPING SETS), HAVING,
    QUALIFY, DISTINCT, ORDER BY, LIMIT / OFFSET; window functions (ROW_NUMBER, RANK, DENSE_RANK, NTILE,
    PERCENT_RANK, CUME_DIST, LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE, aggregates OVER (PARTITION
    BY ... ORDER BY ... ROWS BETWEEN ...)); aggregates COUNT, COUNT(DISTINCT), SUM, AVG, MIN, MAX,
    STDDEV, VARIANCE, MEDIAN, QUANTILE, PERCENTILE_CONT / _DISC, MODE, STRING_AGG, ARG_MIN / ARG_MAX,
    BOOL_AND / BOOL_OR, COUNT_IF, CORR, with FILTER (WHERE ...); + - * / (a float; NULL dividing by 0)
    // %; CASE, COALESCE, NULLIF, CAST / TRY_CAST, text, math and date functions (LOWER, SUBSTRING,
    CONCAT, ||, REPLACE, SPLIT_PART, REGEXP_*, ROUND, EXTRACT, DATE_TRUNC, DATE_DIFF, INTERVAL,
    STRFTIME, ...). LENGTH counts bytes, CHAR_LENGTH characters. A query reads at most 16 tables; JSON
    answers stop at 10,000 rows (truncated): format=ndjson or csv (or Accept: application/x-ndjson /
    text/csv) streams every row instead (a plain scan of one namespace any number, window by window;
    other shapes up to their row cap, then a last too_many_rows line and a broken transfer), and POST
    /v1/sql/exports writes an answer to a file. Writes (write scope): INSERT INTO ns [(columns)] VALUES
    (...) | SELECT ..., CREATE TABLE ns AS SELECT ..., DELETE FROM ns [WHERE ...]; a row's id column
    names the document (an existing id is replaced), its text column is its text, the rest metadata;
    each statement is one commit (all rows or none; a DELETE removes at most 1,000,000), metered as
    writes, and the answer has dml. Reference: https://docs.skimmerdb.com/reference/sql. A time limit
    per plan (10 s free, 30 s pro) and SQL queries in flight per tenant (2 free, 8 pro; 429 past it).
    Errors in the SQL are 422 with the reason; 413 when it would read too much. One query is metered,
    however many namespaces it reads. Counts as one query (metered; see Usage).

    Args:
        format_ (QuerySqlTenantFormat | Unset):  Default: 'json'.
        body (SqlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SqlResult
    """

    return sync_detailed(
        client=client,
        body=body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SqlRequest,
    format_: QuerySqlTenantFormat | Unset = "json",
) -> Response[Error | SqlResult]:
    """SQL across namespaces (beta)

     Beta. A query whose tables are the tenant's namespaces, each by name (quoted when it has - or .:
    "web-logs"); no table is docs here. A key limited to some namespaces sees only those: any other name
    is no table, like one nobody has. Columns: id and every top-level meta key, typed from the values:
    int (booleans 1/0), float, text, date or time; missing is NULL; SHOW COLUMNS lists a namespace's.
    contains(text, '...') and grep(text, 'regex') go through the text index (in WHERE, on one table:
    contains(e.text, ...) when there are several). SELECT, WITH, UNION / INTERSECT / EXCEPT [ALL]; joins
    (INNER, LEFT, RIGHT, FULL, CROSS, USING, NATURAL); subqueries (IN, EXISTS, scalar, in FROM;
    correlated as [NOT] EXISTS / IN with = conditions); GROUP BY (ROLLUP, CUBE, GROUPING SETS), HAVING,
    QUALIFY, DISTINCT, ORDER BY, LIMIT / OFFSET; window functions (ROW_NUMBER, RANK, DENSE_RANK, NTILE,
    PERCENT_RANK, CUME_DIST, LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE, aggregates OVER (PARTITION
    BY ... ORDER BY ... ROWS BETWEEN ...)); aggregates COUNT, COUNT(DISTINCT), SUM, AVG, MIN, MAX,
    STDDEV, VARIANCE, MEDIAN, QUANTILE, PERCENTILE_CONT / _DISC, MODE, STRING_AGG, ARG_MIN / ARG_MAX,
    BOOL_AND / BOOL_OR, COUNT_IF, CORR, with FILTER (WHERE ...); + - * / (a float; NULL dividing by 0)
    // %; CASE, COALESCE, NULLIF, CAST / TRY_CAST, text, math and date functions (LOWER, SUBSTRING,
    CONCAT, ||, REPLACE, SPLIT_PART, REGEXP_*, ROUND, EXTRACT, DATE_TRUNC, DATE_DIFF, INTERVAL,
    STRFTIME, ...). LENGTH counts bytes, CHAR_LENGTH characters. A query reads at most 16 tables; JSON
    answers stop at 10,000 rows (truncated): format=ndjson or csv (or Accept: application/x-ndjson /
    text/csv) streams every row instead (a plain scan of one namespace any number, window by window;
    other shapes up to their row cap, then a last too_many_rows line and a broken transfer), and POST
    /v1/sql/exports writes an answer to a file. Writes (write scope): INSERT INTO ns [(columns)] VALUES
    (...) | SELECT ..., CREATE TABLE ns AS SELECT ..., DELETE FROM ns [WHERE ...]; a row's id column
    names the document (an existing id is replaced), its text column is its text, the rest metadata;
    each statement is one commit (all rows or none; a DELETE removes at most 1,000,000), metered as
    writes, and the answer has dml. Reference: https://docs.skimmerdb.com/reference/sql. A time limit
    per plan (10 s free, 30 s pro) and SQL queries in flight per tenant (2 free, 8 pro; 429 past it).
    Errors in the SQL are 422 with the reason; 413 when it would read too much. One query is metered,
    however many namespaces it reads. Counts as one query (metered; see Usage).

    Args:
        format_ (QuerySqlTenantFormat | Unset):  Default: 'json'.
        body (SqlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SqlResult]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SqlRequest,
    format_: QuerySqlTenantFormat | Unset = "json",
) -> Error | SqlResult | None:
    """SQL across namespaces (beta)

     Beta. A query whose tables are the tenant's namespaces, each by name (quoted when it has - or .:
    "web-logs"); no table is docs here. A key limited to some namespaces sees only those: any other name
    is no table, like one nobody has. Columns: id and every top-level meta key, typed from the values:
    int (booleans 1/0), float, text, date or time; missing is NULL; SHOW COLUMNS lists a namespace's.
    contains(text, '...') and grep(text, 'regex') go through the text index (in WHERE, on one table:
    contains(e.text, ...) when there are several). SELECT, WITH, UNION / INTERSECT / EXCEPT [ALL]; joins
    (INNER, LEFT, RIGHT, FULL, CROSS, USING, NATURAL); subqueries (IN, EXISTS, scalar, in FROM;
    correlated as [NOT] EXISTS / IN with = conditions); GROUP BY (ROLLUP, CUBE, GROUPING SETS), HAVING,
    QUALIFY, DISTINCT, ORDER BY, LIMIT / OFFSET; window functions (ROW_NUMBER, RANK, DENSE_RANK, NTILE,
    PERCENT_RANK, CUME_DIST, LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE, aggregates OVER (PARTITION
    BY ... ORDER BY ... ROWS BETWEEN ...)); aggregates COUNT, COUNT(DISTINCT), SUM, AVG, MIN, MAX,
    STDDEV, VARIANCE, MEDIAN, QUANTILE, PERCENTILE_CONT / _DISC, MODE, STRING_AGG, ARG_MIN / ARG_MAX,
    BOOL_AND / BOOL_OR, COUNT_IF, CORR, with FILTER (WHERE ...); + - * / (a float; NULL dividing by 0)
    // %; CASE, COALESCE, NULLIF, CAST / TRY_CAST, text, math and date functions (LOWER, SUBSTRING,
    CONCAT, ||, REPLACE, SPLIT_PART, REGEXP_*, ROUND, EXTRACT, DATE_TRUNC, DATE_DIFF, INTERVAL,
    STRFTIME, ...). LENGTH counts bytes, CHAR_LENGTH characters. A query reads at most 16 tables; JSON
    answers stop at 10,000 rows (truncated): format=ndjson or csv (or Accept: application/x-ndjson /
    text/csv) streams every row instead (a plain scan of one namespace any number, window by window;
    other shapes up to their row cap, then a last too_many_rows line and a broken transfer), and POST
    /v1/sql/exports writes an answer to a file. Writes (write scope): INSERT INTO ns [(columns)] VALUES
    (...) | SELECT ..., CREATE TABLE ns AS SELECT ..., DELETE FROM ns [WHERE ...]; a row's id column
    names the document (an existing id is replaced), its text column is its text, the rest metadata;
    each statement is one commit (all rows or none; a DELETE removes at most 1,000,000), metered as
    writes, and the answer has dml. Reference: https://docs.skimmerdb.com/reference/sql. A time limit
    per plan (10 s free, 30 s pro) and SQL queries in flight per tenant (2 free, 8 pro; 429 past it).
    Errors in the SQL are 422 with the reason; 413 when it would read too much. One query is metered,
    however many namespaces it reads. Counts as one query (metered; see Usage).

    Args:
        format_ (QuerySqlTenantFormat | Unset):  Default: 'json'.
        body (SqlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SqlResult
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
