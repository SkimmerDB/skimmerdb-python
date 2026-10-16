from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.import_result import ImportResult
from ...models.import_rows_format import ImportRowsFormat
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    name: str,
    *,
    body: File,
    format_: ImportRowsFormat | Unset = "csv",
    id: str | Unset = UNSET,
    text: str | Unset = UNSET,
    schema: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_

    params["format"] = json_format_

    params["id"] = id

    params["text"] = text

    params["schema"] = schema

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/{name}/import".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ImportResult | None:
    if response.status_code == 200:
        response_200 = ImportResult.from_dict(response.json())

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
) -> Response[Error | ImportResult]:
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
    body: File,
    format_: ImportRowsFormat | Unset = "csv",
    id: str | Unset = UNSET,
    text: str | Unset = UNSET,
    schema: str | Unset = UNSET,
) -> Response[Error | ImportResult]:
    """Bulk import a file

     CSV, NDJSON or Parquet as the request body (up to 2 GB and 1M rows), parsed straight into one
    segment: all rows become visible together, or none. A namespace that doesn't exist is made by the
    import (text only; created: true). Metered as a write of that many documents and the file's bytes.

    Args:
        name (str):
        format_ (ImportRowsFormat | Unset):  Default: 'csv'.
        id (str | Unset):
        text (str | Unset):
        schema (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        format_=format_,
        id=id,
        text=text,
        schema=schema,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: ImportRowsFormat | Unset = "csv",
    id: str | Unset = UNSET,
    text: str | Unset = UNSET,
    schema: str | Unset = UNSET,
) -> Error | ImportResult | None:
    """Bulk import a file

     CSV, NDJSON or Parquet as the request body (up to 2 GB and 1M rows), parsed straight into one
    segment: all rows become visible together, or none. A namespace that doesn't exist is made by the
    import (text only; created: true). Metered as a write of that many documents and the file's bytes.

    Args:
        name (str):
        format_ (ImportRowsFormat | Unset):  Default: 'csv'.
        id (str | Unset):
        text (str | Unset):
        schema (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportResult
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
        format_=format_,
        id=id,
        text=text,
        schema=schema,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: ImportRowsFormat | Unset = "csv",
    id: str | Unset = UNSET,
    text: str | Unset = UNSET,
    schema: str | Unset = UNSET,
) -> Response[Error | ImportResult]:
    """Bulk import a file

     CSV, NDJSON or Parquet as the request body (up to 2 GB and 1M rows), parsed straight into one
    segment: all rows become visible together, or none. A namespace that doesn't exist is made by the
    import (text only; created: true). Metered as a write of that many documents and the file's bytes.

    Args:
        name (str):
        format_ (ImportRowsFormat | Unset):  Default: 'csv'.
        id (str | Unset):
        text (str | Unset):
        schema (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportResult]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
        format_=format_,
        id=id,
        text=text,
        schema=schema,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: File,
    format_: ImportRowsFormat | Unset = "csv",
    id: str | Unset = UNSET,
    text: str | Unset = UNSET,
    schema: str | Unset = UNSET,
) -> Error | ImportResult | None:
    """Bulk import a file

     CSV, NDJSON or Parquet as the request body (up to 2 GB and 1M rows), parsed straight into one
    segment: all rows become visible together, or none. A namespace that doesn't exist is made by the
    import (text only; created: true). Metered as a write of that many documents and the file's bytes.

    Args:
        name (str):
        format_ (ImportRowsFormat | Unset):  Default: 'csv'.
        id (str | Unset):
        text (str | Unset):
        schema (str | Unset):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
            format_=format_,
            id=id,
            text=text,
            schema=schema,
        )
    ).parsed
