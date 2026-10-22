from typing import Literal

EmbedConfigProvider = Literal["cohere", "gemini", "openai", "skimmerdb", "voyage"]

EMBED_CONFIG_PROVIDER_VALUES: set[EmbedConfigProvider] = {
    "cohere",
    "gemini",
    "openai",
    "skimmerdb",
    "voyage",
}


def check_embed_config_provider(value: str) -> EmbedConfigProvider:
    if value in EMBED_CONFIG_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EMBED_CONFIG_PROVIDER_VALUES!r}"
    )
