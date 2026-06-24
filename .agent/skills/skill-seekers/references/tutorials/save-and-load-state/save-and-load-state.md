# How To: Save And Load State

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test save and load state

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
assert state_file.exists()
```

### Step 2: Assign state_file = value

```python
state_file = tmp_path / 'state.json'
```

**Verification:**
```python
assert loaded_data['total_checks'] == 5
```

### Step 3: Assign m = SyncMonitor(...)

```python
m = SyncMonitor(config_path=str(config_path), state_file=str(state_file))
```

**Verification:**
```python
assert loaded_data['page_hashes']['https://a.com'] == 'abc'
```

### Step 4: Assign m.state.total_checks = 5

```python
m.state.total_checks = 5
```

### Step 5: Assign m.state.page_hashes = value

```python
m.state.page_hashes = {'https://a.com': 'abc'}
```

### Step 6: Call m._save_state()

```python
m._save_state()
```

**Verification:**
```python
assert state_file.exists()
```

### Step 7: Assign loaded_data = json.loads(...)

```python
loaded_data = json.loads(state_file.read_text())
```

**Verification:**
```python
assert loaded_data['total_checks'] == 5
```


## Complete Example

```python
# Setup
# Fixtures: sample_config

# Workflow
config_path, tmp_path = sample_config
state_file = tmp_path / 'state.json'
m = SyncMonitor(config_path=str(config_path), state_file=str(state_file))
m.state.total_checks = 5
m.state.page_hashes = {'https://a.com': 'abc'}
m._save_state()
assert state_file.exists()
loaded_data = json.loads(state_file.read_text())
assert loaded_data['total_checks'] == 5
assert loaded_data['page_hashes']['https://a.com'] == 'abc'
```

## Next Steps


---

*Source: test_sync_monitor.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*