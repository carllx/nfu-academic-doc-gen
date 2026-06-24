# How To: Set Index Empty Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index empty dataframe

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': Series(dtype='datetime64[ns]'), 'b': Series(dtype='int64'), 'c': []})
```

### Step 2: Assign df2 = df1.set_index(...)

```python
df2 = df1.set_index(['a', 'b'])
```

### Step 3: Assign result = value

```python
result = df2.index.to_frame().dtypes
```

### Step 4: Assign expected = value

```python
expected = df1[['a', 'b']].dtypes
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame({'a': Series(dtype='datetime64[ns]'), 'b': Series(dtype='int64'), 'c': []})
df2 = df1.set_index(['a', 'b'])
result = df2.index.to_frame().dtypes
expected = df1[['a', 'b']].dtypes
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_set_index.py:86 | Complexity: Intermediate | Last updated: 2026-06-02*