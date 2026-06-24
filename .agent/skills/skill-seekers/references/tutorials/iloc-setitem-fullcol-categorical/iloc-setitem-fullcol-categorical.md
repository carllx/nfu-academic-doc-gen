# How To: Iloc Setitem Fullcol Categorical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test iloc setitem fullcol categorical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tests.indexing.common`

**Setup Required:**
```python
# Fixtures: indexer, key, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame({0: range(3)}, dtype=object)
```

**Verification:**
```python
assert frame._mgr.blocks[0]._can_hold_element(cat)
```

### Step 2: Assign cat = Categorical(...)

```python
cat = Categorical(['alpha', 'beta', 'gamma'])
```

**Verification:**
```python
assert np.shares_memory(df[0].values, orig_vals)
```

### Step 3: Assign df = frame.copy(...)

```python
df = frame.copy()
```

**Verification:**
```python
assert cat[0] != 'gamma'
```

### Step 4: Assign orig_vals = value

```python
orig_vals = df.values
```

### Step 5: Assign unknown = cat

```python
indexer(df)[key, 0] = cat
```

### Step 6: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame({0: cat}).astype(object)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 8: Assign unknown = 'gamma'

```python
df.iloc[0, 0] = 'gamma'
```

**Verification:**
```python
assert cat[0] != 'gamma'
```

### Step 9: Assign frame = DataFrame(...)

```python
frame = DataFrame({0: np.array([0, 1, 2], dtype=object), 1: range(3)})
```

### Step 10: Assign df = frame.copy(...)

```python
df = frame.copy()
```

### Step 11: Assign unknown = cat

```python
indexer(df)[key, 0] = cat
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: Series(cat.astype(object), dtype=object), 1: range(3)})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert frame._mgr.blocks[0]._can_hold_element(cat)
```


## Complete Example

```python
# Setup
# Fixtures: indexer, key, using_array_manager

# Workflow
frame = DataFrame({0: range(3)}, dtype=object)
cat = Categorical(['alpha', 'beta', 'gamma'])
if not using_array_manager:
    assert frame._mgr.blocks[0]._can_hold_element(cat)
df = frame.copy()
orig_vals = df.values
indexer(df)[key, 0] = cat
expected = DataFrame({0: cat}).astype(object)
if not using_array_manager:
    assert np.shares_memory(df[0].values, orig_vals)
tm.assert_frame_equal(df, expected)
df.iloc[0, 0] = 'gamma'
assert cat[0] != 'gamma'
frame = DataFrame({0: np.array([0, 1, 2], dtype=object), 1: range(3)})
df = frame.copy()
indexer(df)[key, 0] = cat
expected = DataFrame({0: Series(cat.astype(object), dtype=object), 1: range(3)})
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_iloc.py:75 | Complexity: Advanced | Last updated: 2026-06-02*