from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bucket_import_request import BucketImportRequest
from ...models.bucket_import_result import BucketImportResult
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: BucketImportRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/{name}/import/bucket".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BucketImportResult | Error | None:
    if response.status_code == 200:
        response_200 = BucketImportResult.from_dict(response.json())

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
) -> Response[BucketImportResult | Error]:
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
    body: BucketImportRequest,
) -> Response[BucketImportResult | Error]:
    """Import files from your bucket

     CSV, NDJSON or Parquet files read straight from your own bucket: AWS S3, or an S3-compatible service
    (Cloudflare R2, Backblaze B2, MinIO, Wasabi, Google Cloud Storage) given as s3.endpoint. One key,
    every file under a prefix, or a pattern (*.parquet), in key order: up to 100 files and 4 GB a
    request, each file up to 2 GB; next says where to go on (pass it as after). Each file is an import
    of its own (all its rows visible together); a failure stops the request and answers what was
    imported, the failing key (failed) and next. The keys are used for this request only, never stored;
    the endpoint's host must resolve to a public address. A namespace that doesn't exist is made (text
    only; created: true). Metered as writes of the documents and the files' bytes.

    Args:
        name (str):
        body (BucketImportRequest): Files in the tenant's bucket to import.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BucketImportResult | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BucketImportRequest,
) -> BucketImportResult | Error | None:
    """Import files from your bucket

     CSV, NDJSON or Parquet files read straight from your own bucket: AWS S3, or an S3-compatible service
    (Cloudflare R2, Backblaze B2, MinIO, Wasabi, Google Cloud Storage) given as s3.endpoint. One key,
    every file under a prefix, or a pattern (*.parquet), in key order: up to 100 files and 4 GB a
    request, each file up to 2 GB; next says where to go on (pass it as after). Each file is an import
    of its own (all its rows visible together); a failure stops the request and answers what was
    imported, the failing key (failed) and next. The keys are used for this request only, never stored;
    the endpoint's host must resolve to a public address. A namespace that doesn't exist is made (text
    only; created: true). Metered as writes of the documents and the files' bytes.

    Args:
        name (str):
        body (BucketImportRequest): Files in the tenant's bucket to import.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BucketImportResult | Error
    """

    return sync_detailed(
        name=name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BucketImportRequest,
) -> Response[BucketImportResult | Error]:
    """Import files from your bucket

     CSV, NDJSON or Parquet files read straight from your own bucket: AWS S3, or an S3-compatible service
    (Cloudflare R2, Backblaze B2, MinIO, Wasabi, Google Cloud Storage) given as s3.endpoint. One key,
    every file under a prefix, or a pattern (*.parquet), in key order: up to 100 files and 4 GB a
    request, each file up to 2 GB; next says where to go on (pass it as after). Each file is an import
    of its own (all its rows visible together); a failure stops the request and answers what was
    imported, the failing key (failed) and next. The keys are used for this request only, never stored;
    the endpoint's host must resolve to a public address. A namespace that doesn't exist is made (text
    only; created: true). Metered as writes of the documents and the files' bytes.

    Args:
        name (str):
        body (BucketImportRequest): Files in the tenant's bucket to import.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BucketImportResult | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BucketImportRequest,
) -> BucketImportResult | Error | None:
    """Import files from your bucket

     CSV, NDJSON or Parquet files read straight from your own bucket: AWS S3, or an S3-compatible service
    (Cloudflare R2, Backblaze B2, MinIO, Wasabi, Google Cloud Storage) given as s3.endpoint. One key,
    every file under a prefix, or a pattern (*.parquet), in key order: up to 100 files and 4 GB a
    request, each file up to 2 GB; next says where to go on (pass it as after). Each file is an import
    of its own (all its rows visible together); a failure stops the request and answers what was
    imported, the failing key (failed) and next. The keys are used for this request only, never stored;
    the endpoint's host must resolve to a public address. A namespace that doesn't exist is made (text
    only; created: true). Metered as writes of the documents and the files' bytes.

    Args:
        name (str):
        body (BucketImportRequest): Files in the tenant's bucket to import.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BucketImportResult | Error
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
