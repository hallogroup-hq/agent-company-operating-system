# Troubleshooting and Proven Failure Modes

## 1. "Config key" sounds right but does not exist

**Symptom:** command accepts no such key or silently ignores it.

**Fix:** stop, backup, unset accidental state, inspect `--help`, locate the supported context mechanism.

**Learning:** plausible names are not API contracts.

---

## 2. Context changes do not appear in a running session

**Cause:** context is loaded at session start.

**Fix:** start a fresh session or explicitly reload according to runtime semantics.

---

## 3. Project parent completes before specialist children

**Cause:** native parent/child semantics are execution dependencies, not conceptual containment.

**Fix:** create an explicit downstream integration/synthesis card.

---

## 4. Specialist tasks finish but owner never continues

**Cause:** no event wake/continuation subscription.

**Fix:** configure wake/notify+wake according to desired UX.

---

## 5. Cron costs too many tokens

**Cause:** broad prompt + full context every scheduled run.

**Fix:** deterministic monitor before LLM; inspect only delta; silent when no meaningful issue.

---

## 6. Monitor says "script not found"

**Cause:** scheduled runtime resolves script path relative to profile/runtime home, not the shell path you tested manually.

**Fix:** inspect real runtime resolution and install/copy the monitor where the scheduled profile expects it.

---

## 7. Re-running cron says "already being fired"

**Possible cause:** idempotency/at-most-once guard for the same scheduled instant, not a stuck daemon.

**Fix:** inspect execution DB/run history/fire claim before restarting services or editing DB.

---

## 8. Smoke loop times out although tasks are done

**Cause:** test harness parses the wrong JSON shape.

**Fix:** inspect `show`, run history, or DB state directly. Do not rerun expensive work until runtime state is known.

---

## 9. One global board mixes every project

**Symptom:** task list contains product work, system maintenance, client work, smoke tests, and creative tasks together.

**Fix:** create dedicated execution boards only when workstreams become substantial. Preserve historical cards; route future work forward.

---

## 10. A team wants a fifth agent because one role is slow once

**Fix:** audit median, outliers, blocked reasons, unassigned cards, and routing drift. One long run is not a role bottleneck.
