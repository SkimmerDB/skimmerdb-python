from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.forgot_password_body import ForgotPasswordBody
from ...models.forgot_password_response_202 import ForgotPasswordResponse202
from ...types import Response


def _get_kwargs(
    *,
    body: ForgotPasswordBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/password/forgot",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ForgotPasswordResponse202 | None:
    if response.status_code == 202:
        response_202 = ForgotPasswordResponse202.from_dict(response.json())

        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ForgotPasswordResponse202]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordBody,
) -> Response[Error | ForgotPasswordResponse202]:
    """Ask for a password reset link

     Emails a reset link (single use, an hour) to the address if it has an account. The answer is the
    same either way.

    Args:
        body (ForgotPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ForgotPasswordResponse202]
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
    body: ForgotPasswordBody,
) -> Error | ForgotPasswordResponse202 | None:
    """Ask for a password reset link

     Emails a reset link (single use, an hour) to the address if it has an account. The answer is the
    same either way.

    Args:
        body (ForgotPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ForgotPasswordResponse202
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordBody,
) -> Response[Error | ForgotPasswordResponse202]:
    """Ask for a password reset link

     Emails a reset link (single use, an hour) to the address if it has an account. The answer is the
    same either way.

    Args:
        body (ForgotPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ForgotPasswordResponse202]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ForgotPasswordBody,
) -> Error | ForgotPasswordResponse202 | None:
    """Ask for a password reset link

     Emails a reset link (single use, an hour) to the address if it has an account. The answer is the
    same either way.

    Args:
        body (ForgotPasswordBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ForgotPasswordResponse202
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
