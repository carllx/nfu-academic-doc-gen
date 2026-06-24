# How To: Split

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test split

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

### Step 1: Assign values = np.random.default_rng.standard_normal(...)

```python
values = np.random.default_rng(2).standard_normal((3, 4))
```

**Verification:**
```python
assert (blk.values == -9999).all()
```

### Step 2: Assign blk = new_block(...)

```python
blk = new_block(values, placement=BlockPlacement([3, 1, 6]), ndim=2)
```

**Verification:**
```python
assert len(result) == 3
```

### Step 3: Assign result = blk._split(...)

```python
result = blk._split()
```

**Verification:**
```python
assert_block_equal(res, exp)
```

### Step 4: Assign unknown = value

```python
values[:] = -9999
```

**Verification:**
```python
assert (blk.values == -9999).all()
```

### Step 5: Assign expected = value

```python
expected = [new_block(values[[0]], placement=BlockPlacement([3]), ndim=2), new_block(values[[1]], placement=BlockPlacement([1]), ndim=2), new_block(values[[2]], placement=BlockPlacement([6]), ndim=2)]
```

### Step 6: Call assert_block_equal()

```python
assert_block_equal(res, exp)
```


## Complete Example

```python
# Workflow
values = np.random.default_rng(2).standard_normal((3, 4))
blk = new_block(values, placement=BlockPlacement([3, 1, 6]), ndim=2)
result = blk._split()
values[:] = -9999
assert (blk.values == -9999).all()
assert len(result) == 3
expected = [new_block(values[[0]], placement=BlockPlacement([3]), ndim=2), new_block(values[[1]], placement=BlockPlacement([1]), ndim=2), new_block(values[[2]], placement=BlockPlacement([6]), ndim=2)]
for res, exp in zip(result, expected):
    assert_block_equal(res, exp)
```

## Next Steps


---

*Source: test_internals.py:351 | Complexity: Intermediate | Last updated: 2026-06-02*