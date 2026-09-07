# 13. Build Autonomy: Event-Driven First, Scheduled Only When Justified

## Goal

Membuat agent bergerak tanpa founder, tetapi tidak membakar LLM/token setiap beberapa menit dan tidak melakukan perubahan berisiko tanpa authority.

## Two kinds of autonomy

### Event-driven

Gunakan untuk work execution:

```text
task created
→ specialist runs
→ dependency completes
→ synthesis owner wakes
→ owner continues
```

### Time-driven

Gunakan hanya untuk hal yang benar-benar time-based:

- daily hygiene;
- weekly deeper audit;
- scheduled report;
- external condition watch.

Jangan memakai cron untuk mensimulasikan event continuation.

## Monitor-gated pattern

```text
scheduler tick
     ↓
deterministic monitor
     ↓
no change? ── yes ─→ stop before LLM
     │
     no
     ↓
bounded agent inspection
     ↓
meaningful issue?
  ├─ no → silent
  └─ yes → report / safe action within authority
```

## Proven optimization principle

Scheduled LLM jobs sering mahal karena setiap tick memuat context besar. Tambahkan deterministic monitor yang:

- menghasilkan stable normalized snapshot;
- hash output;
- hanya membangunkan agent jika hash berubah;
- memfilter noise historis.

## Safe scheduled contract

Scheduled hygiene sebaiknya:

- read-only by default;
- inspect delta only;
- bounded number of tool calls;
- no full-vault scan;
- no full-log scan;
- no config/project mutation;
- silent when healthy;
- event-driven flow menangani repair bila perlu.

## Verification

Jangan percaya "monitor-gated" sampai dibuktikan:

1. trigger pertama menghasilkan one LLM run;
2. state tidak berubah;
3. trigger berikutnya terjadi;
4. usage log tidak bertambah;
5. scheduler tetap sehat.

## PASS criteria

Unchanged scheduled state = **0 LLM usage**.
