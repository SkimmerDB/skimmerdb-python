from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.stored_document import StoredDocument
from ...types import Response


def _get_kwargs(
    name: str,
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/docs/{id}".format(
            name=quote(str(name), safe=""),
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | StoredDocument | None:
    if response.status_code == 200:
        response_200 = StoredDocument.from_dict(response.json())

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
) -> Response[Error | StoredDocument]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | StoredDocument]:
    """Get a document

     One whole, with its vector. Ids may hold slashes (the rest of the path is the id). Counts as one
    query (metered; see Usage).

    Args:
        name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoredDocument]
    """

    kwargs = _get_kwargs(
        name=name,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | StoredDocument | None:
    """Get a document

     One whole, with its vector. Ids may hold slashes (the rest of the path is the id). Counts as one
    query (metered; see Usage).

    Args:
        name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoredDocument
    """

    return sync_detailed(
        name=name,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | StoredDocument]:
    """Get a document

     One whole, with its vector. Ids may hold slashes (the rest of the path is the id). Counts as one
    query (metered; see Usage).

    Args:
        name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StoredDocument]
    """

    kwargs = _get_kwargs(
        name=name,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | StoredDocument | None:
    """Get a document

     One whole, with its vector. Ids may hold slashes (the rest of the path is the id). Counts as one
    query (metered; see Usage).

    Args:
        name (str):
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StoredDocument
    """

    return (
        await asyncio_detailed(
            name=name,
            id=id,
            client=client,
        )
    ).parsed
