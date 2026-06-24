# How To: Difference

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed, sort
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_arrays(...)

```python
index = IntervalIndex.from_arrays([1, 0, 3, 2], [1, 2, 3, 4], closed=closed)
```

### Step 2: Assign result = index.difference(...)

```python
result = index.difference(index[:1], sort=sort)
```

### Step 3: Assign expected = value

```python
expected = index[1:]
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = index.difference(...)

```python
result = index.difference(index, sort=sort)
```

### Step 6: Assign expected = empty_index(...)

```python
expected = empty_index(dtype='int64', closed=closed)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign other = IntervalIndex.from_arrays(...)

```python
other = IntervalIndex.from_arrays(index.left.astype('float64'), index.right, closed=closed)
```

### Step 9: Assign result = index.difference(...)

```python
result = index.difference(other, sort=sort)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 11: Assign expected = expected.sort_values(...)

```python
expected = expected.sort_values()
```


## Complete Example

```python
# Setup
# Fixtures: closed, sort

# Workflow
index = IntervalIndex.from_arrays([1, 0, 3, 2], [1, 2, 3, 4], closed=closed)
result = index.difference(index[:1], sort=sort)
expected = index[1:]
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
result = index.difference(index, sort=sort)
expected = empty_index(dtype='int64', closed=closed)
tm.assert_index_equal(result, expected)
other = IntervalIndex.from_arrays(index.left.astype('float64'), index.right, closed=closed)
result = index.difference(other, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:131 | Complexity: Advanced | Last updated: 2026-06-02*