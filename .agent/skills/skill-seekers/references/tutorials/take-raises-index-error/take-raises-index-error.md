# How To: Take Raises Index Error

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take raises index error

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(1, 4, name='xxx')
```

### Step 2: Assign msg = 'index -5 is out of bounds for (axis 0 with )?size 3'

```python
msg = 'index -5 is out of bounds for (axis 0 with )?size 3'
```

### Step 3: Assign msg = 'index -4 is out of bounds for (axis 0 with )?size 3'

```python
msg = 'index -4 is out of bounds for (axis 0 with )?size 3'
```

### Step 4: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, -3]))
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([2, 1], dtype=np.int64, name='xxx')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Call idx.take()

```python
idx.take(np.array([1, -5]))
```

### Step 8: Call idx.take()

```python
idx.take(np.array([1, -4]))
```


## Complete Example

```python
# Workflow
idx = RangeIndex(1, 4, name='xxx')
msg = 'index -5 is out of bounds for (axis 0 with )?size 3'
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -5]))
msg = 'index -4 is out of bounds for (axis 0 with )?size 3'
with pytest.raises(IndexError, match=msg):
    idx.take(np.array([1, -4]))
result = idx.take(np.array([1, -3]))
expected = Index([2, 1], dtype=np.int64, name='xxx')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:79 | Complexity: Advanced | Last updated: 2026-06-02*