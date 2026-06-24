# How To: Merge Multiple Cols With Mixed Cols Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge multiple cols with mixed cols index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(range(6), MultiIndex.from_product([['A', 'B'], [1, 2, 3]], names=['lev1', 'lev2']), name='Amount')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': 0})
```

### Step 3: Assign result = merge(...)

```python
result = merge(df, s.reset_index(), on=['lev1', 'lev2'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': [0] * 6, 'Amount': range(6)})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
s = Series(range(6), MultiIndex.from_product([['A', 'B'], [1, 2, 3]], names=['lev1', 'lev2']), name='Amount')
df = DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': 0})
result = merge(df, s.reset_index(), on=['lev1', 'lev2'])
expected = DataFrame({'lev1': list('AAABBB'), 'lev2': [1, 2, 3, 1, 2, 3], 'col': [0] * 6, 'Amount': range(6)})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:177 | Complexity: Intermediate | Last updated: 2026-06-02*