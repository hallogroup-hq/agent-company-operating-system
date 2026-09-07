# Agent Company Operating System

> Kerangka kerja step-by-step untuk membangun tim AI multi-agent yang **punya peran jelas, state yang tahan lama, delegasi yang benar, autonomy yang terkendali, knowledge system bersama, dan execution board yang tidak saling tabrakan**.

**Status:** framework ini disusun dari implementasi yang benar-benar diuji end-to-end pada lingkungan agentic CLI berbasis Hermes Agent. Prinsipnya tool-agnostic, sedangkan contoh command menggunakan primitive Hermes-like. Selalu cek `--help` pada versi yang Anda pakai.

## English summary

This repository is a practical operating system for a small multi-agent AI team. It focuses on role boundaries, authority, durable state, knowledge architecture, task execution, delegation, escalation, autonomy, multi-project isolation, and evidence-based roster growth.

## Kenapa repo ini ada

Banyak implementasi multi-agent berhenti di level "punya beberapa bot". Yang biasanya hilang justru hal-hal yang membuat sebuah tim bisa bekerja secara operasional:

- siapa yang memiliki outcome;
- kapan boleh bertindak tanpa bertanya;
- kapan harus eskalasi;
- di mana truth disimpan;
- bagaimana task bergerak dari masuk sampai selesai;
- bagaimana specialist bekerja tanpa membuat founder menjadi kurir;
- bagaimana autonomy dibuat hemat dan aman;
- bagaimana banyak project tidak saling mencampur konteks;
- kapan *tidak* perlu menambah agent baru.

Framework ini menjawab itu dengan roadmap 15 langkah yang harus diverifikasi, bukan sekadar ditulis.

## Prinsip inti

```text
Identity != Role != Knowledge != Execution != Automation
```

Pisahkan lapisan-lapisan ini:

```text
Protected Identity
       ↓
Role + Authority
       ↓
Shared Knowledge
       ↓
Project Context
       ↓
Execution State
       ↓
Event / Time Triggers
       ↓
Verification + Escalation
```

Formula autonomy yang dipakai:

```text
Authority + State + Trigger + SOP = Autonomy
```

Bukan:

```text
cron + prompt panjang + "jalan sendiri" = autonomy
```

## Roadmap 15 langkah

| # | Langkah | Tujuan |
|---|---|---|
| 1 | Protect identity | Identitas/personality tidak ikut berubah ketika sistem diubah |
| 2 | Define role metadata | Setiap agent punya domain kerja dan routing description |
| 3 | Audit current state | Pahami tool, profile, workspace, model, gateway, dan storage yang benar-benar aktif |
| 4 | Operating model | Tentukan cara perusahaan agent bekerja sebagai satu sistem |
| 5 | Authority matrix | Tentukan yang boleh dikerjakan sendiri vs Founder Gate |
| 6 | Delegation + escalation | Transfer work tanpa kehilangan ownership |
| 7 | Project lifecycle | Definisikan state project/task yang tidak ambigu |
| 8 | Shared knowledge | Pisahkan durable knowledge dari task state dan private memory |
| 9 | Role SOP / skills | Agent punya cara kerja profesi yang konsisten |
| 10 | Kanban operating rules | Execution state punya kontrak yang jelas |
| 11 | Pilot real project | Uji sistem pada pekerjaan nyata, bukan smoke test saja |
| 12 | Refine behavior | Perbaiki semantic mismatch yang ditemukan pilot |
| 13 | Autonomy | Gabungkan event-driven continuation dan monitor-gated scheduled work |
| 14 | Multi-project / multi-venture | Pisahkan project lewat execution boundary yang benar |
| 15 | Roster growth gate | Tambah agent hanya saat bottleneck role benar-benar terbukti |

Dokumentasi lengkap ada di folder [`docs/`](docs/).

## Quick start

Jangan langsung membuat automation. Mulai dari identity dan role boundary.

1. Salin template dari [`templates/`](templates/).
2. Buat backup semua file identity/profile yang sudah ada.
3. Jalankan audit current state.
4. Tulis Operating Model, Authority, Delegation, dan Lifecycle.
5. Buat shared knowledge protocol.
6. Baru setelah itu rapikan Kanban, pilot real project, lalu autonomy.

## Contoh roster kecil

Nama agent tidak penting. Role boundary yang penting. Contoh roster empat fungsi:

```text
Coordinator / Founder Support / PM
Engineering / Technology
Creative / Marketing
System Steward / Agent Operations
```

Empat fungsi ini hanya contoh. Jangan menambah headcount AI karena ingin simetris. Tambah role hanya berdasarkan recurring bottleneck.

## Tool mapping

Framework ini tidak mengharuskan Hermes, tetapi primitive berikut perlu tersedia dalam bentuk apa pun:

| Primitive | Fungsi |
|---|---|
| Profile / agent configuration | identitas model dan tool surface |
| Protected identity context | personality/soul/canon yang tidak mudah tertimpa |
| Shared durable notes | business/project/client truth |
| Durable task board | owner/status/dependency/run/review |
| Delegation | memanggil specialist tanpa founder menjadi messenger |
| Event continuation | task selesai membangunkan owner/synthesizer |
| Scheduled runner | periodic trigger |
| Deterministic monitor | mencegah LLM dipanggil saat tidak ada perubahan |
| Logs / run history | verification dan debugging |

## Hermes-like command examples

Contoh ini sengaja generik. Sesuaikan dengan versi CLI Anda.

```bash
# cek command surface
hermes kanban --help
hermes cron --help

# buat board project terpisah
hermes kanban boards create example-project \
  --name "Example Project"

# explicit routing - jangan bergantung pada global board switch
hermes kanban --board example-project create \
  "Audit technical readiness" \
  --assignee engineering

# lihat state
hermes kanban --board example-project list
```

## Validation rule

Setiap perubahan sistem harus punya bukti:

```text
backup → change → runtime test → verify state → verify protected identity
```

Jangan menutup step sebagai PASS hanya karena file berhasil ditulis.

## Public safety / sanitization

Contoh di repo ini tidak memuat:

- nama agent pribadi;
- token, API key, OAuth secret, password;
- Telegram/chat IDs;
- local username/home path;
- private task IDs;
- private project atau client identifiers.

Gunakan placeholder untuk environment Anda sendiri.

## Isi repo

- `docs/` - 15-step implementation guide + troubleshooting.
- `templates/` - policy/template yang bisa disalin.
- `examples/` - DAG dan deterministic monitor examples.
- `ebook/` - source Markdown untuk ebook companion.
- `SECURITY.md` - aturan sanitasi sebelum open-source.

## Filosofi akhir

Tujuan akhirnya bukan membuat agent sebanyak mungkin. Tujuannya membuat tim kecil yang:

- tahu siapa yang bertanggung jawab;
- bisa bergerak tanpa menunggu founder di setiap langkah;
- tidak kehilangan konteks ketika chat selesai;
- tidak mengubah protected identity ketika operating system berubah;
- tidak membakar token ketika tidak ada perubahan;
- tidak mencampur project yang seharusnya terisolasi;
- bisa membuktikan kapan sistem bekerja dan kapan belum.

Setelah fondasi selesai, berhenti setup tanpa alasan. Masuk ke loop:

```text
USE → OBSERVE → IMPROVE FROM EVIDENCE
```
