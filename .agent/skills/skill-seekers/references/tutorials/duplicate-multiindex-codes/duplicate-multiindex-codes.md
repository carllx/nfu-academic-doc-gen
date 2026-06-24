# How To: Duplicate Multiindex Codes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicate multiindex codes

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign msg = "Level values must be unique: \\[[A', ]+\\] on level 0"

```python
msg = "Level values must be unique: \\[[A', ]+\\] on level 0"
```

### Step 2: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([['A', 'A', 'B', 'B', 'B'], [1, 2, 1, 2, 3]])
```

### Step 3: Assign msg = "Level values must be unique: \\[[AB', ]+\\] on level 0"

```python
msg = "Level values must be unique: \\[[AB', ]+\\] on level 0"
```

### Step 4: Assign mi = MultiIndex(...)

```python
mi = MultiIndex([['A'] * 10, range(10)], [[0] * 10, range(10)])
```

### Step 5: Call mi.set_levels()

```python
mi.set_levels([['A', 'B', 'A', 'A', 'B'], [2, 1, 3, -2, 5]])
```


## Complete Example

```python
# Workflow
msg = "Level values must be unique: \\[[A', ]+\\] on level 0"
with pytest.raises(ValueError, match=msg):
    mi = MultiIndex([['A'] * 10, range(10)], [[0] * 10, range(10)])
mi = MultiIndex.from_arrays([['A', 'A', 'B', 'B', 'B'], [1, 2, 1, 2, 3]])
msg = "Level values must be unique: \\[[AB', ]+\\] on level 0"
with pytest.raises(ValueError, match=msg):
    mi.set_levels([['A', 'B', 'A', 'A', 'B'], [2, 1, 3, -2, 5]])
```

## Next Steps


---

*Source: test_duplicates.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*