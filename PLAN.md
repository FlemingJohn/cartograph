# Plan

Deadline: Oct 18, 2026, 11:59 PM GMT+5:30. Submit by 11 PM.

## Who owns what

| Alan: data and tools | Iesvs: agents and app |
|---|---|
| `graph/`, `tools/` | `agents/`, `api/`, `web/` |

The only link between the two halves is the tool contract in
`docs/tool-contracts.md`. Iesvs builds against `agents/fakes/` until the real
tools are ready.

## Oct 17

- Together: agree `docs/map-shape.md`, `docs/tool-contracts.md`,
  `docs/state-shape.md`
- Alan: connect to FalkorDB Cloud, load MITRE data, make the company and a
  sample scan, test the graph functions, build the six tools
- Iesvs: coordinator and three checkers with fakes, scoring, approval pause,
  save points, backend streaming
- Together at night: swap fakes for real tools, run once end to end

## Oct 18

- Alan: `record_decision`, the simulation rerun, README, deploy backend,
  blog post
- Iesvs: dashboard, approval panel, deploy frontend, demo video
- Midday: feature freeze
- 11 PM: submit

## Kept small to fit the time

- Reporter merged into the coordinator
- Tickets go to a mock list
- Replay shown in the terminal, not a screen
- Six tools on our server: `attack_paths`, `blast_radius`, `chokepoints`,
  `actors_for`, `detection_gap`, `record_decision`
