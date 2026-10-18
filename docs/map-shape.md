# Map shape

The FalkorDB graph named by `FALKORDB_GRAPH` (default `cartograph`).

---

## Nodes

| Label | Key fields |
|---|---|
| `Internet` | `id` |
| `Service` | `id`, `name`, `is_internal` |
| `Library` | `id`, `name`, `version` |
| `DataStore` | `id`, `name`, `has_personal_data` |
| `LogSource` | `id`, `name` |
| `Team` | `id`, `name` |
| `Finding` | `id`, `title`, `severity`, `scan_id`, `service_id` |
| `Scan` | `id`, `started_at` |
| `Technique` | `id`, `name`, `tactics` |
| `Actor` | `id`, `name`, `kind` |
| `Mitigation` | `id`, `name` |
| `Detection` | `id`, `name` |
| `Countermeasure` | `name`, `tactic` |
| `TriageDecision` | `id`, `status`, `score`, `reason`, `decided_at` |

---

## Relationships

| Relationship | From | To |
|---|---|---|
| `REACHES` | `Internet` | `Service` |
| `CALLS` | `Service` | `Service` |
| `READS` | `Service` | `DataStore` |
| `USES_LIBRARY` | `Service` | `Library` |
| `WRITES` | `Service` | `LogSource` |
| `OWNS` | `Team` | `Service` |
| `AFFECTS` | `Finding` | `Library` |
| `FOUND_IN` | `Finding` | `Scan` |
| `ENABLES` | `Finding` | `Technique` |
| `SUBTECHNIQUE_OF` | `Technique` | `Technique` |
| `USES` | `Actor` | `Technique` |
| `MITIGATES` | `Mitigation` | `Technique` |
| `DETECTS` | `Detection` | `Technique` |
| `NEEDS_LOG` | `Detection` | `LogSource` |
| `COUNTERS` | `Countermeasure` | `Technique` |
| `ABOUT` | `TriageDecision` | `Finding` |
| `IN_SCAN` | `TriageDecision` | `Scan` |

---

## Indexes

| Label | Indexed field | Type |
|---|---|---|
| `Service` | `id` | exact |
| `Library` | `id` | exact |
| `DataStore` | `id` | exact |
| `Finding` | `id` | exact |
| `Finding` | `scan_id` | exact |
| `Scan` | `id` | exact |
| `Technique` | `id` | exact |
| `Actor` | `id` | exact |
| `Mitigation` | `id` | exact |
| `Detection` | `id` | exact |
| `TriageDecision` | `id` | exact |

---

## Demo invariants

Payments path: `Internet` reaches `web-gateway`, which calls services
leading to `payments-service`, which is two hops from `customer-cards`
(a `DataStore` with `has_personal_data: true`).

Report generator: `report-generator` is a `Service` with `is_internal: true`
and no path from `Internet`.

