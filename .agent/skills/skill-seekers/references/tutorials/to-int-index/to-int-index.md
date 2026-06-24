# How To: To Int Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to int index

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign locs = value

```python
locs = [0, 10]
```

### Step 2: Assign lengths = value

```python
lengths = [4, 6]
```

### Step 3: Assign exp_inds = value

```python
exp_inds = [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]
```

### Step 4: Assign block = BlockIndex(...)

```python
block = BlockIndex(20, locs, lengths)
```

### Step 5: Assign dense = block.to_int_index(...)

```python
dense = block.to_int_index()
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dense.indices, np.array(exp_inds, dtype=np.int32))
```


## Complete Example

```python
# Workflow
locs = [0, 10]
lengths = [4, 6]
exp_inds = [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]
block = BlockIndex(20, locs, lengths)
dense = block.to_int_index()
tm.assert_numpy_array_equal(dense.indices, np.array(exp_inds, dtype=np.int32))
```

## Next Steps


---

*Source: test_libsparse.py:417 | Complexity: Intermediate | Last updated: 2026-06-02*