# How To: Unary Float Op Mask

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary float op mask

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_ea_dtype, op
```

## Step-by-Step Guide

### Step 1: Assign dtype = float_ea_dtype

```python
dtype = float_ea_dtype
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1.1, 2.2, 3.3], dtype=dtype)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(ser, op)()
```

### Step 4: Assign target = result.copy(...)

```python
target = result.copy(deep=True)
```

### Step 5: Assign unknown = None

```python
ser[0] = None
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, target)
```


## Complete Example

```python
# Setup
# Fixtures: float_ea_dtype, op

# Workflow
dtype = float_ea_dtype
ser = Series([1.1, 2.2, 3.3], dtype=dtype)
result = getattr(ser, op)()
target = result.copy(deep=True)
ser[0] = None
tm.assert_series_equal(result, target)
```

## Next Steps


---

*Source: test_unary.py:44 | Complexity: Intermediate | Last updated: 2026-06-02*