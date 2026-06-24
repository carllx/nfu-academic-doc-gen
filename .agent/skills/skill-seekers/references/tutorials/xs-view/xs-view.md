# How To: Xs View

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs view

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
# Fixtures: using_array_manager, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign dm = DataFrame(...)

```python
dm = DataFrame(np.arange(20.0).reshape(4, 5), index=range(4), columns=range(5))
```

**Verification:**
```python
assert not (dm.xs(2) == 20).any()
```

### Step 2: Assign df_orig = dm.copy(...)

```python
df_orig = dm.copy()
```

**Verification:**
```python
assert (dm.xs(2) == 20).all()
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(dm, df_orig)
```

### Step 4: Assign unknown = 20

```python
dm.xs(2)[:] = 20
```

### Step 5: Assign msg = '\\nA value is trying to be set on a copy of a slice from a DataFrame'

```python
msg = '\\nA value is trying to be set on a copy of a slice from a DataFrame'
```

**Verification:**
```python
assert not (dm.xs(2) == 20).any()
```

### Step 6: Assign unknown = 20

```python
dm.xs(2)[:] = 20
```

### Step 7: Assign unknown = 20

```python
dm.xs(2)[:] = 20
```


## Complete Example

```python
# Setup
# Fixtures: using_array_manager, using_copy_on_write, warn_copy_on_write

# Workflow
dm = DataFrame(np.arange(20.0).reshape(4, 5), index=range(4), columns=range(5))
df_orig = dm.copy()
if using_copy_on_write:
    with tm.raises_chained_assignment_error():
        dm.xs(2)[:] = 20
    tm.assert_frame_equal(dm, df_orig)
elif using_array_manager:
    msg = '\\nA value is trying to be set on a copy of a slice from a DataFrame'
    with pytest.raises(SettingWithCopyError, match=msg):
        dm.xs(2)[:] = 20
    assert not (dm.xs(2) == 20).any()
else:
    with tm.raises_chained_assignment_error():
        dm.xs(2)[:] = 20
    assert (dm.xs(2) == 20).all()
```

## Next Steps


---

*Source: test_xs.py:125 | Complexity: Advanced | Last updated: 2026-06-02*