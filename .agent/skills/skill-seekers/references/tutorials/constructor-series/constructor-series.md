# How To: Constructor Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor series

## Prerequisites

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `dateutil.tz`
- `numpy`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.internals.blocks`
- `numpy.dtypes`


## Step-by-Step Guide

### Step 1: Assign index1 = value

```python
index1 = ['d', 'b', 'a', 'c']
```

### Step 2: Assign index2 = sorted(...)

```python
index2 = sorted(index1)
```

### Step 3: Assign s1 = Series(...)

```python
s1 = Series([4, 7, -5, 3], index=index1)
```

### Step 4: Assign s2 = Series(...)

```python
s2 = Series(s1, index=index2)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s2, s1.sort_index())
```


## Complete Example

```python
# Workflow
index1 = ['d', 'b', 'a', 'c']
index2 = sorted(index1)
s1 = Series([4, 7, -5, 3], index=index1)
s2 = Series(s1, index=index2)
tm.assert_series_equal(s2, s1.sort_index())
```

## Next Steps


---

*Source: test_constructors.py:282 | Complexity: Intermediate | Last updated: 2026-06-02*