# How To: Concat Series Axis1 Names Applied

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series axis1 names applied

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1, 2, 3])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6])
```

### Step 3: Assign result = concat(...)

```python
result = concat([s, s2], axis=1, keys=['a', 'b'], names=['A'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=Index(['a', 'b'], name='A'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat([s, s2], axis=1, keys=[('a', 1), ('b', 2)], names=['A', 'B'])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=MultiIndex.from_tuples([('a', 1), ('b', 2)], names=['A', 'B']))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series([1, 2, 3])
s2 = Series([4, 5, 6])
result = concat([s, s2], axis=1, keys=['a', 'b'], names=['A'])
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=Index(['a', 'b'], name='A'))
tm.assert_frame_equal(result, expected)
result = concat([s, s2], axis=1, keys=[('a', 1), ('b', 2)], names=['A', 'B'])
expected = DataFrame([[1, 4], [2, 5], [3, 6]], columns=MultiIndex.from_tuples([('a', 1), ('b', 2)], names=['A', 'B']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:96 | Complexity: Advanced | Last updated: 2026-06-02*