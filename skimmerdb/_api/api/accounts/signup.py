from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.signup import Signup
from ...models.signup_request import SignupRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SignupRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/signup",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | Signup | None:
    if response.status_code == 201:
        response_201 = Signup.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Signup]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignupRequest,
) -> Response[Error | Signup]:
    """Sign up

     Makes a person, their first tenant and its first API key (full access, scope admin): the answer's
    key is ready to use and shown only here. Make narrower keys (read or write, some namespaces, caps)
    for apps and agents with POST /v1/keys.

    Args:
        body (SignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
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
    body: SignupRequest,
) -> Error | Signup | None:
    """Sign up

     Makes a person, their first tenant and its first API key (full access, scope admin): the answer's
    key is ready to use and shown only here. Make narrower keys (read or write, some namespaces, caps)
    for apps and agents with POST /v1/keys.

    Args:
        body (SignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SignupRequest,
) -> Response[Error | Signup]:
    """Sign up

     Makes a person, their first tenant and its first API key (full access, scope admin): the answer's
    key is ready to use and shown only here. Make narrower keys (read or write, some namespaces, caps)
    for apps and agents with POST /v1/keys.

    Args:
        body (SignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Signup]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SignupRequest,
) -> Error | Signup | None:
    """Sign up

     Makes a person, their first tenant and its first API key (full access, scope admin): the answer's
    key is ready to use and shown only here. Make narrower keys (read or write, some namespaces, caps)
    for apps and agents with POST /v1/keys.

    Args:
        body (SignupRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Signup
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
