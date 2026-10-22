from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.view import View
from ...types import Response


def _get_kwargs(
    name: str,
    view: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/views/{view}".format(
            name=quote(str(name), safe=""),
            view=quote(str(view), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | View | None:
    if response.status_code == 200:
        response_200 = View.from_dict(response.json())

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
) -> Response[Error | View]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    view: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | View]:
    """Get a view

    Args:
        name (str):
        view (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | View]
    """

    kwargs = _get_kwargs(
        name=name,
        view=view,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    view: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | View | None:
    """Get a view

    Args:
        name (str):
        view (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | View
    """

    return sync_detailed(
        name=name,
        view=view,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    view: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | View]:
    """Get a view

    Args:
        name (str):
        view (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | View]
    """

    kwargs = _get_kwargs(
        name=name,
        view=view,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    view: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | View | None:
    """Get a view

    Args:
        name (str):
        view (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | View
    """

    return (
        await asyncio_detailed(
            name=name,
            view=view,
            client=client,
        )
    ).parsed
