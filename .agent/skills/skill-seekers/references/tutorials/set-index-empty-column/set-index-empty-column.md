# How To: Set Index Empty Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index empty column

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([{'a': 1, 'p': 0}, {'a': 2, 'm': 10}, {'a': 3, 'm': 11, 'p': 20}, {'a': 4, 'm': 12, 'p': 21}], columns=['a', 'm', 'p', 'x'])
```

### Step 2: Assign result = df.set_index(...)

```python
result = df.set_index(['a', 'x'])
```

### Step 3: Assign expected = value

```python
expected = df[['m', 'p']]
```

### Step 4: Assign expected.index = MultiIndex.from_arrays(...)

```python
expected.index = MultiIndex.from_arrays([df['a'], df['x']], names=['a', 'x'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([{'a': 1, 'p': 0}, {'a': 2, 'm': 10}, {'a': 3, 'm': 11, 'p': 20}, {'a': 4, 'm': 12, 'p': 21}], columns=['a', 'm', 'p', 'x'])
result = df.set_index(['a', 'x'])
expected = df[['m', 'p']]
expected.index = MultiIndex.from_arrays([df['a'], df['x']], names=['a', 'x'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_set_index.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*