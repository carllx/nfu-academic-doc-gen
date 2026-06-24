# How To: Get Loc Overflows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc overflows

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([0, 2, 1])
```

### Step 2: Assign val = value

```python
val = np.iinfo(np.int64).max + 1
```

### Step 3: Call idx.get_loc()

```python
idx.get_loc(val)
```

### Step 4: Call idx._engine.get_loc()

```python
idx._engine.get_loc(val)
```


## Complete Example

```python
# Workflow
idx = Index([0, 2, 1])
val = np.iinfo(np.int64).max + 1
with pytest.raises(KeyError, match=str(val)):
    idx.get_loc(val)
with pytest.raises(KeyError, match=str(val)):
    idx._engine.get_loc(val)
```

## Next Steps


---

*Source: test_indexing.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*