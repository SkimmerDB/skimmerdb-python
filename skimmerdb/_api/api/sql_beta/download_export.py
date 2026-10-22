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
    id: str,
    *,
    range_: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(range_, Unset):
        headers["Range"] = range_

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/sql/exports/{id}/download".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | File | None:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410

    if response.status_code == 416:
        response_416 = Error.from_dict(response.json())

        return response_416

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
) -> Response[Error | File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: str | Unset = UNSET,
) -> Response[Error | File]:
    """Download an export (beta)

     The file, streamed (Content-Type text/csv, application/x-ndjson or application/vnd.apache.parquet;
    X-Skimmerdb-Size: its size). Resumable: Range: bytes=first-last (one range) answers 206 with
    Content-Range. Metered as bytes returned; on the free plan a download stops when they're used up (a
    range past them: 402).

    Args:
        id (str):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: str | Unset = UNSET,
) -> Error | File | None:
    """Download an export (beta)

     The file, streamed (Content-Type text/csv, application/x-ndjson or application/vnd.apache.parquet;
    X-Skimmerdb-Size: its size). Resumable: Range: bytes=first-last (one range) answers 206 with
    Content-Range. Metered as bytes returned; on the free plan a download stops when they're used up (a
    range past them: 402).

    Args:
        id (str):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return sync_detailed(
        id=id,
        client=client,
        range_=range_,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: str | Unset = UNSET,
) -> Response[Error | File]:
    """Download an export (beta)

     The file, streamed (Content-Type text/csv, application/x-ndjson or application/vnd.apache.parquet;
    X-Skimmerdb-Size: its size). Resumable: Range: bytes=first-last (one range) answers 206 with
    Content-Range. Metered as bytes returned; on the free plan a download stops when they're used up (a
    range past them: 402).

    Args:
        id (str):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | File]
    """

    kwargs = _get_kwargs(
        id=id,
        range_=range_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    range_: str | Unset = UNSET,
) -> Error | File | None:
    """Download an export (beta)

     The file, streamed (Content-Type text/csv, application/x-ndjson or application/vnd.apache.parquet;
    X-Skimmerdb-Size: its size). Resumable: Range: bytes=first-last (one range) answers 206 with
    Content-Range. Metered as bytes returned; on the free plan a download stops when they're used up (a
    range past them: 402).

    Args:
        id (str):
        range_ (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | File
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            range_=range_,
        )
    ).parsed
