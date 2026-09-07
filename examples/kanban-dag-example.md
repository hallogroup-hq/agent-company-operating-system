# Example: Multi-Agent Execution DAG

## Wrong mental model

```text
Project parent
├── Specialist A
└── Specialist B
```

This only works if the task engine truly models containment. Many do not.

## Safer execution model

```text
Specialist A ─┐
              ├→ Integration / Synthesis (Outcome Owner) → Review / Done
Specialist B ─┘
```

The integration card is the continuation point.

## Generic commands

```bash
# Create specialist cards first
A=$(hermes kanban --board example create "Technical audit" --assignee engineering --json)
B=$(hermes kanban --board example create "Market audit" --assignee creative --json)

# Create synthesis card with dependencies according to your engine's semantics.
# Verify native parent/child behavior using --help and a small smoke test.
```
