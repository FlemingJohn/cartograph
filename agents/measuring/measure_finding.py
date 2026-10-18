import asyncio

from agents.measuring.make_cached_tool_caller import CachedToolCaller
from agents.state.finding import Finding
from agents.state.measurement import Measurement


async def measure_finding(call_once: CachedToolCaller, finding: Finding) -> Measurement:
    service = {"service_id": finding["service_id"]}
    techniques = finding["technique_ids"]
    attack_paths, blast_radius, actors_for, *detection_gap = await asyncio.gather(
        call_once("attack_paths", service),
        call_once("blast_radius", service),
        call_once("actors_for", {"technique_ids": techniques}),
        *[
            call_once("detection_gap", {**service, "technique_id": technique})
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
