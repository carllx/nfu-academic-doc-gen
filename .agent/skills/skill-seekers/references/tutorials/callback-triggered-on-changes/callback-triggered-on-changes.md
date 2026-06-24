# How To: Callback Triggered On Changes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test callback triggered on changes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `pytest`
- `unittest.mock`
- `skill_seekers.sync.monitor`
- `skill_seekers.sync.models`

**Setup Required:**
```python
# Fixtures: sample_config
```

## Step-by-Step Guide

### Step 1: Assign unknown = sample_config

```python
config_path, tmp_path = sample_config
```

**Verification:**
```python
assert len(called) == 1
```

### Step 2: Assign called = value

```python
called = []
```

**Verification:**
```python
assert called[0] is mock_change
```

### Step 3: Assign mock_change = ChangeReport(...)

```python
mock_change = ChangeReport(skill_name='test-skill', total_pages=1, modified=[PageChange(url='https://example.com/docs', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')])
```

### Step 4: Call called.append()

```python
called.append(report)
```

### Step 5: Assign m = SyncMonitor(...)

```python
m = SyncMonitor(config_path=str(config_path), state_file=str(tmp_path / 'state.json'), on_change=cb)
```

### Step 6: Call m.check_now()

```python
m.check_now()
```

**Verification:**
```python
assert len(called) == 1
```


## Complete Example

```python
# Setup
# Fixtures: sample_config

# Workflow
config_path, tmp_path = sample_config
called = []

def cb(report):
    called.append(report)
mock_change = ChangeReport(skill_name='test-skill', total_pages=1, modified=[PageChange(url='https://example.com/docs', change_type=ChangeType.MODIFIED, old_hash='a', new_hash='b')])
with patch.object(SyncMonitor, '_save_state'), patch.object(SyncMonitor, '_notify'):
    m = SyncMonitor(config_path=str(config_path), state_file=str(tmp_path / 'state.json'), on_change=cb)
    with patch.object(m.detector, 'check_pages', return_value=mock_change):
        m.check_now()
        assert len(called) == 1
        assert called[0] is mock_change
```

## Next Steps


---

*Source: test_sync_monitor.py:133 | Complexity: Intermediate | Last updated: 2026-06-02*