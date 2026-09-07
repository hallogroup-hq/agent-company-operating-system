# System Map

## The six layers

```text
1. Protected Identity
2. Role + Authority
3. Shared Durable Knowledge
4. Project Context
5. Durable Execution State
6. Triggers + Verification
```

Jika satu layer mencoba mengambil fungsi layer lain, complexity naik.

## Recommended data placement

| Information | Home |
|---|---|
| Personality, soul, character canon | protected identity |
| Role description / routing | role metadata |
| Company operating rules | company policies |
| Reusable workflow | role SOP / skill |
| Business/client/project truth | shared knowledge |
| Current task status | task board |
| Event continuation | task engine / wake |
| Periodic rhythm | scheduler/cron |
| Agent personal learnings | private memory |

## Design test

Untuk setiap informasi, tanyakan:

1. Apakah ini identity?
2. Apakah ini durable organizational truth?
3. Apakah ini procedure?
4. Apakah ini current execution state?
5. Apakah ini trigger?

Jika jawabannya lebih dari satu, boundary mungkin masih kabur.
