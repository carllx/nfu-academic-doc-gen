# How To: Multiindex Assignment

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex assignment

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(5, 10, size=9).reshape(3, 3), columns=list('abc'), index=[[4, 4, 8], [8, 10, 12]])
```

### Step 2: Assign unknown = value

```python
df['d'] = np.nan
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([0.0, 1.0])
```

### Step 4: Assign unknown = arr

```python
df.loc[4, 'd'] = arr
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df.loc[4, 'd'], Series(arr, index=[8, 10], name='d'))
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).integers(5, 10, size=9).reshape(3, 3), columns=list('abc'), index=[[4, 4, 8], [8, 10, 12]])
df['d'] = np.nan
arr = np.array([0.0, 1.0])
df.loc[4, 'd'] = arr
tm.assert_series_equal(df.loc[4, 'd'], Series(arr, index=[8, 10], name='d'))
```

## Next Steps


---

*Source: test_setitem.py:188 | Complexity: Intermediate | Last updated: 2026-06-02*