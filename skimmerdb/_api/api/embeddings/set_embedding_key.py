from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embedding_key import EmbeddingKey
from ...models.embedding_key_request import EmbeddingKeyRequest
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    provider: str,
    *,
    body: EmbeddingKeyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/embedding-keys/{provider}".format(
            provider=quote(str(provider), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmbeddingKey | Error | None:
    if response.status_code == 200:
        response_200 = EmbeddingKey.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())

        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EmbeddingKey | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: EmbeddingKeyRequest,
) -> Response[EmbeddingKey | Error]:
    """Store an embedding key

     Stores (or replaces) the tenant's key for a provider (openai, voyage, gemini or cohere), after
    checking it with the provider (one tiny embedding with its default model, billed by the provider).
    Kept encrypted; never shown again. Namespaces with an embedding model (embed) then embed documents'
    text and semantic searches with it; the provider bills the tenant, SkimmerDB counts the tokens
    (usage.embed_tokens) and charges nothing for them. Needs an admin key without namespace limits or
    caps, or the owner's login (as managing API keys).

    Args:
        provider (str):
        body (EmbeddingKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingKey | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: EmbeddingKeyRequest,
) -> EmbeddingKey | Error | None:
    """Store an embedding key

     Stores (or replaces) the tenant's key for a provider (openai, voyage, gemini or cohere), after
    checking it with the provider (one tiny embedding with its default model, billed by the provider).
    Kept encrypted; never shown again. Namespaces with an embedding model (embed) then embed documents'
    text and semantic searches with it; the provider bills the tenant, SkimmerDB counts the tokens
    (usage.embed_tokens) and charges nothing for them. Needs an admin key without namespace limits or
    caps, or the owner's login (as managing API keys).

    Args:
        provider (str):
        body (EmbeddingKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingKey | Error
    """

    return sync_detailed(
        provider=provider,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: EmbeddingKeyRequest,
) -> Response[EmbeddingKey | Error]:
    """Store an embedding key

     Stores (or replaces) the tenant's key for a provider (openai, voyage, gemini or cohere), after
    checking it with the provider (one tiny embedding with its default model, billed by the provider).
    Kept encrypted; never shown again. Namespaces with an embedding model (embed) then embed documents'
    text and semantic searches with it; the provider bills the tenant, SkimmerDB counts the tokens
    (usage.embed_tokens) and charges nothing for them. Needs an admin key without namespace limits or
    caps, or the owner's login (as managing API keys).

    Args:
        provider (str):
        body (EmbeddingKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingKey | Error]
    """

    kwargs = _get_kwargs(
        provider=provider,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: EmbeddingKeyRequest,
) -> EmbeddingKey | Error | None:
    """Store an embedding key

     Stores (or replaces) the tenant's key for a provider (openai, voyage, gemini or cohere), after
    checking it with the provider (one tiny embedding with its default model, billed by the provider).
    Kept encrypted; never shown again. Namespaces with an embedding model (embed) then embed documents'
    text and semantic searches with it; the provider bills the tenant, SkimmerDB counts the tokens
    (usage.embed_tokens) and charges nothing for them. Needs an admin key without namespace limits or
    caps, or the owner's login (as managing API keys).

    Args:
        provider (str):
        body (EmbeddingKeyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingKey | Error
    """

    return (
        await asyncio_detailed(
            provider=provider,
            client=client,
            body=body,
        )
    ).parsed
