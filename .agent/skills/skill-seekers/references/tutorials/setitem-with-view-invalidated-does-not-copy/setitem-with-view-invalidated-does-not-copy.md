# How To: Setitem With View Invalidated Does Not Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem with view invalidated does not copy

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
# Fixtures: using_copy_on_write, warn_copy_on_write, request
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

### Step 2: Assign view = value

```python
view = df[:]
```

### Step 3: Assign unknown = 100

```python
df['b'] = 100
```

### Step 4: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

### Step 5: Assign view = None

```python
view = None
```

### Step 6: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 7: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='blk.delete does not track references correctly')
```

### Step 8: Call request.applymarker()

```python
request.applymarker(mark)
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write, request

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': 1, 'c': 1})
view = df[:]
df['b'] = 100
arr = get_array(df, 'a')
view = None
with tm.assert_cow_warning(warn_copy_on_write):
    df.iloc[0, 0] = 100
if using_copy_on_write:
    mark = pytest.mark.xfail(reason='blk.delete does not track references correctly')
    request.applymarker(mark)
    assert np.shares_memory(arr, get_array(df, 'a'))
```

## Next Steps


---

*Source: test_core_functionalities.py:45 | Complexity: Advanced | Last updated: 2026-06-02*