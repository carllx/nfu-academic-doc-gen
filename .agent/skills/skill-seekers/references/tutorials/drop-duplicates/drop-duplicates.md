# How To: Drop Duplicates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test drop duplicates

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: index_flat, keep
```

## Step-by-Step Guide

### Step 1: Assign index = index_flat

```python
index = index_flat
```

### Step 2: Assign holder = type(...)

```python
holder = type(index)
```

### Step 3: Assign unique_values = list(...)

```python
unique_values = list(set(index))
```

### Step 4: Assign dtype = value

```python
dtype = index.dtype if is_numeric_dtype(index) else None
```

### Step 5: Assign unique_idx = holder(...)

```python
unique_idx = holder(unique_values, dtype=dtype)
```

### Step 6: Assign n = len(...)

```python
n = len(unique_idx)
```

### Step 7: Assign duplicated_selection = np.random.default_rng.choice(...)

```python
duplicated_selection = np.random.default_rng(2).choice(n, int(n * 1.5))
```

### Step 8: Assign idx = holder(...)

```python
idx = holder(unique_idx.values[duplicated_selection])
```

### Step 9: Assign expected_duplicated = value

```python
expected_duplicated = pd.Series(duplicated_selection).duplicated(keep=keep).values
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.duplicated(keep=keep), expected_duplicated)
```

### Step 11: Assign expected_dropped = holder(...)

```python
expected_dropped = holder(pd.Series(idx).drop_duplicates(keep=keep))
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.drop_duplicates(keep=keep), expected_dropped)
```

### Step 13: Call pytest.skip()

```python
pytest.skip('RangeIndex is tested in test_drop_duplicates_no_duplicates as it cannot hold duplicates')
```

### Step 14: Call pytest.skip()

```python
pytest.skip('empty index is tested in test_drop_duplicates_no_duplicates as it cannot hold duplicates')
```


## Complete Example

```python
# Setup
# Fixtures: index_flat, keep

# Workflow
index = index_flat
if isinstance(index, RangeIndex):
    pytest.skip('RangeIndex is tested in test_drop_duplicates_no_duplicates as it cannot hold duplicates')
if len(index) == 0:
    pytest.skip('empty index is tested in test_drop_duplicates_no_duplicates as it cannot hold duplicates')
holder = type(index)
unique_values = list(set(index))
dtype = index.dtype if is_numeric_dtype(index) else None
unique_idx = holder(unique_values, dtype=dtype)
n = len(unique_idx)
duplicated_selection = np.random.default_rng(2).choice(n, int(n * 1.5))
idx = holder(unique_idx.values[duplicated_selection])
expected_duplicated = pd.Series(duplicated_selection).duplicated(keep=keep).values
tm.assert_numpy_array_equal(idx.duplicated(keep=keep), expected_duplicated)
expected_dropped = holder(pd.Series(idx).drop_duplicates(keep=keep))
tm.assert_index_equal(idx.drop_duplicates(keep=keep), expected_dropped)
```

## Next Steps


---

*Source: test_common.py:303 | Complexity: Advanced | Last updated: 2026-06-02*