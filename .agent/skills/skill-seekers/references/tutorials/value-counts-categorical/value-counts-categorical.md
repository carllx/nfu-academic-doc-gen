# How To: Value Counts Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cats = Categorical(...)

```python
cats = Categorical(list('abcccb'), categories=list('cabd'))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(cats, name='xxx')
```

### Step 3: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(sort=False)
```

### Step 4: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(list('cabd'), categories=cats.categories, name='xxx')
```

### Step 5: Assign exp = Series(...)

```python
exp = Series([3, 1, 2, 0], name='count', index=exp_index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 7: Assign res = ser.value_counts(...)

```python
res = ser.value_counts(sort=True)
```

### Step 8: Assign exp_index = CategoricalIndex(...)

```python
exp_index = CategoricalIndex(list('cbad'), categories=cats.categories, name='xxx')
```

### Step 9: Assign exp = Series(...)

```python
exp = Series([3, 2, 1, 0], name='count', index=exp_index)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```

### Step 11: Assign ser = Series(...)

```python
ser = Series(['a', 'b', 'c', 'c', 'c', 'b'], name='xxx')
```

### Step 12: Assign res = ser.value_counts(...)

```python
res = ser.value_counts()
```

### Step 13: Assign exp = Series(...)

```python
exp = Series([3, 2, 1], name='count', index=Index(['c', 'b', 'a'], name='xxx'))
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
cats = Categorical(list('abcccb'), categories=list('cabd'))
ser = Series(cats, name='xxx')
res = ser.value_counts(sort=False)
exp_index = CategoricalIndex(list('cabd'), categories=cats.categories, name='xxx')
exp = Series([3, 1, 2, 0], name='count', index=exp_index)
tm.assert_series_equal(res, exp)
res = ser.value_counts(sort=True)
exp_index = CategoricalIndex(list('cbad'), categories=cats.categories, name='xxx')
exp = Series([3, 2, 1, 0], name='count', index=exp_index)
tm.assert_series_equal(res, exp)
ser = Series(['a', 'b', 'c', 'c', 'c', 'b'], name='xxx')
res = ser.value_counts()
exp = Series([3, 2, 1], name='count', index=Index(['c', 'b', 'a'], name='xxx'))
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_value_counts.py:134 | Complexity: Advanced | Last updated: 2026-06-02*