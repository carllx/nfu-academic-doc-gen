# How To: Setitem Mismatched Closed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem mismatched closed

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = IntervalArray.from_breaks(...)

```python
arr = IntervalArray.from_breaks(range(4))
```

### Step 2: Assign orig = arr.copy(...)

```python
orig = arr.copy()
```

### Step 3: Assign other = arr.set_closed(...)

```python
other = arr.set_closed('both')
```

### Step 4: Assign msg = "'value.closed' is 'both', expected 'right'"

```python
msg = "'value.closed' is 'both', expected 'right'"
```

### Step 5: Assign unknown = value

```python
arr[:0] = []
```

### Step 6: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(arr, orig)
```

### Step 7: Assign unknown = value

```python
arr[0] = other[0]
```

### Step 8: Assign unknown = value

```python
arr[:1] = other[:1]
```

### Step 9: Assign unknown = value

```python
arr[:0] = other[:0]
```

### Step 10: Assign unknown = value

```python
arr[:] = other[::-1]
```

### Step 11: Assign unknown = list(...)

```python
arr[:] = list(other[::-1])
```

### Step 12: Assign unknown = unknown.astype(...)

```python
arr[:] = other[::-1].astype(object)
```

### Step 13: Assign unknown = unknown.astype(...)

```python
arr[:] = other[::-1].astype('category')
```


## Complete Example

```python
# Workflow
arr = IntervalArray.from_breaks(range(4))
orig = arr.copy()
other = arr.set_closed('both')
msg = "'value.closed' is 'both', expected 'right'"
with pytest.raises(ValueError, match=msg):
    arr[0] = other[0]
with pytest.raises(ValueError, match=msg):
    arr[:1] = other[:1]
with pytest.raises(ValueError, match=msg):
    arr[:0] = other[:0]
with pytest.raises(ValueError, match=msg):
    arr[:] = other[::-1]
with pytest.raises(ValueError, match=msg):
    arr[:] = list(other[::-1])
with pytest.raises(ValueError, match=msg):
    arr[:] = other[::-1].astype(object)
with pytest.raises(ValueError, match=msg):
    arr[:] = other[::-1].astype('category')
arr[:0] = []
tm.assert_interval_array_equal(arr, orig)
```

## Next Steps


---

*Source: test_interval.py:143 | Complexity: Advanced | Last updated: 2026-06-02*