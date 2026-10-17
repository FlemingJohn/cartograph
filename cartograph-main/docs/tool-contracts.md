# Tool contracts

Every tool is served by the MCP server at `tools.make_server`. Every tool
returns the same envelope:

    {
      "result": <the answer>,
      "cypher": "<the query that produced it>",
      "path": [<node ids along the route, empty if none>]
    }

---

## attack_paths

Can the internet reach this service?

| Field | Type | Default |
|---|---|---|
| `service_id` | text | required |
| `max_hops` | integer | 6 |

`result`:

    {
      "is_reachable": true or false,
      "hop_count": integer or null
    }

`path`: the node ids from `Internet` to the service, empty if not reachable.

---

## blast_radius

What sensitive data stores are near this service?

| Field | Type | Default |
|---|---|---|
| `service_id` | text | required |
| `max_hops` | integer | 3 |

`result`:

    [
      {
        "data_store_id": text,
        "has_personal_data": true or false,
        "hop_count": integer
      }
    ]

`path`: empty (multiple paths, no single route).

---

## chokepoints

Which services have the highest betweenness centrality?

| Field | Type | Default |
|---|---|---|
| `limit` | integer | 10 |

`result`:

    [
      {
        "service_id": text,
        "betweenness": float
      }
    ]

`path`: empty.

---

## actors_for

Which threat actors use these techniques?

| Field | Type | Default |
|---|---|---|
| `technique_ids` | list of text | required |
| `limit` | integer | 10 |

`result`:

    {
      "actor_count": integer,
      "actors": [
        {
          "id": text,
          "name": text
        }
      ]
    }

`path`: empty.

---

## detection_gap

Can we detect this technique on this service?

| Field | Type | Default |
|---|---|---|
| `service_id` | text | required |
| `technique_id` | text | required |

`result`:

    {
      "needed_logs": [text],
      "written_logs": [text],
      "missing_logs": [text]
    }

`path`: empty.

---

## record_decision

Save a triage decision to the graph.

| Field | Type | Default |
|---|---|---|
| `finding_id` | text | required |
| `status` | text | required |
| `score` | integer | required |
| `reason` | text | required |
| `evidence_ids` | list of text | required |

`result`:

    {
      "decision_id": text
    }

`path`: empty.

