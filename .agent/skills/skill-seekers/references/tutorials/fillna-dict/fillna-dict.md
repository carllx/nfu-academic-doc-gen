# How To: Fillna Dict

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna dict

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
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
df = DataFrame({'a': [1.5, np.nan], 'b': 1})
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
```

### Step 3: Assign df2 = df.fillna(...)

```python
df2 = df.fillna({'a': 100.5})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```

### Step 4: Assign unknown = 100

```python
df2.iloc[0, 1] = 100
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_orig, df)
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1.5, np.nan], 'b': 1})
df_orig = df.copy()
df2 = df.fillna({'a': 100.5})
if using_copy_on_write:
    assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
    assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
else:
    assert not np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
df2.iloc[0, 1] = 100
tm.assert_frame_equal(df_orig, df)
```

## Next Steps


---

*Source: test_interp_fillna.py:230 | Complexity: Intermediate | Last updated: 2026-06-02*