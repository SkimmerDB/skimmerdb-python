from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_view_body import CreateViewBody
from ...models.error import Error
from ...models.view_created import ViewCreated
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: CreateViewBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/{name}/views".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ViewCreated | None:
    if response.status_code == 201:
        response_201 = ViewCreated.from_dict(response.json())

        return response_201

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
) -> Response[Error | ViewCreated]:
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
    body: CreateViewBody,
) -> Response[Error | ViewCreated]:
    """Create a view

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace. Its name is the tenant's (not a namespace's name, not docs). Creating one runs it once
    (metered as a query) and answers its columns. A query that can't run from parts is refused with 422
    view_not_decomposable and the reason; past the plan's views, 402 view_limit.

    Args:
        name (str):
        body (CreateViewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewCreated]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateViewBody,
) -> Error | ViewCreated | None:
    """Create a view

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace. Its name is the tenant's (not a namespace's name, not docs). Creating one runs it once
    (metered as a query) and answers its columns. A query that can't run from parts is refused with 422
    view_not_decomposable and the reason; past the plan's views, 402 view_limit.

    Args:
        name (str):
        body (CreateViewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ViewCreated
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateViewBody,
) -> Response[Error | ViewCreated]:
    """Create a view

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace. Its name is the tenant's (not a namespace's name, not docs). Creating one runs it once
    (metered as a query) and answers its columns. A query that can't run from parts is refused with 422
    view_not_decomposable and the reason; past the plan's views, 402 view_limit.

    Args:
        name (str):
        body (CreateViewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ViewCreated]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateViewBody,
) -> Error | ViewCreated | None:
    """Create a view

     A view is a SQL query over one namespace (FROM docs) whose answer is kept as partials per segment:
    COUNT, SUM, MIN, MAX, AVG, COUNT(DISTINCT ...), COUNT_IF and f(...) FILTER (WHERE ...) over any
    WHERE, GROUP BY any expressions (DATE_TRUNC buckets, CASE, ...), with HAVING, ORDER BY and LIMIT
    applied on top. Name it as a table in SQL (SELECT * FROM daily_signups, or join it). It is always
    exact: a segment's partial is reused only while that segment's visible rows are the ones it was
    computed from, so a write or delete recomputes only the segments it touched. Views go with their
    namespace. Its name is the tenant's (not a namespace's name, not docs). Creating one runs it once
    (metered as a query) and answers its columns. A query that can't run from parts is refused with 422
    view_not_decomposable and the reason; past the plan's views, 402 view_limit.

    Args:
        name (str):
        body (CreateViewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ViewCreated
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
