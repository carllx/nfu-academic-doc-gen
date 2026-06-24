# How To: Picks Up Github Workflows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test picks up github workflows

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `pathlib`
- `unittest.mock`
- `skill_seekers.cli.signal_collectors`
- `skill_seekers.cli.signal_collectors`
- `skill_seekers.cli.signal_collectors`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign wf_dir = value

```python
wf_dir = tmp_path / '.github' / 'workflows'
```

**Verification:**
```python
assert any((s.path.name == 'ci.yml' for s in signals))
```

### Step 2: Call wf_dir.mkdir()

```python
wf_dir.mkdir(parents=True)
```

### Step 3: Call unknown.write_text()

```python
(wf_dir / 'ci.yml').write_text('name: CI\non: [push]')
```

### Step 4: Assign signals = collect_dockerfile_and_ci(...)

```python
signals = collect_dockerfile_and_ci(tmp_path)
```

**Verification:**
```python
assert any((s.path.name == 'ci.yml' for s in signals))
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
wf_dir = tmp_path / '.github' / 'workflows'
wf_dir.mkdir(parents=True)
(wf_dir / 'ci.yml').write_text('name: CI\non: [push]')
signals = collect_dockerfile_and_ci(tmp_path)
assert any((s.path.name == 'ci.yml' for s in signals))
```

## Next Steps


---

*Source: test_signal_collectors.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*