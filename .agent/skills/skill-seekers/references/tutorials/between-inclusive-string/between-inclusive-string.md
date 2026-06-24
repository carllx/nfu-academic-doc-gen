# How To: Between Inclusive String

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between inclusive string

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(date_range('1/1/2000', periods=10))
```

### Step 2: Assign unknown = value

```python
left, right = series[[2, 7]]
```

### Step 3: Assign result = series.between(...)

```python
result = series.between(left, right, inclusive='both')
```

### Step 4: Assign expected = value

```python
expected = (series >= left) & (series <= right)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = series.between(...)

```python
result = series.between(left, right, inclusive='left')
```

### Step 7: Assign expected = value

```python
expected = (series >= left) & (series < right)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = series.between(...)

```python
result = series.between(left, right, inclusive='right')
```

### Step 10: Assign expected = value

```python
expected = (series > left) & (series <= right)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign result = series.between(...)

```python
result = series.between(left, right, inclusive='neither')
```

### Step 13: Assign expected = value

```python
expected = (series > left) & (series < right)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
series = Series(date_range('1/1/2000', periods=10))
left, right = series[[2, 7]]
result = series.between(left, right, inclusive='both')
expected = (series >= left) & (series <= right)
tm.assert_series_equal(result, expected)
result = series.between(left, right, inclusive='left')
expected = (series >= left) & (series < right)
tm.assert_series_equal(result, expected)
result = series.between(left, right, inclusive='right')
expected = (series > left) & (series <= right)
tm.assert_series_equal(result, expected)
result = series.between(left, right, inclusive='neither')
expected = (series > left) & (series < right)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_between.py:41 | Complexity: Advanced | Last updated: 2026-06-02*