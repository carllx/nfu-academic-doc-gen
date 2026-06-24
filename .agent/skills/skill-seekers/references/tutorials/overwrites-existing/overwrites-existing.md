# How To: Overwrites Existing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test overwrites existing

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

### Step 1: Assign proj = value

```python
proj = tmp_path / 'p'
```

**Verification:**
```python
assert data['name'] == 'p-codebase'
```

### Step 2: Call proj.mkdir()

```python
proj.mkdir()
```

### Step 3: Assign out = value

```python
out = tmp_path / 'out'
```

### Step 4: Call out.mkdir()

```python
out.mkdir()
```

### Step 5: Assign first = emit_codebase_config(...)

```python
first = emit_codebase_config(proj, out)
```

### Step 6: Call first.write_text()

```python
first.write_text(json.dumps({'name': 'stale'}))
```

### Step 7: Assign second = emit_codebase_config(...)

```python
second = emit_codebase_config(proj, out)
```

### Step 8: Assign data = json.loads(...)

```python
data = json.loads(second.read_text())
```

**Verification:**
```python
assert data['name'] == 'p-codebase'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
proj = tmp_path / 'p'
proj.mkdir()
out = tmp_path / 'out'
out.mkdir()
first = emit_codebase_config(proj, out)
first.write_text(json.dumps({'name': 'stale'}))
second = emit_codebase_config(proj, out)
data = json.loads(second.read_text())
assert data['name'] == 'p-codebase'
```

## Next Steps


---

*Source: test_scan_command.py:106 | Complexity: Advanced | Last updated: 2026-06-02*