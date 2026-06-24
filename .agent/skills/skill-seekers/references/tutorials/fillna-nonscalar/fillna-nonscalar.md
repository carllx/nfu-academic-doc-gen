# How To: Fillna Nonscalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna nonscalar

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([np.nan])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([1])
```

### Step 3: Assign result = s1.fillna(...)

```python
result = s1.fillna(s2)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.0])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = s1.fillna(...)

```python
result = s1.fillna({})
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s1)
```

### Step 8: Assign result = s1.fillna(...)

```python
result = s1.fillna(Series((), dtype=object))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s1)
```

### Step 10: Assign result = s2.fillna(...)

```python
result = s2.fillna(s1)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s2)
```

### Step 12: Assign result = s1.fillna(...)

```python
result = s1.fillna({0: 1})
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign result = s1.fillna(...)

```python
result = s1.fillna({1: 1})
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series([np.nan]))
```

### Step 16: Assign result = s1.fillna(...)

```python
result = s1.fillna({0: 1, 1: 1})
```

### Step 17: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 18: Assign result = s1.fillna(...)

```python
result = s1.fillna(Series({0: 1, 1: 1}))
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 20: Assign result = s1.fillna(...)

```python
result = s1.fillna(Series({0: 1, 1: 1}, index=[4, 5]))
```

### Step 21: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s1)
```


## Complete Example

```python
# Workflow
s1 = Series([np.nan])
s2 = Series([1])
result = s1.fillna(s2)
expected = Series([1.0])
tm.assert_series_equal(result, expected)
result = s1.fillna({})
tm.assert_series_equal(result, s1)
result = s1.fillna(Series((), dtype=object))
tm.assert_series_equal(result, s1)
result = s2.fillna(s1)
tm.assert_series_equal(result, s2)
result = s1.fillna({0: 1})
tm.assert_series_equal(result, expected)
result = s1.fillna({1: 1})
tm.assert_series_equal(result, Series([np.nan]))
result = s1.fillna({0: 1, 1: 1})
tm.assert_series_equal(result, expected)
result = s1.fillna(Series({0: 1, 1: 1}))
tm.assert_series_equal(result, expected)
result = s1.fillna(Series({0: 1, 1: 1}, index=[4, 5]))
tm.assert_series_equal(result, s1)
```

## Next Steps


---

*Source: test_fillna.py:96 | Complexity: Advanced | Last updated: 2026-06-02*