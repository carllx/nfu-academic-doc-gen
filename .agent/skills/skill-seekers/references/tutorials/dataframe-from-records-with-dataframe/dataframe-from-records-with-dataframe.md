# How To: Dataframe From Records With Dataframe

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe from records with dataframe

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
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert not df._mgr._has_no_reference(0)
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
```

### Step 3: Assign df2 = DataFrame.from_records(...)

```python
df2 = DataFrame.from_records(df)
```

**Verification:**
```python
assert not df._mgr._has_no_reference(0)
```

### Step 4: Assign unknown = 100

```python
df2.iloc[0, 0] = 100
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df2)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3]})
df_orig = df.copy()
with tm.assert_produces_warning(FutureWarning):
    df2 = DataFrame.from_records(df)
if using_copy_on_write:
    assert not df._mgr._has_no_reference(0)
assert np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
with tm.assert_cow_warning(warn_copy_on_write):
    df2.iloc[0, 0] = 100
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    tm.assert_frame_equal(df, df2)
```

## Next Steps


---

*Source: test_constructors.py:357 | Complexity: Intermediate | Last updated: 2026-06-02*