# How To: Axis Numeric Only True

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test axis numeric only true

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
df = DataFrame([[1, 2, 3], ['a', 'b', 4]])
```

### Step 3: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([3.0, 4.0], index=[0, 1], name=0.5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.int64)
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
df = DataFrame([[1, 2, 3], ['a', 'b', 4]])
result = df.quantile(0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method)
expected = Series([3.0, 4.0], index=[0, 1], name=0.5)
if interpolation == 'nearest':
    expected = expected.astype(np.int64)
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*