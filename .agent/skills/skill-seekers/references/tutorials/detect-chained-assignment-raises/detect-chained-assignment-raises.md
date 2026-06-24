# How To: Detect Chained Assignment Raises

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_array_manager, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': Series(range(2), dtype='int64'), 'B': np.array(np.arange(2, 4), dtype=np.float64)})
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 2: Assign df_original = df.copy(...)

```python
df_original = df.copy()
```

**Verification:**
```python
assert df['A']._is_copy is None
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_original)
```

### Step 4: Assign unknown = value

```python
df['A'][0] = -5
```

### Step 5: Assign unknown = value

```python
df['A'][1] = -6
```

### Step 6: Assign unknown = value

```python
df['A'][0] = -5
```

### Step 7: Assign unknown = value

```python
df['A'][1] = np.nan
```

**Verification:**
```python
assert df['A']._is_copy is None
```

### Step 8: Assign unknown = value

```python
df['A'][0] = -5
```

### Step 9: Assign unknown = value

```python
df['A'][1] = -6
```

### Step 10: Assign expected = DataFrame(...)

```python
expected = DataFrame([[-5, 2], [-6, 3]], columns=list('AB'))
```

### Step 11: Assign unknown = unknown.astype(...)

```python
expected['B'] = expected['B'].astype('float64')
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 13: Assign unknown = value

```python
df['A'][0] = -5
```

### Step 14: Assign unknown = value

```python
df['A'][1] = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager, using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'A': Series(range(2), dtype='int64'), 'B': np.array(np.arange(2, 4), dtype=np.float64)})
df_original = df.copy()
assert df._is_copy is None
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['A'][0] = -5
    with tm.raises_chained_assignment_error():
        df['A'][1] = -6
    tm.assert_frame_equal(df, df_original)
elif warn_copy_on_write:
    with tm.raises_chained_assignment_error():
        df['A'][0] = -5
    with tm.raises_chained_assignment_error():
        df['A'][1] = np.nan
elif not using_array_manager:
    with pytest.raises(SettingWithCopyError, match=msg):
        with tm.raises_chained_assignment_error():
            df['A'][0] = -5
    with pytest.raises(SettingWithCopyError, match=msg):
        with tm.raises_chained_assignment_error():
            df['A'][1] = np.nan
    assert df['A']._is_copy is None
else:
    df['A'][0] = -5
    df['A'][1] = -6
    expected = DataFrame([[-5, 2], [-6, 3]], columns=list('AB'))
    expected['B'] = expected['B'].astype('float64')
    tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_chaining_and_caching.py:215 | Complexity: Advanced | Last updated: 2026-06-02*