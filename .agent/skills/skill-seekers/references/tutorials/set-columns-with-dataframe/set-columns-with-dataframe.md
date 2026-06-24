# How To: Set Columns With Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set columns with dataframe

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'c'), get_array(df2, 'c'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'c': [7, 8, 9], 'd': [10, 11, 12]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), get_array(df2, 'c'))
```

### Step 3: Assign unknown = df2

```python
df[['c', 'd']] = df2
```

### Step 4: Assign unknown = 0

```python
df2.iloc[0, 0] = 0
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['c'], Series([7, 8, 9], name='c'))
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'c'), get_array(df2, 'c'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df2 = DataFrame({'c': [7, 8, 9], 'd': [10, 11, 12]})
df[['c', 'd']] = df2
if using_copy_on_write:
    assert np.shares_memory(get_array(df, 'c'), get_array(df2, 'c'))
else:
    assert not np.shares_memory(get_array(df, 'c'), get_array(df2, 'c'))
df2.iloc[0, 0] = 0
tm.assert_series_equal(df['c'], Series([7, 8, 9], name='c'))
```

## Next Steps


---

*Source: test_setitem.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*