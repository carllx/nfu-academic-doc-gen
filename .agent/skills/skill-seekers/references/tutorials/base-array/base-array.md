# How To: Base Array

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test base array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core.function_base`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: axis
```

## Step-by-Step Guide

### Step 1: Assign start = 1

```python
start = 1
```

**Verification:**
```python
assert_equal(t1, t2)
```

### Step 2: Assign stop = 2

```python
stop = 2
```

### Step 3: Assign num = 6

```python
num = 6
```

### Step 4: Assign base = array(...)

```python
base = array([1, 2])
```

### Step 5: Assign t1 = logspace(...)

```python
t1 = logspace(start, stop, num=num, base=base, axis=axis)
```

### Step 6: Assign t2 = stack(...)

```python
t2 = stack([logspace(start, stop, num=num, base=_base) for _base in base], axis=(axis + 1) % t1.ndim)
```

### Step 7: Call assert_equal()

```python
assert_equal(t1, t2)
```


## Complete Example

```python
# Setup
# Fixtures: axis

# Workflow
start = 1
stop = 2
num = 6
base = array([1, 2])
t1 = logspace(start, stop, num=num, base=base, axis=axis)
t2 = stack([logspace(start, stop, num=num, base=_base) for _base in base], axis=(axis + 1) % t1.ndim)
assert_equal(t1, t2)
```

## Next Steps


---

*Source: test_function_base.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*