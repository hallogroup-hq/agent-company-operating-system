# 1. Protect Identity Before Changing the System

## Goal

Pisahkan **siapa agent itu** dari **bagaimana agent bekerja**. Identity/personality/canon yang sudah disetujui tidak boleh ikut berubah hanya karena Anda sedang mengubah role, routing, board, tool, atau automation.

## Why this comes first

Kesalahan paling mahal dalam setup multi-agent adalah menjadikan satu file sebagai campuran personality, role, company rules, project context, dan automation instructions. Ketika operating system diubah, karakter ikut drift.

Gunakan model lapisan:

```text
Protected identity  → stable
Role metadata       → editable
Company policies    → editable
Skills / SOP        → editable
Project context     → editable
Task state          → highly dynamic
Automation          → dynamic
```

## Step-by-step

1. Inventaris semua file identity/personality/canon.
2. Tandai yang protected.
3. Buat checksum sebelum perubahan besar.
4. Pindahkan operating instructions keluar dari protected identity bila bercampur.
5. Setelah setiap batch perubahan, hitung checksum lagi.
6. Jika hash berubah tanpa sengaja, hentikan rollout dan restore backup.

### Example

```bash
for p in coordinator engineering creative steward; do
  shasum -a 256 "$HOME/.agent/profiles/$p/IDENTITY.md"
done > /tmp/identity-before

# ... operating-system changes ...

for p in coordinator engineering creative steward; do
  shasum -a 256 "$HOME/.agent/profiles/$p/IDENTITY.md"
done > /tmp/identity-after

cmp -s /tmp/identity-before /tmp/identity-after \
  && echo "PASS: identity unchanged" \
  || echo "STOP: protected identity changed"
```

## PASS criteria

- protected files terinventaris;
- backup tersedia;
- hash sebelum/sesudah sama;
- operating instructions tidak lagi harus ditaruh di identity file.

## Learning

**Identity lock bukan sekadar backup.** Ia adalah boundary arsitektur. Jika boundary ini tidak ada, semua step berikutnya lebih berisiko.
