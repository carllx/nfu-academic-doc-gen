# How To: Transpose Empty Preserves Datetimeindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transpose empty preserves datetimeindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex([], dtype='M8[ns]')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(index=dti)
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
```

### Step 4: Assign result1 = value

```python
result1 = df.T.sum().index
```

### Step 5: Assign result2 = value

```python
result2 = df.sum(axis=1).index
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result1, expected)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result2, expected)
```


## Complete Example

```python
# Workflow
dti = DatetimeIndex([], dtype='M8[ns]')
df = DataFrame(index=dti)
expected = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
result1 = df.T.sum().index
result2 = df.sum(axis=1).index
tm.assert_index_equal(result1, expected)
tm.assert_index_equal(result2, expected)
```

## Next Steps


---

*Source: test_transpose.py:33 | Complexity: Intermediate | Last updated: 2026-06-02*