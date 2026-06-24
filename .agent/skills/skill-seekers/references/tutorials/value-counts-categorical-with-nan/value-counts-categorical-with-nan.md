# How To: Value Counts Categorical With Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts categorical with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['a', 'b', 'a'], dtype='category')
```

### Step 2: Assign exp = Series(...)

```python
exp = Series([2, 1], index=CategoricalIndex(['a', 'b']), name='count')
```

### Step 3: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(dropna=True)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 5: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(dropna=True)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 7: Assign series = value

```python
series = [Series(['a', 'b', None, 'a', None, None], dtype='category'), Series(Categorical(['a', 'b', None, 'a', None, None], categories=['a', 'b']))]
```

### Step 8: Assign exp = Series(...)

```python
exp = Series([2, 1], index=CategoricalIndex(['a', 'b']), name='count')
```

### Step 9: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(dropna=True)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 11: Assign exp = Series(...)

```python
exp = Series([3, 2, 1], index=CategoricalIndex([np.nan, 'a', 'b']), name='count')
```

### Step 12: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(dropna=False)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 14: Assign exp = Series(...)

```python
exp = Series([2, 1, 3], index=CategoricalIndex(['a', 'b', np.nan]), name='count')
```

### Step 15: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(dropna=False, sort=False)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series(['a', 'b', 'a'], dtype='category')
exp = Series([2, 1], index=CategoricalIndex(['a', 'b']), name='count')
res = ser.value_counts(dropna=True)
tm.assert_series_equal(res, exp)
res = ser.value_counts(dropna=True)
tm.assert_series_equal(res, exp)
series = [Series(['a', 'b', None, 'a', None, None], dtype='category'), Series(Categorical(['a', 'b', None, 'a', None, None], categories=['a', 'b']))]
for ser in series:
    exp = Series([2, 1], index=CategoricalIndex(['a', 'b']), name='count')
    res = ser.value_counts(dropna=True)
    tm.assert_series_equal(res, exp)
    exp = Series([3, 2, 1], index=CategoricalIndex([np.nan, 'a', 'b']), name='count')
    res = ser.value_counts(dropna=False)
    tm.assert_series_equal(res, exp)
    exp = Series([2, 1, 3], index=CategoricalIndex(['a', 'b', np.nan]), name='count')
    res = ser.value_counts(dropna=False, sort=False)
    tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_value_counts.py:161 | Complexity: Advanced | Last updated: 2026-06-02*