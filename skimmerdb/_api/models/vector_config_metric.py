from typing import Literal

VectorConfigMetric = Literal["cosine", "euclidean"]

VECTOR_CONFIG_METRIC_VALUES: set[VectorConfigMetric] = {
    "cosine",
    "euclidean",
}


def check_vector_config_metric(value: str) -> VectorConfigMetric:
    if value in VECTOR_CONFIG_METRIC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VECTOR_CONFIG_METRIC_VALUES!r}"
    )
