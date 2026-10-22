from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.query_sql_get_format import QuerySqlGetFormat
from ...models.sql_result import SqlResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    sql: str | Unset = UNSET,
    format_: QuerySqlGetFormat | Unset = "json",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["sql"] = sql

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/sql".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

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

    if response.status_code == 405:
        response_405 = Error.from_dict(response.json())

        return response_405

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
    name: str,
    *,
    client: AuthenticatedClient | Client,
    sql: str | Unset = UNSET,
    format_: QuerySqlGetFormat | Unset = "json",
) -> Response[Error | SqlResult]:
    """SQL over a namespace, by URL (beta)

     Beta. As POST /v1/namespaces/{name}/sql. The same query as a GET, for clients that can only fetch a
    URL: DuckDB's read_csv / read_json over https (with a CREATE SECRET of TYPE http and BEARER_TOKEN),
    curl, a spreadsheet's import. The SQL goes in ?sql= (URL-encoded; DuckDB reads a * in a URL as a
    glob: write %2A). Reads only: SQL that writes answers 405.

    Args:
        name (str):
        sql (str | Unset):
        format_ (QuerySqlGetFormat | Unset):  Default: 'json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SqlResult]
    """

    kwargs = _get_kwargs(
        name=name,
        sql=sql,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    sql: str | Unset = UNSET,
    format_: QuerySqlGetFormat | Unset = "json",
) -> Error | SqlResult | None:
    """SQL over a namespace, by URL (beta)

     Beta. As POST /v1/namespaces/{name}/sql. The same query as a GET, for clients that can only fetch a
    URL: DuckDB's read_csv / read_json over https (with a CREATE SECRET of TYPE http and BEARER_TOKEN),
    curl, a spreadsheet's import. The SQL goes in ?sql= (URL-encoded; DuckDB reads a * in a URL as a
    glob: write %2A). Reads only: SQL that writes answers 405.

    Args:
        name (str):
        sql (str | Unset):
        format_ (QuerySqlGetFormat | Unset):  Default: 'json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SqlResult
    """

    return sync_detailed(
        name=name,
        client=client,
        sql=sql,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    sql: str | Unset = UNSET,
    format_: QuerySqlGetFormat | Unset = "json",
) -> Response[Error | SqlResult]:
    """SQL over a namespace, by URL (beta)

     Beta. As POST /v1/namespaces/{name}/sql. The same query as a GET, for clients that can only fetch a
    URL: DuckDB's read_csv / read_json over https (with a CREATE SECRET of TYPE http and BEARER_TOKEN),
    curl, a spreadsheet's import. The SQL goes in ?sql= (URL-encoded; DuckDB reads a * in a URL as a
    glob: write %2A). Reads only: SQL that writes answers 405.

    Args:
        name (str):
        sql (str | Unset):
        format_ (QuerySqlGetFormat | Unset):  Default: 'json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SqlResult]
    """

    kwargs = _get_kwargs(
        name=name,
        sql=sql,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    sql: str | Unset = UNSET,
    format_: QuerySqlGetFormat | Unset = "json",
) -> Error | SqlResult | None:
    """SQL over a namespace, by URL (beta)

     Beta. As POST /v1/namespaces/{name}/sql. The same query as a GET, for clients that can only fetch a
    URL: DuckDB's read_csv / read_json over https (with a CREATE SECRET of TYPE http and BEARER_TOKEN),
    curl, a spreadsheet's import. The SQL goes in ?sql= (URL-encoded; DuckDB reads a * in a URL as a
    glob: write %2A). Reads only: SQL that writes answers 405.

    Args:
        name (str):
        sql (str | Unset):
        format_ (QuerySqlGetFormat | Unset):  Default: 'json'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SqlResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            sql=sql,
            format_=format_,
        )
    ).parsed
