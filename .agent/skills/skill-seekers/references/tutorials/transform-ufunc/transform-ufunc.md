# How To: Transform Ufunc

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform ufunc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`
- `pandas.tests.frame.common`

**Setup Required:**
```python
# Fixtures: axis, float_frame, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = unpack_obj(...)

```python
obj = unpack_obj(float_frame, frame_or_series, axis)
```

### Step 2: Assign result = obj.transform(...)

```python
result = obj.transform(np.sqrt, axis=axis)
```

### Step 3: Assign expected = f_sqrt

```python
expected = f_sqrt
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 5: Assign f_sqrt = np.sqrt(...)

```python
f_sqrt = np.sqrt(obj)
```


## Complete Example

```python
# Setup
# Fixtures: axis, float_frame, frame_or_series

# Workflow
obj = unpack_obj(float_frame, frame_or_series, axis)
with np.errstate(all='ignore'):
    f_sqrt = np.sqrt(obj)
result = obj.transform(np.sqrt, axis=axis)
expected = f_sqrt
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_transform.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*