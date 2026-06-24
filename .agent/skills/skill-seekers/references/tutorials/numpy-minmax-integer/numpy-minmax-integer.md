# How To: Numpy Minmax Integer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test numpy minmax integer

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

### Step 1: Assign idx = Index(...)

```python
idx = Index([1, 2, 3])
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = idx.values.max(...)

```python
expected = idx.values.max()
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = np.max(...)

```python
result = np.max(idx)
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign expected = idx.values.min(...)

```python
expected = idx.values.min()
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = np.min(...)

```python
result = np.min(idx)
```

**Verification:**
```python
assert result == expected
```

### Step 6: Assign errmsg = "the 'out' parameter is not supported"

```python
errmsg = "the 'out' parameter is not supported"
```

### Step 7: Assign expected = idx.values.argmax(...)

```python
expected = idx.values.argmax()
```

### Step 8: Assign result = np.argmax(...)

```python
result = np.argmax(idx)
```

**Verification:**
```python
assert result == expected
```

### Step 9: Assign expected = idx.values.argmin(...)

```python
expected = idx.values.argmin()
```

### Step 10: Assign result = np.argmin(...)

```python
result = np.argmin(idx)
```

**Verification:**
```python
assert result == expected
```

### Step 11: Assign errmsg = "the 'out' parameter is not supported"

```python
errmsg = "the 'out' parameter is not supported"
```

### Step 12: Call np.min()

```python
np.min(idx, out=0)
```

### Step 13: Call np.max()

```python
np.max(idx, out=0)
```

### Step 14: Call np.argmin()

```python
np.argmin(idx, out=0)
```

### Step 15: Call np.argmax()

```python
np.argmax(idx, out=0)
```


## Complete Example

```python
# Workflow
idx = Index([1, 2, 3])
expected = idx.values.max()
result = np.max(idx)
assert result == expected
expected = idx.values.min()
result = np.min(idx)
assert result == expected
errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.min(idx, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.max(idx, out=0)
expected = idx.values.argmax()
result = np.argmax(idx)
assert result == expected
expected = idx.values.argmin()
result = np.argmin(idx)
assert result == expected
errmsg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=errmsg):
    np.argmin(idx, out=0)
with pytest.raises(ValueError, match=errmsg):
    np.argmax(idx, out=0)
```

## Next Steps


---

*Source: test_reductions.py:437 | Complexity: Advanced | Last updated: 2026-06-02*