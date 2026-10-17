import asyncio

from agents.context.app_context import AppContext
from agents.state.finding import Finding
from agents.state.measurement import Measurement
from agents.tools.call_tool import call_tool


async def measure_finding(context: AppContext, finding: Finding) -> Measurement:
    service = {"service_id": finding["service_id"]}
    techniques = finding["technique_ids"]
    attack_paths, blast_radius, actors_for, *detection_gap = await asyncio.gather(
        call_tool(context, "attack_paths", service),
        call_tool(context, "blast_radius", service),
        call_tool(context, "actors_for", {"technique_ids": techniques}),
        *[
            call_tool(context, "detection_gap", {**service, "technique_id": technique})
            for technique in techniques
        ],
    )
    return {
        "finding": finding,
        "attack_paths": attack_paths,
        "blast_radius": blast_radius,
        "actors_for": actors_for,
        "detection_gap": detection_gap,
    }
