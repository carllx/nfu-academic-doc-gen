# How To: Bins From Interval Index Doc Example

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bins from interval index doc example

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape.tile`


## Step-by-Step Guide

### Step 1: Assign ages = np.array(...)

```python
ages = np.array([10, 15, 13, 12, 23, 25, 28, 59, 60])
```

### Step 2: Assign c = cut(...)

```python
c = cut(ages, bins=[0, 18, 35, 70])
```

### Step 3: Assign expected = IntervalIndex.from_tuples(...)

```python
expected = IntervalIndex.from_tuples([(0, 18), (18, 35), (35, 70)])
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(c.categories, expected)
```

### Step 5: Assign result = cut(...)

```python
result = cut([25, 20, 50], bins=c.categories)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.categories, expected)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result.codes, np.array([1, 1, 2], dtype='int8'))
```


## Complete Example

```python
# Workflow
ages = np.array([10, 15, 13, 12, 23, 25, 28, 59, 60])
c = cut(ages, bins=[0, 18, 35, 70])
expected = IntervalIndex.from_tuples([(0, 18), (18, 35), (35, 70)])
tm.assert_index_equal(c.categories, expected)
result = cut([25, 20, 50], bins=c.categories)
tm.assert_index_equal(result.categories, expected)
tm.assert_numpy_array_equal(result.codes, np.array([1, 1, 2], dtype='int8'))
```

## Next Steps


---

*Source: test_cut.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*