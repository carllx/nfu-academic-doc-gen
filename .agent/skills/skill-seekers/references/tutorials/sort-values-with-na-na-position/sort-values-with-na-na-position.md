# How To: Sort Values With Na Na Position

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sort values with na na position

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`

**Setup Required:**
```python
# Fixtures: dtype, na_position
```

## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [Series([1, 1, 2], dtype=dtype), Series([1, None, 3], dtype=dtype)]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 3: Assign result = index.sort_values(...)

```python
result = index.sort_values(na_position=na_position)
```

### Step 4: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays(arrays)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign arrays = value

```python
arrays = [Series([1, 1, 2], dtype=dtype), Series([None, 1, 3], dtype=dtype)]
```

### Step 7: Assign arrays = value

```python
arrays = [Series([1, 1, 2], dtype=dtype), Series([1, None, 3], dtype=dtype)]
```


## Complete Example

```python
# Setup
# Fixtures: dtype, na_position

# Workflow
arrays = [Series([1, 1, 2], dtype=dtype), Series([1, None, 3], dtype=dtype)]
index = MultiIndex.from_arrays(arrays)
result = index.sort_values(na_position=na_position)
if na_position == 'first':
    arrays = [Series([1, 1, 2], dtype=dtype), Series([None, 1, 3], dtype=dtype)]
else:
    arrays = [Series([1, 1, 2], dtype=dtype), Series([1, None, 3], dtype=dtype)]
expected = MultiIndex.from_arrays(arrays)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_sorting.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*