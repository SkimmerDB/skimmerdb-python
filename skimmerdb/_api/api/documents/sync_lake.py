from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lake_sync_request import LakeSyncRequest
from ...models.lake_sync_result import LakeSyncResult
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    body: LakeSyncRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/namespaces/{name}/lake/sync".format(
            name=quote(str(name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | LakeSyncResult | None:
    if response.status_code == 200:
        response_200 = LakeSyncResult.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

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
) -> Response[Error | LakeSyncResult]:
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
    body: LakeSyncRequest,
) -> Response[Error | LakeSyncResult]:
    """Sync a DuckLake table

     Keeps a table of your DuckLake (catalog in Postgres, data in your S3 bucket on AWS or an
    S3-compatible service such as R2 or MinIO) in the namespace, nothing copied by you: every live row a
    document (its id the key column's value; its text the text columns; its metadata the other columns
    and _rowid, the DuckLake row id). Each sync reads the catalog at a snapshot and writes only what
    changed since the snapshot synced before (inserts, updates, deletes, inlined rows, compactions); a
    change to the table's columns resyncs it whole. Run it after the lake's commits. The catalog URL and
    S3 keys are used for the sync only and never stored; the catalog's host must resolve to a public
    address. A namespace that doesn't exist is made (text only; created: true). Metered as writes of the
    documents upserted and deleted.

    Args:
        name (str):
        body (LakeSyncRequest): A DuckLake table to keep in the namespace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LakeSyncResult]
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
    body: LakeSyncRequest,
) -> Error | LakeSyncResult | None:
    """Sync a DuckLake table

     Keeps a table of your DuckLake (catalog in Postgres, data in your S3 bucket on AWS or an
    S3-compatible service such as R2 or MinIO) in the namespace, nothing copied by you: every live row a
    document (its id the key column's value; its text the text columns; its metadata the other columns
    and _rowid, the DuckLake row id). Each sync reads the catalog at a snapshot and writes only what
    changed since the snapshot synced before (inserts, updates, deletes, inlined rows, compactions); a
    change to the table's columns resyncs it whole. Run it after the lake's commits. The catalog URL and
    S3 keys are used for the sync only and never stored; the catalog's host must resolve to a public
    address. A namespace that doesn't exist is made (text only; created: true). Metered as writes of the
    documents upserted and deleted.

    Args:
        name (str):
        body (LakeSyncRequest): A DuckLake table to keep in the namespace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LakeSyncResult
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
    body: LakeSyncRequest,
) -> Response[Error | LakeSyncResult]:
    """Sync a DuckLake table

     Keeps a table of your DuckLake (catalog in Postgres, data in your S3 bucket on AWS or an
    S3-compatible service such as R2 or MinIO) in the namespace, nothing copied by you: every live row a
    document (its id the key column's value; its text the text columns; its metadata the other columns
    and _rowid, the DuckLake row id). Each sync reads the catalog at a snapshot and writes only what
    changed since the snapshot synced before (inserts, updates, deletes, inlined rows, compactions); a
    change to the table's columns resyncs it whole. Run it after the lake's commits. The catalog URL and
    S3 keys are used for the sync only and never stored; the catalog's host must resolve to a public
    address. A namespace that doesn't exist is made (text only; created: true). Metered as writes of the
    documents upserted and deleted.

    Args:
        name (str):
        body (LakeSyncRequest): A DuckLake table to keep in the namespace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | LakeSyncResult]
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
    body: LakeSyncRequest,
) -> Error | LakeSyncResult | None:
    """Sync a DuckLake table

     Keeps a table of your DuckLake (catalog in Postgres, data in your S3 bucket on AWS or an
    S3-compatible service such as R2 or MinIO) in the namespace, nothing copied by you: every live row a
    document (its id the key column's value; its text the text columns; its metadata the other columns
    and _rowid, the DuckLake row id). Each sync reads the catalog at a snapshot and writes only what
    changed since the snapshot synced before (inserts, updates, deletes, inlined rows, compactions); a
    change to the table's columns resyncs it whole. Run it after the lake's commits. The catalog URL and
    S3 keys are used for the sync only and never stored; the catalog's host must resolve to a public
    address. A namespace that doesn't exist is made (text only; created: true). Metered as writes of the
    documents upserted and deleted.

    Args:
        name (str):
        body (LakeSyncRequest): A DuckLake table to keep in the namespace.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | LakeSyncResult
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            body=body,
        )
    ).parsed
