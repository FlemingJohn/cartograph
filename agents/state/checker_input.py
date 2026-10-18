from typing import TypedDict

from agents.state.measurement import Measurement


class CheckerInput(TypedDict):
    measurements: list[Measurement]
