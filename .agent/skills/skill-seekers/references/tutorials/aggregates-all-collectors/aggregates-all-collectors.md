# How To: Aggregates All Collectors

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test aggregates all collectors

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

### Step 1: Call unknown.write_text()

```python
(tmp_path / 'package.json').write_text('{"name": "x", "dependencies": {"react": "^18"}}')
```

**Verification:**
```python
assert 'manifest' in kinds
```

### Step 2: Call unknown.write_text()

```python
(tmp_path / 'README.md').write_text('# X\nUses React.')
```

**Verification:**
```python
assert 'readme' in kinds
```

### Step 3: Call unknown.write_text()

```python
(tmp_path / 'Dockerfile').write_text('FROM node:20')
```

**Verification:**
```python
assert 'dockerfile' in kinds
```

### Step 4: Assign src = value

```python
src = tmp_path / 'src'
```

**Verification:**
```python
assert any((s.kind == 'source_sample' for s in bundle.signals))
```

### Step 5: Call src.mkdir()

```python
src.mkdir()
```

**Verification:**
```python
assert bundle.project_name == tmp_path.name
```

### Step 6: Call unknown.write_text()

```python
(src / 'app.js').write_text("import React from 'react';")
```

### Step 7: Assign kinds = value

```python
kinds = {s.kind for s in bundle.signals}
```

**Verification:**
```python
assert 'manifest' in kinds
```

### Step 8: Assign run.return_value.returncode = 0

```python
run.return_value.returncode = 0
```

### Step 9: Assign run.return_value.stdout = ''

```python
run.return_value.stdout = ''
```

### Step 10: Assign bundle = collect_signals(...)

```python
bundle = collect_signals(tmp_path)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
(tmp_path / 'package.json').write_text('{"name": "x", "dependencies": {"react": "^18"}}')
(tmp_path / 'README.md').write_text('# X\nUses React.')
(tmp_path / 'Dockerfile').write_text('FROM node:20')
src = tmp_path / 'src'
src.mkdir()
(src / 'app.js').write_text("import React from 'react';")
with patch('skill_seekers.cli.signal_collectors.subprocess.run') as run:
    run.return_value.returncode = 0
    run.return_value.stdout = ''
    bundle = collect_signals(tmp_path)
kinds = {s.kind for s in bundle.signals}
assert 'manifest' in kinds
assert 'readme' in kinds
assert 'dockerfile' in kinds
assert any((s.kind == 'source_sample' for s in bundle.signals))
assert bundle.project_name == tmp_path.name
```

## Next Steps


---

*Source: test_signal_collectors.py:367 | Complexity: Advanced | Last updated: 2026-06-02*