# How To: Fillna Inplace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna inplace

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
# Fixtures: using_copy_on_write, downcast
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.5, np.nan], 'b': 1})
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), arr_a)
```

### Step 2: Assign arr_a = get_array(...)

```python
arr_a = get_array(df, 'a')
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), arr_b)
```

### Step 3: Assign arr_b = get_array(...)

```python
arr_b = get_array(df, 'b')
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 4: Assign msg = "The 'downcast' keyword in fillna is deprecated"

```python
msg = "The 'downcast' keyword in fillna is deprecated"
```

**Verification:**
```python
assert df._mgr._has_no_reference(1)
```

### Step 5: Call df.fillna()

```python
df.fillna(5.5, inplace=True, downcast=downcast)
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, downcast

# Workflow
df = DataFrame({'a': [1.5, np.nan], 'b': 1})
arr_a = get_array(df, 'a')
arr_b = get_array(df, 'b')
msg = "The 'downcast' keyword in fillna is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.fillna(5.5, inplace=True, downcast=downcast)
assert np.shares_memory(get_array(df, 'a'), arr_a)
assert np.shares_memory(get_array(df, 'b'), arr_b)
if using_copy_on_write:
    assert df._mgr._has_no_reference(0)
    assert df._mgr._has_no_reference(1)
```

## Next Steps


---

*Source: test_interp_fillna.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*