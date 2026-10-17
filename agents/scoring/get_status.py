from agents.state.finding_status import FindingStatus

LOWEST_SCORE_BY_STATUS: list[tuple[int, FindingStatus]] = [
    (70, "fix_now"),
    (40, "watch"),
    (0, "accept"),
]


def get_status(total: int) -> FindingStatus:
    return next(status for lowest, status in LOWEST_SCORE_BY_STATUS if total >= lowest)
