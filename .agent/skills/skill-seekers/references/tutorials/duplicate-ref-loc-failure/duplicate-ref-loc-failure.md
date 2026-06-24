# How To: Duplicate Ref Loc Failure

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicate ref loc failure

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

### Step 1: Assign tmp_mgr = create_mgr(...)

```python
tmp_mgr = create_mgr('a:bool; a: f8')
```

### Step 2: Assign unknown = value

```python
axes, blocks = (tmp_mgr.axes, tmp_mgr.blocks)
```

### Step 3: Assign unknown.mgr_locs = BlockPlacement(...)

```python
blocks[0].mgr_locs = BlockPlacement(np.array([0]))
```

### Step 4: Assign unknown.mgr_locs = BlockPlacement(...)

```python
blocks[1].mgr_locs = BlockPlacement(np.array([0]))
```

### Step 5: Assign msg = 'Gaps in blk ref_locs'

```python
msg = 'Gaps in blk ref_locs'
```

### Step 6: Assign unknown.mgr_locs = BlockPlacement(...)

```python
blocks[0].mgr_locs = BlockPlacement(np.array([0]))
```

### Step 7: Assign unknown.mgr_locs = BlockPlacement(...)

```python
blocks[1].mgr_locs = BlockPlacement(np.array([1]))
```

### Step 8: Assign mgr = BlockManager(...)

```python
mgr = BlockManager(blocks, axes)
```

### Step 9: Call mgr.iget()

```python
mgr.iget(1)
```

### Step 10: Assign mgr = BlockManager(...)

```python
mgr = BlockManager(blocks, axes)
```

### Step 11: Call mgr._rebuild_blknos_and_blklocs()

```python
mgr._rebuild_blknos_and_blklocs()
```


## Complete Example

```python
# Workflow
tmp_mgr = create_mgr('a:bool; a: f8')
axes, blocks = (tmp_mgr.axes, tmp_mgr.blocks)
blocks[0].mgr_locs = BlockPlacement(np.array([0]))
blocks[1].mgr_locs = BlockPlacement(np.array([0]))
msg = 'Gaps in blk ref_locs'
with pytest.raises(AssertionError, match=msg):
    mgr = BlockManager(blocks, axes)
    mgr._rebuild_blknos_and_blklocs()
blocks[0].mgr_locs = BlockPlacement(np.array([0]))
blocks[1].mgr_locs = BlockPlacement(np.array([1]))
mgr = BlockManager(blocks, axes)
mgr.iget(1)
```

## Next Steps


---

*Source: test_internals.py:377 | Complexity: Advanced | Last updated: 2026-06-02*