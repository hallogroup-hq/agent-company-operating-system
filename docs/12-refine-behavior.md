# 12. Refine Behavior From Pilot Evidence

## Goal

Perbaiki semantic mismatch yang hanya terlihat setelah real work berjalan.

## Common finding: dependency != containment

Salah satu failure paling umum adalah menganggap native parent/child task relationship sebagai project hierarchy. Padahal task engine mungkin menafsirkannya sebagai dependency DAG.

Solusi:

```text
Conceptual project ownership
!=
Native dependency edge
```

Project ownership tinggal di Project HQ / operating model.
Execution dependency tinggal di task engine.

## Common finding: event delivery has modes

Bedakan:

- notify = passive notification;
- wake = membangunkan agent/session;
- notify+wake = keduanya.

Untuk continuation otomatis, sering kali `wake` lebih tepat daripada notification generik yang noisy.

## Common finding: smoke parser bisa salah meskipun runtime benar

Jangan menyimpulkan system failure dari test harness failure sebelum memeriksa task state/runs langsung.

## Refine loop

```text
observe mismatch
→ inspect native semantics
→ update policy/SOP
→ rerun isolated test
→ preserve history
```

## PASS criteria

Setelah refinement, flow yang sebelumnya butuh manual nudge bisa bergerak sendiri secara deterministic/event-driven.
