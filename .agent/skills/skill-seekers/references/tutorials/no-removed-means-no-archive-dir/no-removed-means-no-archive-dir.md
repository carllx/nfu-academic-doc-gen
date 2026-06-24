# How To: No Removed Means No Archive Dir

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test no removed means no archive dir

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
assert result.archived == []
```

### Step 2: Assign keep = value

```python
keep = out / 'react.json'
```

**Verification:**
```python
assert not (out / '.archived').exists()
```

### Step 3: Call keep.write_text()

```python
keep.write_text(json.dumps({'name': 'react', 'metadata': {'detected_version': '18.0.0'}}))
```

### Step 4: Assign client = self._client_returning(...)

```python
client = self._client_returning(['react'])
```

**Verification:**
```python
assert result.archived == []
```

### Step 5: Assign result = run_scan(...)

```python
result = run_scan(proj, out, agent_client=client, allow_network=True, allow_generate=False, skip_publish=True, min_confidence=0.4)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
proj, out = self._setup_project(tmp_path)
keep = out / 'react.json'
keep.write_text(json.dumps({'name': 'react', 'metadata': {'detected_version': '18.0.0'}}))
client = self._client_returning(['react'])
with patch('skill_seekers.cli.scan_command.resolve_config_path', return_value=keep):
    result = run_scan(proj, out, agent_client=client, allow_network=True, allow_generate=False, skip_publish=True, min_confidence=0.4)
assert result.archived == []
assert not (out / '.archived').exists()
```

## Next Steps


---

*Source: test_scan_command.py:1089 | Complexity: Intermediate | Last updated: 2026-06-02*