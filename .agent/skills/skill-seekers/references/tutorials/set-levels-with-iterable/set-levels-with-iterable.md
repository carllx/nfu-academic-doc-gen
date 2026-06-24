# How To: Set Levels With Iterable

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set levels with iterable

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign sizes = value

```python
sizes = [1, 2, 3]
```

### Step 2: Assign colors = value

```python
colors = ['black'] * 3
```

### Step 3: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays([sizes, colors], names=['size', 'color'])
```

### Step 4: Assign result = index.set_levels(...)

```python
result = index.set_levels(map(int, ['3', '2', '1']), level='size')
```

### Step 5: Assign expected_sizes = value

```python
expected_sizes = [3, 2, 1]
```

### Step 6: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays([expected_sizes, colors], names=['size', 'color'])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
sizes = [1, 2, 3]
colors = ['black'] * 3
index = MultiIndex.from_arrays([sizes, colors], names=['size', 'color'])
result = index.set_levels(map(int, ['3', '2', '1']), level='size')
expected_sizes = [3, 2, 1]
expected = MultiIndex.from_arrays([expected_sizes, colors], names=['size', 'color'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_get_set.py:342 | Complexity: Intermediate | Last updated: 2026-06-02*