# How To: Sort Values With Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort values with na

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [array([2, NA, 1], dtype='Int64'), array([1, 2, 3], dtype='Int64')]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 3: Assign index = index.sort_values(...)

```python
index = index.sort_values()
```

### Step 4: Assign result = DataFrame(...)

```python
result = DataFrame(range(3), index=index)
```

### Step 5: Assign arrays = value

```python
arrays = [array([1, 2, NA], dtype='Int64'), array([3, 1, 2], dtype='Int64')]
```

### Step 6: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(range(3), index=index)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [array([2, NA, 1], dtype='Int64'), array([1, 2, 3], dtype='Int64')]
index = MultiIndex.from_arrays(arrays)
index = index.sort_values()
result = DataFrame(range(3), index=index)
arrays = [array([1, 2, NA], dtype='Int64'), array([3, 1, 2], dtype='Int64')]
index = MultiIndex.from_arrays(arrays)
expected = DataFrame(range(3), index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sorted.py:96 | Complexity: Advanced | Last updated: 2026-06-02*