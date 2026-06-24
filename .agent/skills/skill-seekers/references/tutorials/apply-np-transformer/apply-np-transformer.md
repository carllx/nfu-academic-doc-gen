# How To: Apply Np Transformer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply np transformer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`

**Setup Required:**
```python
# Fixtures: float_frame, op, how
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
float_frame.iloc[0, 0] = -1.0
```

### Step 2: Assign warn = None

```python
warn = None
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign warn = RuntimeWarning

```python
warn = RuntimeWarning
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(float_frame, how)(op)
```

### Step 6: Assign expected = getattr(...)

```python
expected = getattr(np, op)(float_frame)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, op, how

# Workflow
float_frame.iloc[0, 0] = -1.0
warn = None
if op in ['log', 'sqrt']:
    warn = RuntimeWarning
with tm.assert_produces_warning(warn, check_stacklevel=False):
    result = getattr(float_frame, how)(op)
    expected = getattr(np, op)(float_frame)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_str.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*