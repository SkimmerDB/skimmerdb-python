from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.write_request import WriteRequest
from ...models.write_result import WriteResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: WriteRequest,
    wait: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["wait"] = wait

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/{name}/docs".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WriteResult | None:
    if response.status_code == 200:
        response_200 = WriteResult.from_dict(response.json())

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

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if response.status_code == 507:
        response_507 = Error.from_dict(response.json())

        return response_507

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | WriteResult]:
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
    body: WriteRequest,
    wait: bool | Unset = UNSET,
) -> Response[Error | WriteResult]:
    """Write documents

     Put (insert or replace) and delete in one request. Answers once the write is stored in object
    storage (about 250 ms); searchable on this server at once, everywhere within a second; wait: true
    answers once it's searchable here. A namespace that doesn't exist is made by the write (created:
    true in the answer): with vectors of the first vector's length and cosine when the documents have
    vectors, else text only (create it first for euclidean); past the plan's namespace count, 402
    namespace_limit. Metered as documents written and bytes written (see Usage). With Content-Type
    application/x-ndjson the body is one document a line (up to 16 MB; any length: POST
    .../docs/stream).

    Args:
        name (str):
        wait (bool | Unset):
        body (WriteRequest): 1 to 10,000 documents and deletes a request, 64 MB at most.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WriteResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        wait=wait,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: WriteRequest,
    wait: bool | Unset = UNSET,
) -> Error | WriteResult | None:
    """Write documents

     Put (insert or replace) and delete in one request. Answers once the write is stored in object
    storage (about 250 ms); searchable on this server at once, everywhere within a second; wait: true
    answers once it's searchable here. A namespace that doesn't exist is made by the write (created:
    true in the answer): with vectors of the first vector's length and cosine when the documents have
    vectors, else text only (create it first for euclidean); past the plan's namespace count, 402
    namespace_limit. Metered as documents written and bytes written (see Usage). With Content-Type
    application/x-ndjson the body is one document a line (up to 16 MB; any length: POST
    .../docs/stream).

    Args:
        name (str):
        wait (bool | Unset):
        body (WriteRequest): 1 to 10,000 documents and deletes a request, 64 MB at most.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WriteResult
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        wait=wait,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: WriteRequest,
    wait: bool | Unset = UNSET,
) -> Response[Error | WriteResult]:
    """Write documents

     Put (insert or replace) and delete in one request. Answers once the write is stored in object
    storage (about 250 ms); searchable on this server at once, everywhere within a second; wait: true
    answers once it's searchable here. A namespace that doesn't exist is made by the write (created:
    true in the answer): with vectors of the first vector's length and cosine when the documents have
    vectors, else text only (create it first for euclidean); past the plan's namespace count, 402
    namespace_limit. Metered as documents written and bytes written (see Usage). With Content-Type
    application/x-ndjson the body is one document a line (up to 16 MB; any length: POST
    .../docs/stream).

    Args:
        name (str):
        wait (bool | Unset):
        body (WriteRequest): 1 to 10,000 documents and deletes a request, 64 MB at most.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WriteResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        wait=wait,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: WriteRequest,
    wait: bool | Unset = UNSET,
) -> Error | WriteResult | None:
    """Write documents

     Put (insert or replace) and delete in one request. Answers once the write is stored in object
    storage (about 250 ms); searchable on this server at once, everywhere within a second; wait: true
    answers once it's searchable here. A namespace that doesn't exist is made by the write (created:
    true in the answer): with vectors of the first vector's length and cosine when the documents have
    vectors, else text only (create it first for euclidean); past the plan's namespace count, 402
    namespace_limit. Metered as documents written and bytes written (see Usage). With Content-Type
    application/x-ndjson the body is one document a line (up to 16 MB; any length: POST
    .../docs/stream).

    Args:
        name (str):
        wait (bool | Unset):
        body (WriteRequest): 1 to 10,000 documents and deletes a request, 64 MB at most.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WriteResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            wait=wait,
        )
    ).parsed
