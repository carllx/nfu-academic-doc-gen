# How To: Interp Limit Forward

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp limit forward

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
s = Series([1, 3, np.nan, np.nan, np.nan, 11])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([1.0, 3.0, 5.0, 7.0, np.nan, 11.0])
```

### Step 3: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='linear', limit=2, limit_direction='forward')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.interpolate(...)

```python
result = s.interpolate(method='linear', limit=2, limit_direction='FORWARD')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([1, 3, np.nan, np.nan, np.nan, 11])
expected = Series([1.0, 3.0, 5.0, 7.0, np.nan, 11.0])
result = s.interpolate(method='linear', limit=2, limit_direction='forward')
tm.assert_series_equal(result, expected)
result = s.interpolate(method='linear', limit=2, limit_direction='FORWARD')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:375 | Complexity: Intermediate | Last updated: 2026-06-02*