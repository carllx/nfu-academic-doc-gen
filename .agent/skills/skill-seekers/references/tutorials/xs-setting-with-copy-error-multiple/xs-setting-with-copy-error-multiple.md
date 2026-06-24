# How To: Xs Setting With Copy Error Multiple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs setting with copy error multiple

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: four_level_index_dataframe, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = four_level_index_dataframe

```python
df = four_level_index_dataframe
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 3: Assign result = df.xs(...)

```python
result = df.xs(('a', 4), level=['one', 'four'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 5: Assign unknown = 10

```python
result[:] = 10
```

### Step 6: Assign msg = 'A value is trying to be set on a copy of a slice from a DataFrame'

```python
msg = 'A value is trying to be set on a copy of a slice from a DataFrame'
```

### Step 7: Assign unknown = 10

```python
result[:] = 10
```


## Complete Example

```python
# Setup
# Fixtures: four_level_index_dataframe, using_copy_on_write, warn_copy_on_write

# Workflow
df = four_level_index_dataframe
df_orig = df.copy()
result = df.xs(('a', 4), level=['one', 'four'])
if using_copy_on_write or warn_copy_on_write:
    result[:] = 10
else:
    msg = 'A value is trying to be set on a copy of a slice from a DataFrame'
    with pytest.raises(SettingWithCopyError, match=msg):
        result[:] = 10
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_xs.py:227 | Complexity: Advanced | Last updated: 2026-06-02*