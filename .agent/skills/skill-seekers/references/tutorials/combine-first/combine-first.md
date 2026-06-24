# How To: Combine First

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign values = np.arange(...)

```python
values = np.arange(20, dtype=np.float64)
```

**Verification:**
```python
assert np.isfinite(combined).all()
```

### Step 2: Assign series = Series(...)

```python
series = Series(values, index=np.arange(20, dtype=np.int64))
```

### Step 3: Assign series_copy = value

```python
series_copy = series * 2
```

### Step 4: Assign unknown = value

```python
series_copy[::2] = np.nan
```

### Step 5: Assign combined = series.combine_first(...)

```python
combined = series.combine_first(series_copy)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(combined, series)
```

### Step 7: Assign combined = series_copy.combine_first(...)

```python
combined = series_copy.combine_first(series)
```

**Verification:**
```python
assert np.isfinite(combined).all()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(combined[::2], series[::2])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(combined[1::2], series_copy[1::2])
```

### Step 10: Assign index = pd.Index(...)

```python
index = pd.Index([str(i) for i in range(20)])
```

### Step 11: Assign floats = Series(...)

```python
floats = Series(np.random.default_rng(2).standard_normal(20), index=index)
```

### Step 12: Assign strings = Series(...)

```python
strings = Series([str(i) for i in range(10)], index=index[::2], dtype=object)
```

### Step 13: Assign combined = strings.combine_first(...)

```python
combined = strings.combine_first(floats)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(strings, combined.loc[index[::2]])
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(floats[1::2].astype(object), combined.loc[index[1::2]])
```

### Step 16: Assign ser = Series(...)

```python
ser = Series([1.0, 2, 3], index=[0, 1, 2])
```

### Step 17: Assign empty = Series(...)

```python
empty = Series([], index=[], dtype=object)
```

### Step 18: Assign msg = 'The behavior of array concatenation with empty entries is deprecated'

```python
msg = 'The behavior of array concatenation with empty entries is deprecated'
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, result)
```

### Step 20: Assign result = ser.combine_first(...)

```python
result = ser.combine_first(empty)
```

### Step 21: Assign ser.index = ser.index.astype(...)

```python
ser.index = ser.index.astype('O')
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
values = np.arange(20, dtype=np.float64)
series = Series(values, index=np.arange(20, dtype=np.int64))
series_copy = series * 2
series_copy[::2] = np.nan
combined = series.combine_first(series_copy)
tm.assert_series_equal(combined, series)
combined = series_copy.combine_first(series)
assert np.isfinite(combined).all()
tm.assert_series_equal(combined[::2], series[::2])
tm.assert_series_equal(combined[1::2], series_copy[1::2])
index = pd.Index([str(i) for i in range(20)])
floats = Series(np.random.default_rng(2).standard_normal(20), index=index)
strings = Series([str(i) for i in range(10)], index=index[::2], dtype=object)
combined = strings.combine_first(floats)
tm.assert_series_equal(strings, combined.loc[index[::2]])
tm.assert_series_equal(floats[1::2].astype(object), combined.loc[index[1::2]])
ser = Series([1.0, 2, 3], index=[0, 1, 2])
empty = Series([], index=[], dtype=object)
msg = 'The behavior of array concatenation with empty entries is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.combine_first(empty)
if not using_infer_string:
    ser.index = ser.index.astype('O')
tm.assert_series_equal(ser, result)
```

## Next Steps


---

*Source: test_combine_first.py:34 | Complexity: Advanced | Last updated: 2026-06-02*