# How To: Setitem With View Copies

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem with view copies

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': 1, 'c': 1})
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign view = value

```python
view = df[:]
```

### Step 3: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 4: Assign unknown = 100

```python
df['b'] = 100
```

### Step 5: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

### Step 6: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(df, 'a'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(view, expected)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': 1, 'c': 1})
view = df[:]
expected = df.copy()
df['b'] = 100
arr = get_array(df, 'a')
with tm.assert_cow_warning(warn_copy_on_write):
    df.iloc[0, 0] = 100
if using_copy_on_write:
    assert not np.shares_memory(arr, get_array(df, 'a'))
    tm.assert_frame_equal(view, expected)
```

## Next Steps


---

*Source: test_core_functionalities.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*