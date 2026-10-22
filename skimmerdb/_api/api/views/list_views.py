from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.view_list import ViewList
from ...types import Response


def _get_kwargs(
    name: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/views".format(
            name=quote(str(name), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ViewList | None:
    if response.status_code == 200:
        response_200 = ViewList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ViewList]:
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
) -> Response[Error | ViewList]:
    """List a namespace's views

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewList]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ViewList | None:
    """List a namespace's views

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ViewList
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | ViewList]:
    """List a namespace's views

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewList]
    """

    kwargs = _get_kwargs(
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | ViewList | None:
    """List a namespace's views

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace.

    Args:
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ViewList
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
