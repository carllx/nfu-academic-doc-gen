# How To: Sort Index Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index level

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
```

### Step 2: Assign s = Series(...)

```python
s = Series([1, 2], mi)
```

### Step 3: Assign backwards = value

```python
backwards = s.iloc[[1, 0]]
```

### Step 4: Assign res = s.sort_index(...)

```python
res = s.sort_index(level='A')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(backwards, res)
```

### Step 6: Assign res = s.sort_index(...)

```python
res = s.sort_index(level=['A', 'B'])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(backwards, res)
```

### Step 8: Assign res = s.sort_index(...)

```python
res = s.sort_index(level='A', sort_remaining=False)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, res)
```

### Step 10: Assign res = s.sort_index(...)

```python
res = s.sort_index(level=['A', 'B'], sort_remaining=False)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, res)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]
res = s.sort_index(level='A')
tm.assert_series_equal(backwards, res)
res = s.sort_index(level=['A', 'B'])
tm.assert_series_equal(backwards, res)
res = s.sort_index(level='A', sort_remaining=False)
tm.assert_series_equal(s, res)
res = s.sort_index(level=['A', 'B'], sort_remaining=False)
tm.assert_series_equal(s, res)
```

## Next Steps


---

*Source: test_sort_index.py:82 | Complexity: Advanced | Last updated: 2026-06-02*