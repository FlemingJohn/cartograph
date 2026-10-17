import asyncio
from collections import defaultdict
from collections.abc import AsyncIterator

from api.steps.agent_step import AgentStep

LAST_STEP_KIND = "finished"


class RunEvents:
    def __init__(self) -> None:
        self.steps_by_scan: dict[str, list[AgentStep]] = defaultdict(list)
        self.arrival = asyncio.Condition()

    async def add(self, step: AgentStep) -> None:
        async with self.arrival:
            self.steps_by_scan[step["scan_id"]].append(step)
            self.arrival.notify_all()

    async def clear(self, scan_id: str) -> None:
        async with self.arrival:
            self.steps_by_scan.pop(scan_id, None)

    async def follow(self, scan_id: str) -> AsyncIterator[AgentStep]:
        position = 0
        has_finished = False
        while not has_finished:
            new_steps = await self.wait_for_steps(scan_id, position)
            position += len(new_steps)
            has_finished = any(step["kind"] == LAST_STEP_KIND for step in new_steps)
            for step in new_steps:
                yield step

    async def wait_for_steps(self, scan_id: str, position: int) -> list[AgentStep]:
        async with self.arrival:
            await self.arrival.wait_for(lambda: len(self.steps_by_scan[scan_id]) > position)
            return self.steps_by_scan[scan_id][position:]
