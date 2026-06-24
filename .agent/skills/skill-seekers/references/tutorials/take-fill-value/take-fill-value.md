# How To: Take Fill Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take fill value

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

### Step 2: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, 0, -1]))
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([2, 1, 3], dtype=np.int64, name='xxx')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign msg = 'Unable to fill values because RangeIndex cannot contain NA'

```python
msg = 'Unable to fill values because RangeIndex cannot contain NA'
```

### Step 6: Assign result = idx.take(...)

```python
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index([2, 1, 3], dtype=np.int64, name='xxx')
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign msg = 'Unable to fill values because RangeIndex cannot contain NA'

```python
msg = 'Unable to fill values because RangeIndex cannot contain NA'
```

### Step 10: Call idx.take()

```python
idx.take(np.array([1, 0, -1]), fill_value=True)
```

### Step 11: Call idx.take()

```python
idx.take(np.array([1, 0, -2]), fill_value=True)
```

### Step 12: Call idx.take()

```python
idx.take(np.array([1, 0, -5]), fill_value=True)
```


## Complete Example

```python
# Workflow
idx = RangeIndex(1, 4, name='xxx')
result = idx.take(np.array([1, 0, -1]))
expected = Index([2, 1, 3], dtype=np.int64, name='xxx')
tm.assert_index_equal(result, expected)
msg = 'Unable to fill values because RangeIndex cannot contain NA'
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -1]), fill_value=True)
result = idx.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = Index([2, 1, 3], dtype=np.int64, name='xxx')
tm.assert_index_equal(result, expected)
msg = 'Unable to fill values because RangeIndex cannot contain NA'
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -2]), fill_value=True)
with pytest.raises(ValueError, match=msg):
    idx.take(np.array([1, 0, -5]), fill_value=True)
```

## Next Steps


---

*Source: test_indexing.py:56 | Complexity: Advanced | Last updated: 2026-06-02*