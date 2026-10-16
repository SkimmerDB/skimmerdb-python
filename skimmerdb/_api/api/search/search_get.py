from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_result import SearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    q: str | Unset = UNSET,
    regex: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    scan: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["regex"] = regex

    params["filter"] = filter_

    params["limit"] = limit

    params["cursor"] = cursor

    params["scan"] = scan

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/search".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SearchResult | None:
    if response.status_code == 200:
        response_200 = SearchResult.from_dict(response.json())

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
) -> Response[Error | SearchResult]:
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
    q: str | Unset = UNSET,
    regex: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    scan: bool | Unset = UNSET,
) -> Response[Error | SearchResult]:
    """Search (query string)

     Text search as GET, the same answer as POST. Counts as one query (metered; see Usage).

    Args:
        name (str):
        q (str | Unset):
        regex (bool | Unset):
        filter_ (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        scan (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResult]
    """

    kwargs = _get_kwargs(
        name=name,
        q=q,
        regex=regex,
        filter_=filter_,
        limit=limit,
        cursor=cursor,
        scan=scan,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    regex: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    scan: bool | Unset = UNSET,
) -> Error | SearchResult | None:
    """Search (query string)

     Text search as GET, the same answer as POST. Counts as one query (metered; see Usage).

    Args:
        name (str):
        q (str | Unset):
        regex (bool | Unset):
        filter_ (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        scan (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResult
    """

    return sync_detailed(
        name=name,
        client=client,
        q=q,
        regex=regex,
        filter_=filter_,
        limit=limit,
        cursor=cursor,
        scan=scan,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    regex: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    scan: bool | Unset = UNSET,
) -> Response[Error | SearchResult]:
    """Search (query string)

     Text search as GET, the same answer as POST. Counts as one query (metered; see Usage).

    Args:
        name (str):
        q (str | Unset):
        regex (bool | Unset):
        filter_ (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        scan (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResult]
    """

    kwargs = _get_kwargs(
        name=name,
        q=q,
        regex=regex,
        filter_=filter_,
        limit=limit,
        cursor=cursor,
        scan=scan,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    regex: bool | Unset = UNSET,
    filter_: str | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    scan: bool | Unset = UNSET,
) -> Error | SearchResult | None:
    """Search (query string)

     Text search as GET, the same answer as POST. Counts as one query (metered; see Usage).

    Args:
        name (str):
        q (str | Unset):
        regex (bool | Unset):
        filter_ (str | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        scan (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            q=q,
            regex=regex,
            filter_=filter_,
            limit=limit,
            cursor=cursor,
            scan=scan,
        )
    ).parsed
