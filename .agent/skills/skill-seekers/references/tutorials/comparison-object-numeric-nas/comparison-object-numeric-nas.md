# How To: Comparison Object Numeric Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparison object numeric nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: comparison_op
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).standard_normal(10), dtype=object)
```

### Step 2: Assign shifted = ser.shift(...)

```python
shifted = ser.shift(2)
```

### Step 3: Assign func = comparison_op

```python
func = comparison_op
```

### Step 4: Assign result = func(...)

```python
result = func(ser, shifted)
```

### Step 5: Assign expected = func(...)

```python
expected = func(ser.astype(float), shifted.astype(float))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: comparison_op

# Workflow
ser = Series(np.random.default_rng(2).standard_normal(10), dtype=object)
shifted = ser.shift(2)
func = comparison_op
result = func(ser, shifted)
expected = func(ser.astype(float), shifted.astype(float))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_object.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*