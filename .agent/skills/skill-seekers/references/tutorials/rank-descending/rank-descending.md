# How To: Rank Descending

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank descending

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: ser, results, dtype, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign unknown = results

```python
method, _ = results
```

### Step 2: Assign res = s.rank(...)

```python
res = s.rank(ascending=False)
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected.astype(expected_dtype(dtype, 'average')))
```

### Step 4: Assign res2 = s.rank(...)

```python
res2 = s.rank(method=method, ascending=False)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, expected.astype(expected_dtype(dtype, method)))
```

### Step 6: Assign s = ser.dropna(...)

```python
s = ser.dropna()
```

### Step 7: Assign s = ser.astype(...)

```python
s = ser.astype(dtype)
```

### Step 8: Assign expected = unknown.rank(...)

```python
expected = (s.astype('float64').max() - s.astype('float64')).rank()
```

### Step 9: Assign expected = unknown.rank(...)

```python
expected = (s.max() - s).rank()
```

### Step 10: Assign expected = unknown.rank(...)

```python
expected = (s.astype('float64').max() - s.astype('float64')).rank(method=method)
```

### Step 11: Assign expected = unknown.rank(...)

```python
expected = (s.max() - s).rank(method=method)
```


## Complete Example

```python
# Setup
# Fixtures: ser, results, dtype, using_infer_string

# Workflow
method, _ = results
if dtype == 'int64' or (not using_infer_string and dtype == 'str'):
    s = ser.dropna()
else:
    s = ser.astype(dtype)
res = s.rank(ascending=False)
if dtype.startswith('str'):
    expected = (s.astype('float64').max() - s.astype('float64')).rank()
else:
    expected = (s.max() - s).rank()
tm.assert_series_equal(res, expected.astype(expected_dtype(dtype, 'average')))
if dtype.startswith('str'):
    expected = (s.astype('float64').max() - s.astype('float64')).rank(method=method)
else:
    expected = (s.max() - s).rank(method=method)
res2 = s.rank(method=method, ascending=False)
tm.assert_series_equal(res2, expected.astype(expected_dtype(dtype, method)))
```

## Next Steps


---

*Source: test_rank.py:380 | Complexity: Advanced | Last updated: 2026-06-02*