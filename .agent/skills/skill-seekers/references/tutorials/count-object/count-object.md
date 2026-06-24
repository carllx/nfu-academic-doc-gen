# How To: Count Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test count object

## Prerequisites

**Required Modules:**
- `itertools`
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a'] * 3 + ['b'] * 3, 'c': [2] * 3 + [3] * 3})
```

### Step 2: Assign result = df.groupby.a.count(...)

```python
result = df.groupby('c').a.count()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([3, 3], index=Index([2, 3], name='c'), name='a')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', np.nan, np.nan] + ['b'] * 3, 'c': [2] * 3 + [3] * 3})
```

### Step 6: Assign result = df.groupby.a.count(...)

```python
result = df.groupby('c').a.count()
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([1, 3], index=Index([2, 3], name='c'), name='a')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': ['a'] * 3 + ['b'] * 3, 'c': [2] * 3 + [3] * 3})
result = df.groupby('c').a.count()
expected = Series([3, 3], index=Index([2, 3], name='c'), name='a')
tm.assert_series_equal(result, expected)
df = DataFrame({'a': ['a', np.nan, np.nan] + ['b'] * 3, 'c': [2] * 3 + [3] * 3})
result = df.groupby('c').a.count()
expected = Series([1, 3], index=Index([2, 3], name='c'), name='a')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_counting.py:318 | Complexity: Advanced | Last updated: 2026-06-02*