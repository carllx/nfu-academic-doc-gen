# How To: Validate Any All Out Keepdims Raises

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test validate any all out keepdims raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: kwargs, func
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2])
```

### Step 2: Assign param = next(...)

```python
param = next(iter(kwargs))
```

### Step 3: Assign name = value

```python
name = func.__name__
```

### Step 4: Assign msg = value

```python
msg = f"the '{param}' parameter is not supported in the pandas implementation of {name}\\(\\)"
```

### Step 5: Call func()

```python
func(ser, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: kwargs, func

# Workflow
ser = Series([1, 2])
param = next(iter(kwargs))
name = func.__name__
msg = f"the '{param}' parameter is not supported in the pandas implementation of {name}\\(\\)"
with pytest.raises(ValueError, match=msg):
    func(ser, **kwargs)
```

## Next Steps


---

*Source: test_reductions.py:117 | Complexity: Intermediate | Last updated: 2026-06-02*