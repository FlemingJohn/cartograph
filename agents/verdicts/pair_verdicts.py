from typing import Any

from agents.state.measurement import Measurement


def pair_verdicts(
    measurements: list[Measurement], verdicts: list[Any]
) -> list[tuple[Measurement, Any]]:
    measurement_by_finding = {
        measurement["finding"]["finding_id"]: measurement for measurement in measurements
    }
    return [
        (measurement_by_finding[verdict.finding_id], verdict)
        for verdict in verdicts
        if verdict.finding_id in measurement_by_finding
    ]
