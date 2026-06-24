# How To: Merge On Key Enlarging One

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge on key enlarging one

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
# Fixtures: using_copy_on_write, func, how
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'key': Series(['a', 'b', 'c'], dtype=object), 'a': [1, 2, 3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'key': Series(['a', 'b'], dtype=object), 'b': [4, 5]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 3: Assign df1_orig = df1.copy(...)

```python
df1_orig = df1.copy()
```

**Verification:**
```python
assert df2._mgr._has_no_reference(1)
```

### Step 4: Assign df2_orig = df2.copy(...)

```python
df2_orig = df2.copy()
```

**Verification:**
```python
assert df2._mgr._has_no_reference(0)
```

### Step 5: Assign result = func(...)

```python
result = func(df1, df2, how=how)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'key'), get_array(df1, 'key')) is (how == 'left')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df1_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'key'), get_array(df2, 'key'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df2_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 8: Assign unknown = 0

```python
result.iloc[0, 1] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 9: Assign unknown = 0

```python
result.iloc[0, 2] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, func, how

# Workflow
df1 = DataFrame({'key': Series(['a', 'b', 'c'], dtype=object), 'a': [1, 2, 3]})
df2 = DataFrame({'key': Series(['a', 'b'], dtype=object), 'b': [4, 5]})
df1_orig = df1.copy()
df2_orig = df2.copy()
result = func(df1, df2, how=how)
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
    assert df2._mgr._has_no_reference(1)
    assert df2._mgr._has_no_reference(0)
    assert np.shares_memory(get_array(result, 'key'), get_array(df1, 'key')) is (how == 'left')
    assert not np.shares_memory(get_array(result, 'key'), get_array(df2, 'key'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
if how == 'left':
    result.iloc[0, 1] = 0
else:
    result.iloc[0, 2] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
tm.assert_frame_equal(df1, df1_orig)
tm.assert_frame_equal(df2, df2_orig)
```

## Next Steps


---

*Source: test_functions.py:270 | Complexity: Advanced | Last updated: 2026-06-02*