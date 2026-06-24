# How To: Assigning To Same Variable Removes References

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assigning to same variable removes references

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
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert df._mgr._has_no_reference(1)
```

### Step 2: Assign df = df.reset_index(...)

```python
df = df.reset_index()
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```

### Step 3: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

### Step 4: Assign unknown = 100

```python
df.iloc[0, 1] = 100
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3]})
df = df.reset_index()
if using_copy_on_write:
    assert df._mgr._has_no_reference(1)
arr = get_array(df, 'a')
df.iloc[0, 1] = 100
assert np.shares_memory(arr, get_array(df, 'a'))
```

## Next Steps


---

*Source: test_core_functionalities.py:9 | Complexity: Intermediate | Last updated: 2026-06-02*