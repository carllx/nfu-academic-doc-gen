# How To: Emits Expected Shape

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test emits expected shape

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
proj = tmp_path / 'myproj'
```

**Verification:**
```python
assert cfg_path.name == 'myproj-codebase.json'
```

### Step 2: Call proj.mkdir()

```python
proj.mkdir()
```

**Verification:**
```python
assert data['name'] == 'myproj-codebase'
```

### Step 3: Assign out = value

```python
out = tmp_path / 'out'
```

**Verification:**
```python
assert 'sources' in data
```

### Step 4: Call out.mkdir()

```python
out.mkdir()
```

**Verification:**
```python
assert len(data['sources']) == 1
```

### Step 5: Assign cfg_path = emit_codebase_config(...)

```python
cfg_path = emit_codebase_config(proj, out)
```

**Verification:**
```python
assert source['type'] == 'local'
```

### Step 6: Assign data = json.loads(...)

```python
data = json.loads(cfg_path.read_text())
```

**Verification:**
```python
assert source['path'] == str(proj.resolve())
```

### Step 7: Assign source = value

```python
source = data['sources'][0]
```

**Verification:**
```python
assert source.get('include_code') is True
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
proj = tmp_path / 'myproj'
proj.mkdir()
out = tmp_path / 'out'
out.mkdir()
cfg_path = emit_codebase_config(proj, out)
assert cfg_path.name == 'myproj-codebase.json'
data = json.loads(cfg_path.read_text())
assert data['name'] == 'myproj-codebase'
assert 'sources' in data
assert len(data['sources']) == 1
source = data['sources'][0]
assert source['type'] == 'local'
assert source['path'] == str(proj.resolve())
assert source.get('include_code') is True
assert 'file_patterns' in source
assert 'skip_patterns' in source
```

## Next Steps


---

*Source: test_scan_command.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*