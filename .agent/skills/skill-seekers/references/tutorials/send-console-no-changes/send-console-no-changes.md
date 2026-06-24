# How To: Send Console No Changes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test send console no changes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `unittest.mock`
- `skill_seekers.sync.notifier`
- `skill_seekers.sync.models`

**Setup Required:**
```python
# Fixtures: capsys
```

## Step-by-Step Guide

### Step 1: Assign report = ChangeReport(...)

```python
report = ChangeReport(skill_name='test-skill', total_pages=5, unchanged=5)
```

**Verification:**
```python
assert 'No changes detected' in captured.out
```

### Step 2: Assign payload = WebhookPayload(...)

```python
payload = WebhookPayload(event='change_detected', skill_name='test-skill', changes=report)
```

### Step 3: Assign n = Notifier(...)

```python
n = Notifier()
```

### Step 4: Call n._send_console()

```python
n._send_console(payload)
```

### Step 5: Assign captured = capsys.readouterr(...)

```python
captured = capsys.readouterr()
```

**Verification:**
```python
assert 'No changes detected' in captured.out
```


## Complete Example

```python
# Setup
# Fixtures: capsys

# Workflow
report = ChangeReport(skill_name='test-skill', total_pages=5, unchanged=5)
payload = WebhookPayload(event='change_detected', skill_name='test-skill', changes=report)
n = Notifier()
n._send_console(payload)
captured = capsys.readouterr()
assert 'No changes detected' in captured.out
```

## Next Steps


---

*Source: test_sync_notifier.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*