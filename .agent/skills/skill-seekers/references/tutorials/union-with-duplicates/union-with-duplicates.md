# How To: Union With Duplicates

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union with duplicates

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `struct`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.arrays`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign lvals = op(...)

```python
lvals = op([3, 1, 3, 4])
```

### Step 2: Assign rvals = op(...)

```python
rvals = op([2, 3, 1, 1])
```

### Step 3: Assign expected = op(...)

```python
expected = op([3, 3, 1, 1, 4, 2])
```

### Step 4: Assign result = algos.union_with_duplicates(...)

```python
result = algos.union_with_duplicates(lvals, rvals)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = algos.union_with_duplicates(...)

```python
result = algos.union_with_duplicates(lvals, rvals)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
lvals = op([3, 1, 3, 4])
rvals = op([2, 3, 1, 1])
expected = op([3, 3, 1, 1, 4, 2])
if isinstance(expected, np.ndarray):
    result = algos.union_with_duplicates(lvals, rvals)
    tm.assert_numpy_array_equal(result, expected)
else:
    result = algos.union_with_duplicates(lvals, rvals)
    tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_algos.py:2049 | Complexity: Intermediate | Last updated: 2026-06-02*