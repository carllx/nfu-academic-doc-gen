# How To: Getitem Boolean Iadd

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem boolean iadd

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((5, 5))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr.copy(), columns=['A', 'B', 'C', 'D', 'E'])
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(df.values, arr)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((5, 5))
df = DataFrame(arr.copy(), columns=['A', 'B', 'C', 'D', 'E'])
df[df < 0] += 1
arr[arr < 0] += 1
tm.assert_almost_equal(df.values, arr)
```

## Next Steps


---

*Source: test_indexing.py:228 | Complexity: Beginner | Last updated: 2026-06-02*