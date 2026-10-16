from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    name: str,
    seg: str,
    file: str,
    *,
    off: int | Unset = UNSET,
    n: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["off"] = off

    params["n"] = n

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/namespaces/{name}/sidecars/{seg}/{file}".format(
            name=quote(str(name), safe=""),
            seg=quote(str(seg), safe=""),
            file=quote(str(file), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    seg: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    off: int | Unset = UNSET,
    n: int | Unset = UNSET,
) -> Response[Error | File]:
    """Read a sidecar file

     Its bytes (at most 64 MB a call). Counts as one query (metered; see Usage).

    Args:
        name (str):
        seg (str):
        file (str):
        off (int | Unset):
        n (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        name=name,
        seg=seg,
        file=file,
        off=off,
        n=n,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    seg: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    off: int | Unset = UNSET,
    n: int | Unset = UNSET,
) -> Error | File | None:
    """Read a sidecar file

     Its bytes (at most 64 MB a call). Counts as one query (metered; see Usage).

    Args:
        name (str):
        seg (str):
        file (str):
        off (int | Unset):
        n (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return sync_detailed(
        name=name,
        seg=seg,
        file=file,
        client=client,
        off=off,
        n=n,
    ).parsed


async def asyncio_detailed(
    name: str,
    seg: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    off: int | Unset = UNSET,
    n: int | Unset = UNSET,
) -> Response[Error | File]:
    """Read a sidecar file

     Its bytes (at most 64 MB a call). Counts as one query (metered; see Usage).

    Args:
        name (str):
        seg (str):
        file (str):
        off (int | Unset):
        n (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        name=name,
        seg=seg,
        file=file,
        off=off,
        n=n,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    seg: str,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    off: int | Unset = UNSET,
    n: int | Unset = UNSET,
) -> Error | File | None:
    """Read a sidecar file

     Its bytes (at most 64 MB a call). Counts as one query (metered; see Usage).

    Args:
        name (str):
        seg (str):
        file (str):
        off (int | Unset):
        n (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return (
        await asyncio_detailed(
            name=name,
            seg=seg,
            file=file,
            client=client,
            off=off,
            n=n,
        )
    ).parsed
