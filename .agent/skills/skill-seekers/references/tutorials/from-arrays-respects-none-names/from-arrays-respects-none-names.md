# How To: From Arrays Respects None Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from arrays respects none names

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([1, 2, 3], name='foo')
```

### Step 2: Assign b = Series(...)

```python
b = Series(['a', 'b', 'c'], name='bar')
```

### Step 3: Assign result = MultiIndex.from_arrays(...)

```python
result = MultiIndex.from_arrays([a, b], names=None)
```

### Step 4: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[1, 2, 3], ['a', 'b', 'c']], codes=[[0, 1, 2], [0, 1, 2]], names=None)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = Series([1, 2, 3], name='foo')
b = Series(['a', 'b', 'c'], name='bar')
result = MultiIndex.from_arrays([a, b], names=None)
expected = MultiIndex(levels=[[1, 2, 3], ['a', 'b', 'c']], codes=[[0, 1, 2], [0, 1, 2]], names=None)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:335 | Complexity: Intermediate | Last updated: 2026-06-02*