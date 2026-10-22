from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.verify_email_body import VerifyEmailBody
from ...models.verify_email_response_200 import VerifyEmailResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: VerifyEmailBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/email/verify",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | VerifyEmailResponse200 | None:
    if response.status_code == 200:
        response_200 = VerifyEmailResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | VerifyEmailResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyEmailBody,
) -> Response[Error | VerifyEmailResponse200]:
    """Verify an email

     Uses the link a signup's email carries (single use, 7 days; skimmerdb.com/verify-email sends it
    here). Until an owner's email is verified a free tenant gets 1% of the free plan (402
    email_unverified past it); after, all of it.

    Args:
        body (VerifyEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyEmailResponse200]
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
    body: VerifyEmailBody,
) -> Error | VerifyEmailResponse200 | None:
    """Verify an email

     Uses the link a signup's email carries (single use, 7 days; skimmerdb.com/verify-email sends it
    here). Until an owner's email is verified a free tenant gets 1% of the free plan (402
    email_unverified past it); after, all of it.

    Args:
        body (VerifyEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyEmailResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyEmailBody,
) -> Response[Error | VerifyEmailResponse200]:
    """Verify an email

     Uses the link a signup's email carries (single use, 7 days; skimmerdb.com/verify-email sends it
    here). Until an owner's email is verified a free tenant gets 1% of the free plan (402
    email_unverified past it); after, all of it.

    Args:
        body (VerifyEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VerifyEmailResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyEmailBody,
) -> Error | VerifyEmailResponse200 | None:
    """Verify an email

     Uses the link a signup's email carries (single use, 7 days; skimmerdb.com/verify-email sends it
    here). Until an owner's email is verified a free tenant gets 1% of the free plan (402
    email_unverified past it); after, all of it.

    Args:
        body (VerifyEmailBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VerifyEmailResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
