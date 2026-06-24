# How To: Interp Unlimited

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp unlimited

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([np.nan, 1.0, 3.0, np.nan, np.nan, np.nan, 11.0, np.nan])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
```

### Step 3: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='linear', limit_direction='both')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.nan, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
```

### Step 6: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='linear', limit_direction='forward')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, np.nan])
```

### Step 9: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='linear', limit_direction='backward')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([np.nan, 1.0, 3.0, np.nan, np.nan, np.nan, 11.0, np.nan])
expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
result = s.interpolate(method='linear', limit_direction='both')
tm.assert_series_equal(result, expected)
expected = Series([np.nan, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, 11.0])
result = s.interpolate(method='linear', limit_direction='forward')
tm.assert_series_equal(result, expected)
expected = Series([1.0, 1.0, 3.0, 5.0, 7.0, 9.0, 11.0, np.nan])
result = s.interpolate(method='linear', limit_direction='backward')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:387 | Complexity: Advanced | Last updated: 2026-06-02*