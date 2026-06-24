# How To: Set Column With Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set column with array

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), arr)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype='int64')
```

### Step 3: Assign unknown = arr

```python
df['c'] = arr
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), arr)
```

### Step 4: Assign unknown = 0

```python
arr[0] = 0
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['c'], Series([1, 2, 3], name='c'))
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
arr = np.array([1, 2, 3], dtype='int64')
df['c'] = arr
assert not np.shares_memory(get_array(df, 'c'), arr)
arr[0] = 0
tm.assert_series_equal(df['c'], Series([1, 2, 3], name='c'))
```

## Next Steps


---

*Source: test_setitem.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*