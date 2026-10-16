from typing import Literal

KeyRequestScope = Literal["admin", "read", "write"]

KEY_REQUEST_SCOPE_VALUES: set[KeyRequestScope] = {
    "admin",
    "read",
    "write",
}


def check_key_request_scope(value: str) -> KeyRequestScope:
    if value in KEY_REQUEST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {KEY_REQUEST_SCOPE_VALUES!r}"
    )
