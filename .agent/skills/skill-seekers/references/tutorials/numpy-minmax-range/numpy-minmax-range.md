# How To: Numpy Minmax Range

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy minmax range

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays.string_arrow`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(0, 10, 3)
```

**Verification:**
```python
assert result == 9
```

### Step 2: Assign result = np.max(...)

```python
result = np.max(idx)
```

**Verification:**
```python
assert result == 0
```

### Step 3: Assign result = np.min(...)

```python
result = np.min(idx)
```

**Verification:**
```python
assert result == 0
```

### Step 4: Assign errmsg = "the 'out' parameter is not supported"

```python
errmsg = "the 'out' parameter is not supported"
```

### Step 5: Call np.min()

```python
np.min(idx, out=0)
```

### Step 6: Call np.max()

```python
np.max(idx, out=0)
```


## Complete Example

```python
# Workflow
idx = RangeIndex(0, 10, 3)
result = np.max(idx)
assert result == 9
result = np.min(idx)
assert result == 0
errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(idx, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.max(idx, out=0)
```

## Next Steps


---

*Source: test_reductions.py:469 | Complexity: Intermediate | Last updated: 2026-06-02*