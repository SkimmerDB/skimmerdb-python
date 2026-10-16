from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.usage import Usage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Usage | None:
    if response.status_code == 200:
        response_200 = Usage.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Usage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: bool | Unset = UNSET,
) -> Response[Error | Usage]:
    """Usage and bill this period

     This billing period so far and what it costs. Metered per tenant per UTC day: storage (GB-months),
    documents and bytes written, queries and the object-storage reads they made, the MCP part of queries
    and writes.

    Args:
        days (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Usage]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    days: bool | Unset = UNSET,
) -> Error | Usage | None:
    """Usage and bill this period

     This billing period so far and what it costs. Metered per tenant per UTC day: storage (GB-months),
    documents and bytes written, queries and the object-storage reads they made, the MCP part of queries
    and writes.

    Args:
        days (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Usage
    """

    return sync_detailed(
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    days: bool | Unset = UNSET,
) -> Response[Error | Usage]:
    """Usage and bill this period

     This billing period so far and what it costs. Metered per tenant per UTC day: storage (GB-months),
    documents and bytes written, queries and the object-storage reads they made, the MCP part of queries
    and writes.

    Args:
        days (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Usage]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    days: bool | Unset = UNSET,
) -> Error | Usage | None:
    """Usage and bill this period

     This billing period so far and what it costs. Metered per tenant per UTC day: storage (GB-months),
    documents and bytes written, queries and the object-storage reads they made, the MCP part of queries
    and writes.

    Args:
        days (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Usage
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
        )
    ).parsed
