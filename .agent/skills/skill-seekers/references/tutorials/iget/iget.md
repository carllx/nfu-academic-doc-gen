# How To: Iget

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iget

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.internals`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.internals`
- `pandas.core.internals.blocks`


## Step-by-Step Guide

### Step 1: Assign cols = Index(...)

```python
cols = Index(list('abc'))
```

### Step 2: Assign values = np.random.default_rng.random(...)

```python
values = np.random.default_rng(2).random((3, 3))
```

### Step 3: Assign block = new_block(...)

```python
block = new_block(values=values.copy(), placement=BlockPlacement(np.arange(3, dtype=np.intp)), ndim=values.ndim)
```

### Step 4: Assign mgr = BlockManager(...)

```python
mgr = BlockManager(blocks=(block,), axes=[cols, Index(np.arange(3))])
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mgr.iget(0).internal_values(), values[0])
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mgr.iget(1).internal_values(), values[1])
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(mgr.iget(2).internal_values(), values[2])
```


## Complete Example

```python
# Workflow
cols = Index(list('abc'))
values = np.random.default_rng(2).random((3, 3))
block = new_block(values=values.copy(), placement=BlockPlacement(np.arange(3, dtype=np.intp)), ndim=values.ndim)
mgr = BlockManager(blocks=(block,), axes=[cols, Index(np.arange(3))])
tm.assert_almost_equal(mgr.iget(0).internal_values(), values[0])
tm.assert_almost_equal(mgr.iget(1).internal_values(), values[1])
tm.assert_almost_equal(mgr.iget(2).internal_values(), values[2])
```

## Next Steps


---

*Source: test_internals.py:437 | Complexity: Intermediate | Last updated: 2026-06-02*