# How To: Set Incompatible Types

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set incompatible types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed, op_name, sort
```

## Step-by-Step Guide

### Step 1: Assign index = monotonic_index(...)

```python
index = monotonic_index(0, 11, closed=closed)
```

### Step 2: Assign set_op = getattr(...)

```python
set_op = getattr(index, op_name)
```

### Step 3: Assign result = set_op(...)

```python
result = set_op(Index([1, 2, 3]), sort=sort)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign other = interval_range(...)

```python
other = interval_range(Timestamp('20180101'), periods=9, closed=closed)
```

### Step 6: Assign expected = getattr(...)

```python
expected = getattr(index.astype(object), op_name)(other, sort=sort)
```

### Step 7: Assign result = set_op(...)

```python
result = set_op(other, sort=sort)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign expected = index

```python
expected = index
```

### Step 10: Assign expected = getattr(...)

```python
expected = getattr(index.astype('O'), op_name)(Index([1, 2, 3]))
```

### Step 11: Assign other = monotonic_index(...)

```python
other = monotonic_index(0, 11, closed=other_closed)
```

### Step 12: Assign expected = getattr(...)

```python
expected = getattr(index.astype(object), op_name)(other, sort=sort)
```

### Step 13: Assign result = set_op(...)

```python
result = set_op(other, sort=sort)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 15: Assign expected = index

```python
expected = index
```

### Step 16: Assign expected = index

```python
expected = index
```


## Complete Example

```python
# Setup
# Fixtures: closed, op_name, sort

# Workflow
index = monotonic_index(0, 11, closed=closed)
set_op = getattr(index, op_name)
if op_name == 'difference':
    expected = index
else:
    expected = getattr(index.astype('O'), op_name)(Index([1, 2, 3]))
result = set_op(Index([1, 2, 3]), sort=sort)
tm.assert_index_equal(result, expected)
for other_closed in {'right', 'left', 'both', 'neither'} - {closed}:
    other = monotonic_index(0, 11, closed=other_closed)
    expected = getattr(index.astype(object), op_name)(other, sort=sort)
    if op_name == 'difference':
        expected = index
    result = set_op(other, sort=sort)
    tm.assert_index_equal(result, expected)
other = interval_range(Timestamp('20180101'), periods=9, closed=closed)
expected = getattr(index.astype(object), op_name)(other, sort=sort)
if op_name == 'difference':
    expected = index
result = set_op(other, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:180 | Complexity: Advanced | Last updated: 2026-06-02*