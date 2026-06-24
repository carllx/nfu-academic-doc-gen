# How To: Constructor Boolean Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor boolean index

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

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3], index=[4, 5, 6])
```

### Step 2: Assign index = value

```python
index = s1 == 2
```

### Step 3: Assign result = Series(...)

```python
result = Series([1, 3, 2], index=index)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 3, 2], index=[False, True, False])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2, 3], index=[4, 5, 6])
index = s1 == 2
result = Series([1, 3, 2], index=index)
expected = Series([1, 3, 2], index=[False, True, False])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*