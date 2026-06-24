# How To: Axis

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test axis

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
result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = df.quantile(...)

```python
result = df.quantile([0.5, 0.75], axis=1, interpolation=interpolation, method=method)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({1: [1.5, 1.75], 2: [2.5, 2.75], 3: [3.5, 3.75]}, index=[0.5, 0.75])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_index_type=True)
```

### Step 9: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 10: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```

### Step 11: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation=interpolation, method=method)
expected = Series([1.5, 2.5, 3.5], index=[1, 2, 3], name=0.5)
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_series_equal(result, expected)
result = df.quantile([0.5, 0.75], axis=1, interpolation=interpolation, method=method)
expected = DataFrame({1: [1.5, 1.75], 2: [2.5, 2.75], 3: [3.5, 3.75]}, index=[0.5, 0.75])
if interpolation == 'nearest':
    expected.iloc[0, :] -= 0.5
    expected.iloc[1, :] += 0.25
    expected = expected.astype(np.int64)
tm.assert_frame_equal(result, expected, check_index_type=True)
```

## Next Steps


---

*Source: test_quantile.py:115 | Complexity: Advanced | Last updated: 2026-06-02*