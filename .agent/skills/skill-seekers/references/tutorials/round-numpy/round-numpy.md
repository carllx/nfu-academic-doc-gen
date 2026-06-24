# How To: Round Numpy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round numpy

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
# Fixtures: any_float_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1.53, 1.36, 0.06], dtype=any_float_dtype)
```

### Step 2: Assign out = np.round(...)

```python
out = np.round(ser, decimals=0)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([2.0, 1.0, 0.0], dtype=any_float_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(out, expected)
```

### Step 5: Assign msg = "the 'out' parameter is not supported"

```python
msg = "the 'out' parameter is not supported"
```

### Step 6: Call np.round()

```python
np.round(ser, decimals=0, out=ser)
```


## Complete Example

```python
# Setup
# Fixtures: any_float_dtype

# Workflow
ser = Series([1.53, 1.36, 0.06], dtype=any_float_dtype)
out = np.round(ser, decimals=0)
expected = Series([2.0, 1.0, 0.0], dtype=any_float_dtype)
tm.assert_series_equal(out, expected)
msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.round(ser, decimals=0, out=ser)
```

## Next Steps


---

*Source: test_round.py:19 | Complexity: Intermediate | Last updated: 2026-06-02*