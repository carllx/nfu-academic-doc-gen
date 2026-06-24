# How To: Setitem Dont Track Unnecessary References

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem dont track unnecessary references

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
df = DataFrame({'a': [1, 2, 3], 'b': 1, 'c': 1})
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign unknown = 100

```python
df['b'] = 100
```

### Step 3: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

### Step 4: Assign unknown = 100

```python
df.iloc[0, 0] = 100
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
df = DataFrame({'a': [1, 2, 3], 'b': 1, 'c': 1})
df['b'] = 100
arr = get_array(df, 'a')
df.iloc[0, 0] = 100
assert np.shares_memory(arr, get_array(df, 'a'))
```

## Next Steps


---

*Source: test_core_functionalities.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*