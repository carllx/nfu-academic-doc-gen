# How To: Check Document

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check document

## Prerequisites

**Required Modules:**
- `os`
- `textwrap`
- `distutils.command.check`
- `distutils.errors`
- `distutils.tests`
- `pytest`
- `pygments`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('docutils')
```

**Verification:**
```python
assert len(msgs) == 1
```

### Step 2: Assign unknown = self.create_dist(...)

```python
pkg_info, dist = self.create_dist()
```

**Verification:**
```python
assert len(msgs) == 0
```

### Step 3: Assign cmd = check(...)

```python
cmd = check(dist)
```

### Step 4: Assign broken_rest = 'title\n===\n\ntest'

```python
broken_rest = 'title\n===\n\ntest'
```

### Step 5: Assign msgs = cmd._check_rst_data(...)

```python
msgs = cmd._check_rst_data(broken_rest)
```

**Verification:**
```python
assert len(msgs) == 1
```

### Step 6: Assign rest = 'title\n=====\n\ntest'

```python
rest = 'title\n=====\n\ntest'
```

### Step 7: Assign msgs = cmd._check_rst_data(...)

```python
msgs = cmd._check_rst_data(rest)
```

**Verification:**
```python
assert len(msgs) == 0
```


## Complete Example

```python
# Workflow
pytest.importorskip('docutils')
pkg_info, dist = self.create_dist()
cmd = check(dist)
broken_rest = 'title\n===\n\ntest'
msgs = cmd._check_rst_data(broken_rest)
assert len(msgs) == 1
rest = 'title\n=====\n\ntest'
msgs = cmd._check_rst_data(rest)
assert len(msgs) == 0
```

## Next Steps


---

*Source: test_check.py:105 | Complexity: Intermediate | Last updated: 2026-06-02*