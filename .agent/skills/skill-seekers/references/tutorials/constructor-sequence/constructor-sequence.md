# How To: Constructor Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor sequence

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

### Step 1: Assign expected = Series(...)

```python
expected = Series(list(range(10)), dtype='int64')
```

### Step 2: Assign result = Series(...)

```python
result = Series(range(10), dtype='int64')
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = Series(list(range(10)), dtype='int64')
result = Series(range(10), dtype='int64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:300 | Complexity: Beginner | Last updated: 2026-06-02*