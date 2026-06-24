# How To: Sum Timedelta64 Skipna False

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sum timedelta64 skipna false

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: using_array_manager, request
```

## Step-by-Step Guide

### Step 1: Assign arr = np.arange.astype.view.reshape(...)

```python
arr = np.arange(8).astype(np.int64).view('m8[s]').reshape(4, 2)
```

**Verification:**
```python
assert (df.dtypes == arr.dtype).all()
```

### Step 2: Assign unknown = 'Nat'

```python
arr[-1, -1] = 'Nat'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

**Verification:**
```python
assert (df.dtypes == arr.dtype).all()
```

### Step 4: Assign result = df.sum(...)

```python
result = df.sum(skipna=False)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([pd.Timedelta(seconds=12), pd.NaT], dtype='m8[s]')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = df.sum(...)

```python
result = df.sum(axis=0, skipna=False)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = df.sum(...)

```python
result = df.sum(axis=1, skipna=False)
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([pd.Timedelta(seconds=1), pd.Timedelta(seconds=5), pd.Timedelta(seconds=9), pd.NaT], dtype='m8[s]')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='Incorrect type inference on NaT in reduction result')
```

### Step 13: Call request.applymarker()

```python
request.applymarker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager, request

# Workflow
if using_array_manager:
    mark = pytest.mark.xfail(reason='Incorrect type inference on NaT in reduction result')
    request.applymarker(mark)
arr = np.arange(8).astype(np.int64).view('m8[s]').reshape(4, 2)
arr[-1, -1] = 'Nat'
df = DataFrame(arr)
assert (df.dtypes == arr.dtype).all()
result = df.sum(skipna=False)
expected = Series([pd.Timedelta(seconds=12), pd.NaT], dtype='m8[s]')
tm.assert_series_equal(result, expected)
result = df.sum(axis=0, skipna=False)
tm.assert_series_equal(result, expected)
result = df.sum(axis=1, skipna=False)
expected = Series([pd.Timedelta(seconds=1), pd.Timedelta(seconds=5), pd.Timedelta(seconds=9), pd.NaT], dtype='m8[s]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:1906 | Complexity: Advanced | Last updated: 2026-06-02*