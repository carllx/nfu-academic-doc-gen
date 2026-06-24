# How To: Dataframe From Series Or Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe from series or index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write, data, dtype, cons
```

## Step-by-Step Guide

### Step 1: Assign obj = cons(...)

```python
obj = cons(data, dtype=dtype)
```

**Verification:**
```python
assert np.shares_memory(get_array(obj), get_array(df, 0))
```

### Step 2: Assign obj_orig = obj.copy(...)

```python
obj_orig = obj.copy()
```

**Verification:**
```python
assert not df._mgr._has_no_reference(0)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(obj, dtype=dtype)
```

**Verification:**
```python
assert np.shares_memory(get_array(obj), get_array(df, 0))
```

### Step 4: Assign unknown = value

```python
df.iloc[0, 0] = data[-1]
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(obj, obj_orig)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write, data, dtype, cons

# Workflow
obj = cons(data, dtype=dtype)
obj_orig = obj.copy()
df = DataFrame(obj, dtype=dtype)
assert np.shares_memory(get_array(obj), get_array(df, 0))
if using_copy_on_write:
    assert not df._mgr._has_no_reference(0)
with tm.assert_cow_warning(warn_copy_on_write):
    df.iloc[0, 0] = data[-1]
if using_copy_on_write:
    tm.assert_equal(obj, obj_orig)
```

## Next Steps


---

*Source: test_constructors.py:290 | Complexity: Intermediate | Last updated: 2026-06-02*