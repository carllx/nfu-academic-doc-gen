# How To: Join Midx String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join midx string

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign midx = MultiIndex.from_arrays(...)

```python
midx = MultiIndex.from_arrays([Series(['a', 'a', 'c'], dtype=StringDtype()), Series(['a', 'b', 'c'], dtype=StringDtype())], names=['a', 'b'])
```

### Step 2: Assign midx2 = MultiIndex.from_arrays(...)

```python
midx2 = MultiIndex.from_arrays([Series(['a'], dtype=StringDtype()), Series(['c'], dtype=StringDtype())], names=['a', 'c'])
```

### Step 3: Assign result = midx.join(...)

```python
result = midx.join(midx2, how='inner')
```

### Step 4: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([Series(['a', 'a'], dtype=StringDtype()), Series(['a', 'b'], dtype=StringDtype()), Series(['c', 'c'], dtype=StringDtype())], names=['a', 'b', 'c'])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
midx = MultiIndex.from_arrays([Series(['a', 'a', 'c'], dtype=StringDtype()), Series(['a', 'b', 'c'], dtype=StringDtype())], names=['a', 'b'])
midx2 = MultiIndex.from_arrays([Series(['a'], dtype=StringDtype()), Series(['c'], dtype=StringDtype())], names=['a', 'c'])
result = midx.join(midx2, how='inner')
expected = MultiIndex.from_arrays([Series(['a', 'a'], dtype=StringDtype()), Series(['a', 'b'], dtype=StringDtype()), Series(['c', 'c'], dtype=StringDtype())], names=['a', 'b', 'c'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:184 | Complexity: Intermediate | Last updated: 2026-06-02*