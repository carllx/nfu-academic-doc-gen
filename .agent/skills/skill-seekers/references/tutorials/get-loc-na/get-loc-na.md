# How To: Get Loc Na

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc na

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
idx = Index([np.nan, 1, 2], dtype=np.float64)
```

**Verification:**
```python
assert idx.get_loc(1) == 1
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([np.nan, 1, np.nan], dtype=np.float64)
```

**Verification:**
```python
assert idx.get_loc(np.nan) == 0
```

### Step 3: Assign msg = "'Cannot get left slice bound for non-unique label: nan'"

```python
msg = "'Cannot get left slice bound for non-unique label: nan'"
```

**Verification:**
```python
assert idx.get_loc(1) == 1
```

### Step 4: Assign idx = Index(...)

```python
idx = Index([np.nan, 1, np.nan, np.nan], dtype=np.float64)
```

**Verification:**
```python
assert idx.get_loc(1) == 1
```

### Step 5: Assign msg = "'Cannot get left slice bound for non-unique label: nan"

```python
msg = "'Cannot get left slice bound for non-unique label: nan"
```

### Step 6: Call idx.slice_locs()

```python
idx.slice_locs(np.nan)
```

### Step 7: Call idx.slice_locs()

```python
idx.slice_locs(np.nan)
```


## Complete Example

```python
# Workflow
idx = Index([np.nan, 1, 2], dtype=np.float64)
assert idx.get_loc(1) == 1
assert idx.get_loc(np.nan) == 0
idx = Index([np.nan, 1, np.nan], dtype=np.float64)
assert idx.get_loc(1) == 1
msg = "'Cannot get left slice bound for non-unique label: nan'"
with pytest.raises(KeyError, match=msg):
    idx.slice_locs(np.nan)
idx = Index([np.nan, 1, np.nan, np.nan], dtype=np.float64)
assert idx.get_loc(1) == 1
msg = "'Cannot get left slice bound for non-unique label: nan"
with pytest.raises(KeyError, match=msg):
    idx.slice_locs(np.nan)
```

## Next Steps


---

*Source: test_indexing.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*