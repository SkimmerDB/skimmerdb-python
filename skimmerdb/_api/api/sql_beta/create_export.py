from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.export import Export
from ...models.export_request import ExportRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ExportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sql/exports",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Export | None:
    if response.status_code == 202:
        response_202 = Export.from_dict(response.json())

        return response_202

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
) -> Response[Error | Export]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportRequest,
) -> Response[Error | Export]:
    """Export a query's answer (beta)

     For answers too big or too slow for a request: the query runs in the background (the plan's
    export_seconds: 60 s free, 900 s pro) and its rows are written as CSV, NDJSON or Parquet into object
    storage under the tenant's own prefix, kept 24 hours, or, with destination, delivered to the
    tenant's own bucket (AWS S3, R2, B2, MinIO, ...) by multipart upload and not kept here (its bytes
    count as bytes returned). A plain scan of one namespace exports any number of rows; other shapes up
    to their row cap. Poll GET /v1/sql/exports/{id}; download when done. Limits: exports queued or
    running at once (1 free, 2 pro; 429), exports a UTC day (10 free; 402 export_limit), an export's
    size (1 GB free, 50 GB pro; failed past it). Metered: one query when it runs; downloads as bytes
    returned. A server that restarts fails its running exports (run them again).

    Args:
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Export]
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
    body: ExportRequest,
) -> Error | Export | None:
    """Export a query's answer (beta)

     For answers too big or too slow for a request: the query runs in the background (the plan's
    export_seconds: 60 s free, 900 s pro) and its rows are written as CSV, NDJSON or Parquet into object
    storage under the tenant's own prefix, kept 24 hours, or, with destination, delivered to the
    tenant's own bucket (AWS S3, R2, B2, MinIO, ...) by multipart upload and not kept here (its bytes
    count as bytes returned). A plain scan of one namespace exports any number of rows; other shapes up
    to their row cap. Poll GET /v1/sql/exports/{id}; download when done. Limits: exports queued or
    running at once (1 free, 2 pro; 429), exports a UTC day (10 free; 402 export_limit), an export's
    size (1 GB free, 50 GB pro; failed past it). Metered: one query when it runs; downloads as bytes
    returned. A server that restarts fails its running exports (run them again).

    Args:
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Export
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ExportRequest,
) -> Response[Error | Export]:
    """Export a query's answer (beta)

     For answers too big or too slow for a request: the query runs in the background (the plan's
    export_seconds: 60 s free, 900 s pro) and its rows are written as CSV, NDJSON or Parquet into object
    storage under the tenant's own prefix, kept 24 hours, or, with destination, delivered to the
    tenant's own bucket (AWS S3, R2, B2, MinIO, ...) by multipart upload and not kept here (its bytes
    count as bytes returned). A plain scan of one namespace exports any number of rows; other shapes up
    to their row cap. Poll GET /v1/sql/exports/{id}; download when done. Limits: exports queued or
    running at once (1 free, 2 pro; 429), exports a UTC day (10 free; 402 export_limit), an export's
    size (1 GB free, 50 GB pro; failed past it). Metered: one query when it runs; downloads as bytes
    returned. A server that restarts fails its running exports (run them again).

    Args:
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Export]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ExportRequest,
) -> Error | Export | None:
    """Export a query's answer (beta)

     For answers too big or too slow for a request: the query runs in the background (the plan's
    export_seconds: 60 s free, 900 s pro) and its rows are written as CSV, NDJSON or Parquet into object
    storage under the tenant's own prefix, kept 24 hours, or, with destination, delivered to the
    tenant's own bucket (AWS S3, R2, B2, MinIO, ...) by multipart upload and not kept here (its bytes
    count as bytes returned). A plain scan of one namespace exports any number of rows; other shapes up
    to their row cap. Poll GET /v1/sql/exports/{id}; download when done. Limits: exports queued or
    running at once (1 free, 2 pro; 429), exports a UTC day (10 free; 402 export_limit), an export's
    size (1 GB free, 50 GB pro; failed past it). Metered: one query when it runs; downloads as bytes
    returned. A server that restarts fails its running exports (run them again).

    Args:
        body (ExportRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Export
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
