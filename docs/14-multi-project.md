# 14. Multi-Project / Multi-Venture Architecture

## Goal

Mencegah context bleed, task collision, dan board yang berubah menjadi campuran semua bisnis/project.

## Key model

```text
Shared Knowledge
Business / Venture
└── Client / Brand
    └── Project HQ
        └── execution board slug

Task System
Global/System board
Dedicated project board A
Dedicated project board B
```

## Board is an execution boundary

Board bukan business hierarchy. Ia memisahkan queue, DB, workspace, dan dispatcher/execution surface.

Gunakan global/system board untuk:

- agent-system work;
- cross-project operating-system work;
- global maintenance;
- bounded one-off work yang belum layak punya board sendiri.

Buat dedicated board jika workstream punya independent execution life:

- multiple meaningful tasks;
- survive current conversation;
- multiple roles;
- own backlog/milestone;
- dependency/review loop;
- mixing dengan work lain mengurangi clarity.

## Stable internal slug

Jika public brand/name mungkin berubah, gunakan stable internal execution slug. Jangan mengikat immutable board slug ke naming yang masih eksploratif.

## Explicit routing

Prefer:

```bash
hermes kanban --board example-project ...
```

Daripada mengandalkan remembered global board switch.

## Native project_id warning

Jika task engine punya `project_id`, cek semantics. Pada Hermes-like system, `--project` bisa berarti repository/worktree integration, **bukan conceptual business/project ID**.

Jangan overload field native tanpa memahami semantics.

## Migration rule

Jangan memindahkan completed history hanya untuk kosmetik.

Ketika dedicated board dibuat:

- completed history boleh tetap di board lama;
- in-flight work boleh selesai di tempat asal;
- future substantial work masuk board baru;
- Project HQ mencatat transisi.

## PASS criteria

Runtime smoke task dari beberapa role benar-benar berjalan di dedicated board dan tidak mengubah global board.
