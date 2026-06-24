# How To: Merge On Key

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge on key

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
# Fixtures: using_copy_on_write, func
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
df2 = DataFrame({'key': Series(['a', 'b', 'c'], dtype=object), 'b': [4, 5, 6]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 3: Assign df1_orig = df1.copy(...)

```python
df1_orig = df1.copy()
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'key'), get_array(df1, 'key'))
```

### Step 4: Assign df2_orig = df2.copy(...)

```python
df2_orig = df2.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'key'), get_array(df2, 'key'))
```

### Step 5: Assign result = func(...)

```python
result = func(df1, df2, on='key')
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 6: Assign unknown = 0

```python
result.iloc[0, 1] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 7: Assign unknown = 0

```python
result.iloc[0, 2] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df1_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df2_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, func

# Workflow
df1 = DataFrame({'key': Series(['a', 'b', 'c'], dtype=object), 'a': [1, 2, 3]})
df2 = DataFrame({'key': Series(['a', 'b', 'c'], dtype=object), 'b': [4, 5, 6]})
df1_orig = df1.copy()
df2_orig = df2.copy()
result = func(df1, df2, on='key')
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
    assert np.shares_memory(get_array(result, 'key'), get_array(df1, 'key'))
    assert not np.shares_memory(get_array(result, 'key'), get_array(df2, 'key'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
result.iloc[0, 1] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
result.iloc[0, 2] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
tm.assert_frame_equal(df1, df1_orig)
tm.assert_frame_equal(df2, df2_orig)
```

## Next Steps


---

*Source: test_functions.py:207 | Complexity: Advanced | Last updated: 2026-06-02*