# How To: Float Dtype Ewma

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test float dtype ewma

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func, expected, float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({0: range(5), 1: range(6, 11), 2: range(10, 20, 2)}, dtype=float_numpy_dtype)
```

### Step 2: Assign msg = 'Support for axis=1 in DataFrame.ewm is deprecated'

```python
msg = 'Support for axis=1 in DataFrame.ewm is deprecated'
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(e, func)()
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign e = df.ewm(...)

```python
e = df.ewm(alpha=0.5, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: func, expected, float_numpy_dtype

# Workflow
df = DataFrame({0: range(5), 1: range(6, 11), 2: range(10, 20, 2)}, dtype=float_numpy_dtype)
msg = 'Support for axis=1 in DataFrame.ewm is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    e = df.ewm(alpha=0.5, axis=1)
result = getattr(e, func)()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ewm.py:197 | Complexity: Intermediate | Last updated: 2026-06-02*