# 2. Define Role Metadata and Routing

## Goal

Setiap agent harus bisa dijelaskan dalam 1-3 kalimat: domain apa yang ia miliki, jenis pekerjaan apa yang masuk ke sana, dan apa yang bukan domainnya.

## Example role set

```text
Coordinator
Owns intake, planning, prioritization, coordination, follow-up, stakeholder support.

Engineering
Owns architecture, code, debugging, testing, infrastructure, integrations.

Creative & Marketing
Owns brand, campaigns, content, audience insight, communication, GTM.

System Steward
Owns agent-system health, maintenance, workflow integrity, recovery, knowledge integrity.
```

## Important distinction

Role metadata bukan personality. Jangan menaruh tone, backstory, visual canon, atau relationship canon di sini.

## Step-by-step

1. Tulis satu kalimat "owns" untuk setiap role.
2. Tambahkan 5-10 examples pekerjaan yang jelas masuk.
3. Tambahkan 3-5 examples pekerjaan yang jelas tidak masuk.
4. Pastikan tidak ada dua role yang sama-sama "default owner" untuk domain yang sama.
5. Biarkan cross-functional delegation, tapi jangan biarkan delegation mengaburkan owner.
6. Uji dengan 10 contoh request dan lihat apakah routing konsisten.

## PASS criteria

Untuk sebuah request, tim bisa menentukan:

- recipient;
- owner;
- specialist yang mungkin dibutuhkan;
- decision apa yang harus tetap ke founder.
