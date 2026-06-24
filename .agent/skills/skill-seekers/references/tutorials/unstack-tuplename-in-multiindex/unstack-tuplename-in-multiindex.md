# How To: Unstack Tuplename In Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack tuplename in multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([['a', 'b', 'c'], [1, 2, 3]], names=[('A', 'a'), ('B', 'b')])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(1, index=idx)
```

### Step 3: Assign result = ser.unstack(...)

```python
result = ser.unstack(('A', 'a'))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1, 1], [1, 1, 1], [1, 1, 1]], columns=MultiIndex.from_tuples([('a',), ('b',), ('c',)], names=[('A', 'a')]), index=Index([1, 2, 3], name=('B', 'b')))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_product([['a', 'b', 'c'], [1, 2, 3]], names=[('A', 'a'), ('B', 'b')])
ser = Series(1, index=idx)
result = ser.unstack(('A', 'a'))
expected = DataFrame([[1, 1, 1], [1, 1, 1], [1, 1, 1]], columns=MultiIndex.from_tuples([('a',), ('b',), ('c',)], names=[('A', 'a')]), index=Index([1, 2, 3], name=('B', 'b')))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_unstack.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*