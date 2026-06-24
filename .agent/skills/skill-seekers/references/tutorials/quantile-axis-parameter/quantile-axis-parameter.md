# How To: Quantile Axis Parameter

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile axis parameter

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: interp_method, request, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign unknown = interp_method

```python
interpolation, method = interp_method
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
```

### Step 3: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=0, interpolation=interpolation, method=method)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([2.0, 3.0], index=['A', 'B'], name=0.5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = df.quantile(...)

```python
expected = df.quantile(0.5, axis='index', interpolation=interpolation, method=method)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis='columns', interpolation=interpolation, method=method)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign msg = 'No axis named -1 for object type DataFrame'

```python
msg = 'No axis named -1 for object type DataFrame'
```

### Step 14: Assign msg = 'No axis named column for object type DataFrame'

```python
msg = 'No axis named column for object type DataFrame'
```

### Step 15: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```

### Step 16: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 17: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 18: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 19: Call df.quantile()

```python
df.quantile(0.1, axis=-1, interpolation=interpolation, method=method)
```

### Step 20: Call df.quantile()

```python
df.quantile(0.1, axis='column')
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=0, interpolation=interpolation, method=method)
expected = Series([2.0, 3.0], index=['A', 'B'], name=0.5)
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)
expected = df.quantile(0.5, axis='index', interpolation=interpolation, method=method)
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)
result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
tm.assert_series_equal(result, expected)
result = df.quantile(0.5, axis='columns', interpolation=interpolation, method=method)
tm.assert_series_equal(result, expected)
msg = 'No axis named -1 for object type DataFrame'
with pytest.raises(ValueError, match=msg):
    df.quantile(0.1, axis=-1, interpolation=interpolation, method=method)
msg = 'No axis named column for object type DataFrame'
with pytest.raises(ValueError, match=msg):
    df.quantile(0.1, axis='column')
```

## Next Steps


---

*Source: test_quantile.py:199 | Complexity: Advanced | Last updated: 2026-06-02*