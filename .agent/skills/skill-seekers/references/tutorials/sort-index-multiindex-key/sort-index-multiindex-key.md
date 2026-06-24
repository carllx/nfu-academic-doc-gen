# How To: Sort Index Multiindex Key

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index multiindex key

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

### Step 4: Assign result = s.sort_index(...)

```python
result = s.sort_index(level='C', key=lambda x: -x)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, result)
```

### Step 6: Assign result = s.sort_index(...)

```python
result = s.sort_index(level='C', key=lambda x: x)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(backwards, result)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([[1, 1, 3], [1, 1, 1]], names=list('ABC'))
s = Series([1, 2], mi)
backwards = s.iloc[[1, 0]]
result = s.sort_index(level='C', key=lambda x: -x)
tm.assert_series_equal(s, result)
result = s.sort_index(level='C', key=lambda x: x)
tm.assert_series_equal(backwards, result)
```

## Next Steps


---

*Source: test_sort_index.py:219 | Complexity: Intermediate | Last updated: 2026-06-02*