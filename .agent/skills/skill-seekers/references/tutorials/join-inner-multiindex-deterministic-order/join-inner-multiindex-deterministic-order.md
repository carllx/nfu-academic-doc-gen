# How To: Join Inner Multiindex Deterministic Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join inner multiindex deterministic order

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame(data={'e': 5}, index=MultiIndex.from_tuples([(1, 2, 4)], names=('a', 'b', 'd')))
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame(data={'f': 6}, index=MultiIndex.from_tuples([(2, 3)], names=('b', 'c')))
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, how='inner')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'e': [5], 'f': [6]}, index=MultiIndex.from_tuples([(1, 2, 4, 3)], names=('a', 'b', 'd', 'c')))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame(data={'e': 5}, index=MultiIndex.from_tuples([(1, 2, 4)], names=('a', 'b', 'd')))
right = DataFrame(data={'f': 6}, index=MultiIndex.from_tuples([(2, 3)], names=('b', 'c')))
result = left.join(right, how='inner')
expected = DataFrame({'e': [5], 'f': [6]}, index=MultiIndex.from_tuples([(1, 2, 4, 3)], names=('a', 'b', 'd', 'c')))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:919 | Complexity: Intermediate | Last updated: 2026-06-02*