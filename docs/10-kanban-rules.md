# 10. Kanban Operating Rules

## Goal

Task board menjadi durable execution system, bukan daftar to-do pasif.

## Card contract

Substantial card sebaiknya memiliki:

- outcome/objective;
- owner/assignee;
- relevant context;
- constraints;
- definition of done;
- dependencies;
- blocker state;
- result/verification evidence.

## Native dependency semantics matter

Jangan mengasumsikan `parent -> child` berarti project containment. Pada beberapa systems, itu berarti **execution dependency**: parent menunggu child atau child menunggu parent sesuai implementation.

Selalu uji semantics dengan smoke DAG kecil.

## Recommended execution topology

```text
kickoff/spec (optional)
      ↓
parallel specialist work
      ↓
integration / synthesis card owned by outcome owner
      ↓
review / founder gate only if needed
```

## Critical learning

**Continuation harus berupa card/edge yang eksplisit.** Jangan berharap "parent project" otomatis bangun dan mensintesis hanya karena semua child selesai.

## PASS criteria

- specialist fanout bekerja;
- integration card menunggu dependency yang benar;
- owner kembali menerima outcome tanpa manual nudge;
- no orphan execution.
