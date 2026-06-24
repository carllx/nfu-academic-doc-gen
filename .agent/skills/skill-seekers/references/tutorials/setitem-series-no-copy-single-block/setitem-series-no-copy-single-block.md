# How To: Setitem Series No Copy Single Block

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem series no copy single block

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
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(rhs), get_array(df, 'a'))
```

### Step 2: Assign rhs = Series(...)

```python
rhs = Series([4, 5, 6])
```

### Step 3: Assign rhs_orig = rhs.copy(...)

```python
rhs_orig = rhs.copy()
```

### Step 4: Assign unknown = rhs

```python
df['a'] = rhs
```

### Step 5: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rhs, rhs_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(rhs), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
rhs = Series([4, 5, 6])
rhs_orig = rhs.copy()
df['a'] = rhs
if using_copy_on_write:
    assert np.shares_memory(get_array(rhs), get_array(df, 'a'))
df.iloc[0, 0] = 100
tm.assert_series_equal(rhs, rhs_orig)
```

## Next Steps


---

*Source: test_setitem.py:103 | Complexity: Intermediate | Last updated: 2026-06-02*