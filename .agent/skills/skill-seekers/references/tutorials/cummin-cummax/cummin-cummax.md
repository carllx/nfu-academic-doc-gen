# How To: Cummin Cummax

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cummin cummax

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, method
```

## Step-by-Step Guide

### Step 1: Assign ufunc = value

```python
ufunc = methods[method]
```

### Step 2: Assign result = value

```python
result = getattr(datetime_series, method)().values
```

### Step 3: Assign expected = ufunc(...)

```python
expected = ufunc(np.array(datetime_series))
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign ts = datetime_series.copy(...)

```python
ts = datetime_series.copy()
```

### Step 6: Assign unknown = value

```python
ts[::2] = np.nan
```

### Step 7: Assign result = value

```python
result = getattr(ts, method)()[1::2]
```

### Step 8: Assign expected = ufunc(...)

```python
expected = ufunc(ts.dropna())
```

### Step 9: Assign result.index = result.index._with_freq(...)

```python
result.index = result.index._with_freq(None)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, method

# Workflow
ufunc = methods[method]
result = getattr(datetime_series, method)().values
expected = ufunc(np.array(datetime_series))
tm.assert_numpy_array_equal(result, expected)
ts = datetime_series.copy()
ts[::2] = np.nan
result = getattr(ts, method)()[1::2]
expected = ufunc(ts.dropna())
result.index = result.index._with_freq(None)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:44 | Complexity: Advanced | Last updated: 2026-06-02*