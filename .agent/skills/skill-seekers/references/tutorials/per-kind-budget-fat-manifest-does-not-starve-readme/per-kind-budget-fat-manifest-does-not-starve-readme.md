# How To: Per Kind Budget Fat Manifest Does Not Starve Readme

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Regression for WS5: a 50 KB package.json used to consume the entire
64 KB global budget and crowd out README + source samples. Per-kind
budgets guarantee each category gets a slice.

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

### Step 1: 'Regression for WS5: a 50 KB package.json used to consume the entire\n        64 KB global budget and crowd out README + source samples. Per-kind\n        budgets guarantee each category gets a slice.'

```python
'Regression for WS5: a 50 KB package.json used to consume the entire\n        64 KB global budget and crowd out README + source samples. Per-kind\n        budgets guarantee each category gets a slice.'
```

**Verification:**
```python
assert readme_marker in combined, 'README starved by fat manifest'
```

### Step 2: Call unknown.write_text()

```python
(tmp_path / 'package.json').write_text('x' * 50000)
```

**Verification:**
```python
assert src_marker in combined, 'Source sample starved by fat manifest'
```

### Step 3: Assign readme_marker = 'UNIQUE_README_CONTENT_FOR_ASSERTION'

```python
readme_marker = 'UNIQUE_README_CONTENT_FOR_ASSERTION'
```

**Verification:**
```python
assert 'package.json' in {s.path.name for s in bundle.signals}
```

### Step 4: Call unknown.write_text()

```python
(tmp_path / 'README.md').write_text(f'# Project\n\n{readme_marker}\n')
```

### Step 5: Assign src = value

```python
src = tmp_path / 'src'
```

### Step 6: Call src.mkdir()

```python
src.mkdir()
```

### Step 7: Assign src_marker = 'UNIQUE_SOURCE_IMPORT_FOR_ASSERTION'

```python
src_marker = 'UNIQUE_SOURCE_IMPORT_FOR_ASSERTION'
```

### Step 8: Call unknown.write_text()

```python
(src / 'app.py').write_text(f'import {src_marker}\n')
```

### Step 9: Assign bundle = collect_signals(...)

```python
bundle = collect_signals(tmp_path)
```

### Step 10: Assign combined = unknown.join(...)

```python
combined = '\n'.join((s.content for s in bundle.signals))
```

**Verification:**
```python
assert readme_marker in combined, 'README starved by fat manifest'
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
'Regression for WS5: a 50 KB package.json used to consume the entire\n        64 KB global budget and crowd out README + source samples. Per-kind\n        budgets guarantee each category gets a slice.'
(tmp_path / 'package.json').write_text('x' * 50000)
readme_marker = 'UNIQUE_README_CONTENT_FOR_ASSERTION'
(tmp_path / 'README.md').write_text(f'# Project\n\n{readme_marker}\n')
src = tmp_path / 'src'
src.mkdir()
src_marker = 'UNIQUE_SOURCE_IMPORT_FOR_ASSERTION'
(src / 'app.py').write_text(f'import {src_marker}\n')
bundle = collect_signals(tmp_path)
combined = '\n'.join((s.content for s in bundle.signals))
assert readme_marker in combined, 'README starved by fat manifest'
assert src_marker in combined, 'Source sample starved by fat manifest'
assert 'package.json' in {s.path.name for s in bundle.signals}
```

## Next Steps


---

*Source: test_signal_collectors.py:398 | Complexity: Advanced | Last updated: 2026-06-02*