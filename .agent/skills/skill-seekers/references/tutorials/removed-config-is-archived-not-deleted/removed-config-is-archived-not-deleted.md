# How To: Removed Config Is Archived Not Deleted

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test removed config is archived not deleted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `json`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.signal_collectors`
- `asyncio`
- `skill_seekers.cli.main`
- `skill_seekers.cli.main`
- `argparse`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.parsers`
- `argparse`
- `skill_seekers.cli.parsers.scan_parser`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`
- `skill_seekers.cli.scan_command`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign unknown = self._setup_project(...)

```python
proj, out = self._setup_project(tmp_path)
```

**Verification:**
```python
assert not stale.exists()
```

### Step 2: Assign stale = value

```python
stale = out / 'moment.json'
```

**Verification:**
```python
assert archived_root.is_dir()
```

### Step 3: Call stale.write_text()

```python
stale.write_text(json.dumps({'name': 'moment', 'metadata': {'detected_version': '2.0.0'}}))
```

**Verification:**
```python
assert len(ts_dirs) == 1
```

### Step 4: Assign keep = value

```python
keep = out / 'react.json'
```

**Verification:**
```python
assert any((f.name == 'moment.json' for f in archived_files))
```

### Step 5: Call keep.write_text()

```python
keep.write_text(json.dumps({'name': 'react', 'metadata': {'detected_version': '18.0.0'}}))
```

**Verification:**
```python
assert len(result.archived) == 1
```

### Step 6: Assign client = self._client_returning(...)

```python
client = self._client_returning(['react'])
```

**Verification:**
```python
assert result.archived[0].name == 'moment.json'
```

### Step 7: Assign archived_root = value

```python
archived_root = out / '.archived'
```

**Verification:**
```python
assert archived_root.is_dir()
```

### Step 8: Assign ts_dirs = list(...)

```python
ts_dirs = list(archived_root.iterdir())
```

**Verification:**
```python
assert len(ts_dirs) == 1
```

### Step 9: Assign archived_files = list(...)

```python
archived_files = list(ts_dirs[0].iterdir())
```

**Verification:**
```python
assert any((f.name == 'moment.json' for f in archived_files))
```

### Step 10: Assign result = run_scan(...)

```python
result = run_scan(proj, out, agent_client=client, allow_network=True, allow_generate=False, skip_publish=True, min_confidence=0.4)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
proj, out = self._setup_project(tmp_path)
stale = out / 'moment.json'
stale.write_text(json.dumps({'name': 'moment', 'metadata': {'detected_version': '2.0.0'}}))
keep = out / 'react.json'
keep.write_text(json.dumps({'name': 'react', 'metadata': {'detected_version': '18.0.0'}}))
client = self._client_returning(['react'])
with patch('skill_seekers.cli.scan_command.resolve_config_path', return_value=keep):
    result = run_scan(proj, out, agent_client=client, allow_network=True, allow_generate=False, skip_publish=True, min_confidence=0.4)
assert not stale.exists()
archived_root = out / '.archived'
assert archived_root.is_dir()
ts_dirs = list(archived_root.iterdir())
assert len(ts_dirs) == 1
archived_files = list(ts_dirs[0].iterdir())
assert any((f.name == 'moment.json' for f in archived_files))
assert len(result.archived) == 1
assert result.archived[0].name == 'moment.json'
```

## Next Steps


---

*Source: test_scan_command.py:1052 | Complexity: Advanced | Last updated: 2026-06-02*