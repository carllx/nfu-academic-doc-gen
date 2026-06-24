# How To: Merge On Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge on index

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'b': [4, 5, 6]})
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
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 4: Assign df2_orig = df2.copy(...)

```python
df2_orig = df2.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 5: Assign result = merge(...)

```python
result = merge(df1, df2, left_index=True, right_index=True)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 6: Assign unknown = 0

```python
result.iloc[0, 0] = 0
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 7: Assign unknown = 0

```python
result.iloc[0, 1] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df1, df1_orig)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df2_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df1 = DataFrame({'a': [1, 2, 3]})
df2 = DataFrame({'b': [4, 5, 6]})
df1_orig = df1.copy()
df2_orig = df2.copy()
result = merge(df1, df2, left_index=True, right_index=True)
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
result.iloc[0, 0] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
result.iloc[0, 1] = 0
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'b'), get_array(df2, 'b'))
tm.assert_frame_equal(df1, df1_orig)
tm.assert_frame_equal(df2, df2_orig)
```

## Next Steps


---

*Source: test_functions.py:236 | Complexity: Advanced | Last updated: 2026-06-02*