# 7. Define a Project / Task Lifecycle

## Goal

Setiap state punya arti operasional yang tidak ambigu.

## Recommended lifecycle

```text
TRIAGE
TODO
SCHEDULED
READY
RUNNING
BLOCKED
REVIEW
DONE
ARCHIVED
```

## Semantics

### TRIAGE
Request substantial tetapi objective/routing/spec belum cukup.

### TODO
Valid work tetapi masih menunggu dependency/prerequisite.

### SCHEDULED
Menunggu waktu, bukan human input.

### READY
Objective, owner, context, constraints, dan reasonable DoD sudah cukup untuk dieksekusi.

### RUNNING
Sedang dikerjakan dan punya owner aktif.

### BLOCKED
Tidak bisa lanjut setelah diagnosis, reasonable attempts, specialist, dan alternative path sudah dicoba.

### REVIEW
Deliverable sudah ada; perlu verification terhadap objective/constraints/DoD.

### DONE
Outcome ada, verification relevan selesai, artifact preserved, handoff jelas, tidak ada obvious next action yang masih menjadi bagian scope.

### ARCHIVED
Inactive/complete/abandoned/superseded dengan history tetap dipertahankan.

## Important rule

Child done != project done.

Project owner tetap harus melakukan integration/synthesis.

## PASS criteria

Dua agent yang melihat task yang sama harus menafsirkan state-nya dengan cara yang sama.
