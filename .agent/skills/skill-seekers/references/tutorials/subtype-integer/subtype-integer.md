# How To: Subtype Integer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subtype integer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index, subtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = IntervalDtype(...)

```python
dtype = IntervalDtype(subtype, 'right')
```

### Step 2: Assign result = index.astype(...)

```python
result = index.astype(dtype)
```

### Step 3: Assign new_left = index.left.astype(...)

```python
new_left = index.left.astype(subtype)
```

### Step 4: Assign new_right = index.right.astype(...)

```python
new_right = index.right.astype(subtype)
```

### Step 5: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays(new_left, new_right, closed=index.closed)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign msg = 'Cannot convert interval\\[(timedelta64|datetime64)\\[ns.*\\], .*\\] to interval\\[uint64, .*\\]'

```python
msg = 'Cannot convert interval\\[(timedelta64|datetime64)\\[ns.*\\], .*\\] to interval\\[uint64, .*\\]'
```

### Step 8: Call index.astype()

```python
index.astype(dtype)
```


## Complete Example

```python
# Setup
# Fixtures: index, subtype

# Workflow
dtype = IntervalDtype(subtype, 'right')
if subtype != 'int64':
    msg = 'Cannot convert interval\\[(timedelta64|datetime64)\\[ns.*\\], .*\\] to interval\\[uint64, .*\\]'
    with pytest.raises(TypeError, match=msg):
        index.astype(dtype)
    return
result = index.astype(dtype)
new_left = index.left.astype(subtype)
new_right = index.right.astype(subtype)
expected = IntervalIndex.from_arrays(new_left, new_right, closed=index.closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:212 | Complexity: Advanced | Last updated: 2026-06-02*