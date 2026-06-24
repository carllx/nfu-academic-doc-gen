# How To: Dragon4 Positional Interface Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dragon4 positional interface overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `platform`
- `pytest`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: tp, pad_val
```

## Step-by-Step Guide

### Step 1: Assign fpos = value

```python
fpos = np.format_float_positional
```

### Step 2: Call pytest.skip()

```python
pytest.skip('Skipping flaky test of float128 on musllinux')
```

### Step 3: Call fpos()

```python
fpos(tp('1.047'), unique=False, precision=pad_val)
```

### Step 4: Call fpos()

```python
fpos(tp('1.047'), precision=2, pad_left=pad_val)
```

### Step 5: Call fpos()

```python
fpos(tp('1.047'), precision=2, pad_right=pad_val)
```


## Complete Example

```python
# Setup
# Fixtures: tp, pad_val

# Workflow
if IS_MUSL and tp == np.float128:
    pytest.skip('Skipping flaky test of float128 on musllinux')
fpos = np.format_float_positional
with pytest.raises(RuntimeError, match='Float formatting result too large'):
    fpos(tp('1.047'), unique=False, precision=pad_val)
with pytest.raises(RuntimeError, match='Float formatting result too large'):
    fpos(tp('1.047'), precision=2, pad_left=pad_val)
with pytest.raises(RuntimeError, match='Float formatting result too large'):
    fpos(tp('1.047'), precision=2, pad_right=pad_val)
```

## Next Steps


---

*Source: test_scalarprint.py:297 | Complexity: Intermediate | Last updated: 2026-06-02*