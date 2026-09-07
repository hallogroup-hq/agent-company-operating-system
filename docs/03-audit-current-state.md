# 3. Audit the Current State Before Designing More

## Goal

Jangan mendesain sistem berdasarkan asumsi. Audit apa yang benar-benar berjalan.

## Audit surface

Minimal audit:

- agent/profile list;
- configured model + fallback;
- enabled tools;
- gateway/service status;
- workspace/cwd;
- context-file loading rules;
- task board and database path;
- cron jobs;
- shared knowledge storage;
- symlink or mount integrity;
- existing skills;
- existing blocked/stale work.

## Step-by-step

1. Catat version runtime.
2. Catat setiap profile dan default model.
3. Catat tool surface per profile.
4. Verifikasi cwd yang dipakai worker/gateway, bukan hanya shell interaktif.
5. Audit context hierarchy - file mana yang benar-benar dimuat.
6. List board/task state.
7. List cron dan notification subscriptions.
8. List skill directories.
9. Simpan snapshot sebelum perubahan.

## Critical learning

Jangan mengasumsikan config key ada hanya karena namanya masuk akal. Gunakan:

```bash
<tool> --help
<tool> <subcommand> --help
```

Jika config key tidak dikenali, jangan memaksa menulisnya ke state internal.

## PASS criteria

Anda bisa menggambar current architecture dari bukti runtime, bukan dari ingatan.
