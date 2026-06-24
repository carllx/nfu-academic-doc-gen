# How To: Dup Columns Across Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dup columns across dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = [[1, -1, 2.0], [2, -2, 3.0]]
```

### Step 2: Assign rs = DataFrame(...)

```python
rs = DataFrame(vals, columns=['A', 'A', 'B'])
```

### Step 3: Assign xp = DataFrame(...)

```python
xp = DataFrame(vals)
```

### Step 4: Assign xp.columns = value

```python
xp.columns = ['A', 'A', 'B']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(rs, xp)
```


## Complete Example

```python
# Workflow
vals = [[1, -1, 2.0], [2, -2, 3.0]]
rs = DataFrame(vals, columns=['A', 'A', 'B'])
xp = DataFrame(vals)
xp.columns = ['A', 'A', 'B']
tm.assert_frame_equal(rs, xp)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:310 | Complexity: Intermediate | Last updated: 2026-06-02*