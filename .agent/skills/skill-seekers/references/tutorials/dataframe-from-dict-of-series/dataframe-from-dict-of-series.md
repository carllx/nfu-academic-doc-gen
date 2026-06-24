# How To: Dataframe From Dict Of Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe from dict of series

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
# Fixtures: request, using_copy_on_write, warn_copy_on_write, columns, index, dtype
```

## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3])
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(s1))
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6])
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
```

### Step 3: Assign s1_orig = s1.copy(...)

```python
s1_orig = s1.copy()
```

**Verification:**
```python
assert s1.iloc[0] == 10
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=index, columns=columns, dtype=dtype)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
```

### Step 5: Assign result = DataFrame(...)

```python
result = DataFrame({'a': s1, 'b': s2}, index=index, columns=columns, dtype=dtype, copy=False)
```

**Verification:**
```python
assert result.iloc[0, 0] == 10
```

### Step 6: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3])
```

### Step 7: Assign s2 = Series(...)

```python
s2 = Series([4, 5, 6])
```

### Step 8: Assign result = DataFrame(...)

```python
result = DataFrame({'a': s1, 'b': s2}, index=index, columns=columns, dtype=dtype, copy=False)
```

### Step 9: Assign unknown = 10

```python
result.iloc[0, 0] = 10
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s1_orig)
```

**Verification:**
```python
assert s1.iloc[0] == 10
```

### Step 11: Assign unknown = 10

```python
s1.iloc[0] = 10
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert result.iloc[0, 0] == 10
```


## Complete Example

```python
# Setup
# Fixtures: request, using_copy_on_write, warn_copy_on_write, columns, index, dtype

# Workflow
s1 = Series([1, 2, 3])
s2 = Series([4, 5, 6])
s1_orig = s1.copy()
expected = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]}, index=index, columns=columns, dtype=dtype)
result = DataFrame({'a': s1, 'b': s2}, index=index, columns=columns, dtype=dtype, copy=False)
assert np.shares_memory(get_array(result, 'a'), get_array(s1))
with tm.assert_cow_warning(warn_copy_on_write):
    result.iloc[0, 0] = 10
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
    tm.assert_series_equal(s1, s1_orig)
else:
    assert s1.iloc[0] == 10
s1 = Series([1, 2, 3])
s2 = Series([4, 5, 6])
result = DataFrame({'a': s1, 'b': s2}, index=index, columns=columns, dtype=dtype, copy=False)
with tm.assert_cow_warning(warn_copy_on_write):
    s1.iloc[0] = 10
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(s1))
    tm.assert_frame_equal(result, expected)
else:
    assert result.iloc[0, 0] == 10
```

## Next Steps


---

*Source: test_constructors.py:224 | Complexity: Advanced | Last updated: 2026-06-02*