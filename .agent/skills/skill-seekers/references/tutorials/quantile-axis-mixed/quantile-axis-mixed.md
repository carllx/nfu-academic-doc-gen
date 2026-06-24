# How To: Quantile Axis Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile axis mixed

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
df = DataFrame({'A': [1, 2, 3], 'B': [2.0, 3.0, 4.0], 'C': pd.date_range('20130101', periods=3), 'D': ['foo', 'bar', 'baz']})
```

### Step 3: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.5, 2.5, 3.5], name=0.5)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = "'<' not supported between instances of 'Timestamp' and 'float'"

```python
msg = "'<' not supported between instances of 'Timestamp' and 'float'"
```

### Step 7: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
```

### Step 8: Call df.quantile()

```python
df.quantile(0.5, axis=1, numeric_only=False)
```


## Complete Example

```python
# Setup
# Fixtures: interp_method, request, using_array_manager

# Workflow
interpolation, method = interp_method
df = DataFrame({'A': [1, 2, 3], 'B': [2.0, 3.0, 4.0], 'C': pd.date_range('20130101', periods=3), 'D': ['foo', 'bar', 'baz']})
result = df.quantile(0.5, axis=1, numeric_only=True, interpolation=interpolation, method=method)
expected = Series([1.5, 2.5, 3.5], name=0.5)
if interpolation == 'nearest':
    expected -= 0.5
if method == 'table' and using_array_manager:
    request.applymarker(pytest.mark.xfail(reason='Axis name incorrectly set.'))
tm.assert_series_equal(result, expected)
msg = "'<' not supported between instances of 'Timestamp' and 'float'"
with pytest.raises(TypeError, match=msg):
    df.quantile(0.5, axis=1, numeric_only=False)
```

## Next Steps


---

*Source: test_quantile.py:173 | Complexity: Advanced | Last updated: 2026-06-02*