# Verification Checklist

Use this after each major setup step.

## Before change

- [ ] Identify files/state to touch.
- [ ] Backup.
- [ ] Capture protected identity hashes.
- [ ] Capture task/board counts when relevant.
- [ ] Capture cron/subscription state when relevant.

## During change

- [ ] Modify only intended layer.
- [ ] Avoid direct DB mutation unless no supported interface exists.
- [ ] Prefer managed blocks or idempotent scripts.
- [ ] Do not overwrite identity/canon.

## After change

- [ ] Verify file content.
- [ ] Verify runtime behavior.
- [ ] Verify task/board state.
- [ ] Verify protected hashes unchanged.
- [ ] Verify no accidental public/external action.
- [ ] Record the learning if behavior differed from assumptions.

## Definition of PASS

A step is PASS only if the intended behavior is proven at runtime or through the strongest available deterministic evidence.
