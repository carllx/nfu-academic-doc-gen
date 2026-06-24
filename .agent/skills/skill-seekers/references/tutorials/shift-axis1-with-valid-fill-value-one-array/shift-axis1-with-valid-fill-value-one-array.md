# How To: Shift Axis1 With Valid Fill Value One Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift axis1 with valid fill value one array

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = np.random.default_rng.standard_normal(...)

```python
data = np.random.default_rng(2).standard_normal((5, 3))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 3: Assign res = df.shift(...)

```python
res = df.shift(axis=1, periods=1, fill_value=12345)
```

### Step 4: Assign expected = value

```python
expected = df.T.shift(periods=1, fill_value=12345).T
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 6: Assign df2 = unknown.astype(...)

```python
df2 = df[[0]].astype('Float64')
```

### Step 7: Assign res2 = df2.shift(...)

```python
res2 = df2.shift(axis=1, periods=1, fill_value=12345)
```

### Step 8: Assign expected2 = DataFrame(...)

```python
expected2 = DataFrame([12345] * 5, dtype='Float64')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res2, expected2)
```


## Complete Example

```python
# Workflow
data = np.random.default_rng(2).standard_normal((5, 3))
df = DataFrame(data)
res = df.shift(axis=1, periods=1, fill_value=12345)
expected = df.T.shift(periods=1, fill_value=12345).T
tm.assert_frame_equal(res, expected)
df2 = df[[0]].astype('Float64')
res2 = df2.shift(axis=1, periods=1, fill_value=12345)
expected2 = DataFrame([12345] * 5, dtype='Float64')
tm.assert_frame_equal(res2, expected2)
```

## Next Steps


---

*Source: test_shift.py:20 | Complexity: Advanced | Last updated: 2026-06-02*