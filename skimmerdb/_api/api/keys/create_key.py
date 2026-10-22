from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.key_request import KeyRequest
from ...models.new_key import NewKey
from ...types import Response


def _get_kwargs(
    *,
    body: KeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | NewKey | None:
    if response.status_code == 201:
        response_201 = NewKey.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | NewKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequest,
) -> Response[Error | NewKey]:
    """Make an API key

     The key is in the answer only. Scopes: read: list namespaces, search, count, get documents, warm,
    SQL, usage. write: also create and delete namespaces and views, write, update, delete and import
    documents. admin: also make, list, change and revoke keys, and billing. Only an admin key without
    namespace limits or caps (or the owner's login) can manage keys, so a read or write key can't make
    more.

    Args:
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NewKey]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequest,
) -> Error | NewKey | None:
    """Make an API key

     The key is in the answer only. Scopes: read: list namespaces, search, count, get documents, warm,
    SQL, usage. write: also create and delete namespaces and views, write, update, delete and import
    documents. admin: also make, list, change and revoke keys, and billing. Only an admin key without
    namespace limits or caps (or the owner's login) can manage keys, so a read or write key can't make
    more.

    Args:
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NewKey
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequest,
) -> Response[Error | NewKey]:
    """Make an API key

     The key is in the answer only. Scopes: read: list namespaces, search, count, get documents, warm,
    SQL, usage. write: also create and delete namespaces and views, write, update, delete and import
    documents. admin: also make, list, change and revoke keys, and billing. Only an admin key without
    namespace limits or caps (or the owner's login) can manage keys, so a read or write key can't make
    more.

    Args:
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | NewKey]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequest,
) -> Error | NewKey | None:
    """Make an API key

     The key is in the answer only. Scopes: read: list namespaces, search, count, get documents, warm,
    SQL, usage. write: also create and delete namespaces and views, write, update, delete and import
    documents. admin: also make, list, change and revoke keys, and billing. Only an admin key without
    namespace limits or caps (or the owner's login) can manage keys, so a read or write key can't make
    more.

    Args:
        body (KeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | NewKey
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
