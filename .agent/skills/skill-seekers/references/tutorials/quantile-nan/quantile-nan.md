# How To: Quantile Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3, 4, np.nan])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = ser.quantile(...)

```python
result = ser.quantile(0.5)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 3: Assign expected = 2.5

```python
expected = 2.5
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign s1 = Series(...)

```python
s1 = Series([], dtype=object)
```

### Step 5: Assign cases = value

```python
cases = [s1, Series([np.nan, np.nan])]
```

### Step 6: Assign res = ser.quantile(...)

```python
res = ser.quantile(0.5)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 7: Assign res = ser.quantile(...)

```python
res = ser.quantile([0.5])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series([np.nan], index=[0.5]))
```

### Step 9: Assign res = ser.quantile(...)

```python
res = ser.quantile([0.2, 0.3])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series([np.nan, np.nan], index=[0.2, 0.3]))
```


## Complete Example

```python
# Workflow
ser = Series([1, 2, 3, 4, np.nan])
result = ser.quantile(0.5)
expected = 2.5
assert result == expected
s1 = Series([], dtype=object)
cases = [s1, Series([np.nan, np.nan])]
for ser in cases:
    res = ser.quantile(0.5)
    assert np.isnan(res)
    res = ser.quantile([0.5])
    tm.assert_series_equal(res, Series([np.nan], index=[0.5]))
    res = ser.quantile([0.2, 0.3])
    tm.assert_series_equal(res, Series([np.nan, np.nan], index=[0.2, 0.3]))
```

## Next Steps


---

*Source: test_quantile.py:106 | Complexity: Advanced | Last updated: 2026-06-02*