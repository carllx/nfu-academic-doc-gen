# How To: Mask Return Dtype

**Difficulty**: Advanced
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mask return dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0.0, 1.0, 2.0, 3.0], dtype=Float64Dtype())
```

### Step 2: Assign cond = value

```python
cond = ~ser.isna()
```

### Step 3: Assign other = Series(...)

```python
other = Series([True, False, True, False])
```

### Step 4: Assign excepted = Series(...)

```python
excepted = Series([1.0, 0.0, 1.0, 0.0], dtype=ser.dtype)
```

### Step 5: Assign result = ser.mask(...)

```python
result = ser.mask(cond, other)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, excepted)
```


## Complete Example

```python
# Workflow
ser = Series([0.0, 1.0, 2.0, 3.0], dtype=Float64Dtype())
cond = ~ser.isna()
other = Series([True, False, True, False])
excepted = Series([1.0, 0.0, 1.0, 0.0], dtype=ser.dtype)
result = ser.mask(cond, other)
tm.assert_series_equal(result, excepted)
```

## Next Steps


---

*Source: test_mask.py:136 | Complexity: Advanced | Last updated: 2026-06-02*