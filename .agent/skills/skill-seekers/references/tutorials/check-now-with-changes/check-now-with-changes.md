# How To: Check Now With Changes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test check now with changes

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
assert m.state.total_changes == 1
```

### Step 2: Assign old_hash = 'abc123'

```python
old_hash = 'abc123'
```

**Verification:**
```python
assert 'https://example.com/docs' in m.state.page_hashes
```

### Step 3: Assign m = SyncMonitor(...)

```python
m = SyncMonitor(config_path=str(config_path), state_file=str(tmp_path / 'state.json'))
```

### Step 4: Assign m.state.page_hashes = value

```python
m.state.page_hashes = {'https://example.com/docs': old_hash}
```

### Step 5: Call m.check_now()

```python
m.check_now()
```

**Verification:**
```python
assert m.state.total_changes == 1
```


## Complete Example

```python
# Setup
# Fixtures: sample_config

# Workflow
config_path, tmp_path = sample_config
old_hash = 'abc123'
with patch.object(SyncMonitor, '_save_state'):
    m = SyncMonitor(config_path=str(config_path), state_file=str(tmp_path / 'state.json'))
    m.state.page_hashes = {'https://example.com/docs': old_hash}
    with patch.object(m.detector, 'check_pages', return_value=ChangeReport(skill_name='test-skill', total_pages=1, modified=[PageChange(url='https://example.com/docs', change_type=ChangeType.MODIFIED, old_hash=old_hash, new_hash='newhash')])):
        m.check_now()
        assert m.state.total_changes == 1
        assert 'https://example.com/docs' in m.state.page_hashes
```

## Next Steps


---

*Source: test_sync_monitor.py:100 | Complexity: Intermediate | Last updated: 2026-06-02*