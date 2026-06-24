# How To: Bool Operators With Nas

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test bool operators with nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: bool_op
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(bdate_range('1/1/2000', periods=10), dtype=object)
```

### Step 2: Assign unknown = value

```python
ser[::2] = np.nan
```

### Step 3: Assign mask = ser.isna(...)

```python
mask = ser.isna()
```

### Step 4: Assign filled = ser.fillna(...)

```python
filled = ser.fillna(ser[0])
```

### Step 5: Assign result = bool_op(...)

```python
result = bool_op(ser < ser[9], ser > ser[3])
```

### Step 6: Assign expected = bool_op(...)

```python
expected = bool_op(filled < filled[9], filled > filled[3])
```

### Step 7: Assign unknown = False

```python
expected[mask] = False
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: bool_op

# Workflow
ser = Series(bdate_range('1/1/2000', periods=10), dtype=object)
ser[::2] = np.nan
mask = ser.isna()
filled = ser.fillna(ser[0])
result = bool_op(ser < ser[9], ser > ser[3])
expected = bool_op(filled < filled[9], filled > filled[3])
expected[mask] = False
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:24 | Complexity: Advanced | Last updated: 2026-06-02*