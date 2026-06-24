# How To: Set Column With Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set column with series

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
assert np.shares_memory(get_array(df, 'c'), get_array(ser))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3])
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), get_array(ser))
```

### Step 3: Assign unknown = ser

```python
df['c'] = ser
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 4: Assign unknown = 0

```python
ser.iloc[0] = 0
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['c'], Series([1, 2, 3], name='c'))
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'c'), get_array(ser))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
ser = Series([1, 2, 3])
df['c'] = ser
if using_copy_on_write:
    assert np.shares_memory(get_array(df, 'c'), get_array(ser))
else:
    assert not np.shares_memory(get_array(df, 'c'), get_array(ser))
ser.iloc[0] = 0
assert ser.iloc[0] == 0
tm.assert_series_equal(df['c'], Series([1, 2, 3], name='c'))
```

## Next Steps


---

*Source: test_setitem.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*