# How To: Check Integrity

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test check integrity

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
locs = []
```

### Step 2: Assign lengths = value

```python
lengths = []
```

### Step 3: Call BlockIndex()

```python
BlockIndex(0, locs, lengths)
```

### Step 4: Call BlockIndex()

```python
BlockIndex(1, locs, lengths)
```

### Step 5: Assign msg = 'Block 0 extends beyond end'

```python
msg = 'Block 0 extends beyond end'
```

### Step 6: Assign msg = 'Block 0 overlaps'

```python
msg = 'Block 0 overlaps'
```

### Step 7: Call BlockIndex()

```python
BlockIndex(10, [5], [10])
```

### Step 8: Call BlockIndex()

```python
BlockIndex(10, [2, 5], [5, 3])
```


## Complete Example

```python
# Workflow
locs = []
lengths = []
BlockIndex(0, locs, lengths)
BlockIndex(1, locs, lengths)
msg = 'Block 0 extends beyond end'
with pytest.raises(ValueError, match=msg):
    BlockIndex(10, [5], [10])
msg = 'Block 0 overlaps'
with pytest.raises(ValueError, match=msg):
    BlockIndex(10, [2, 5], [5, 3])
```

## Next Steps


---

*Source: test_libsparse.py:399 | Complexity: Advanced | Last updated: 2026-06-02*