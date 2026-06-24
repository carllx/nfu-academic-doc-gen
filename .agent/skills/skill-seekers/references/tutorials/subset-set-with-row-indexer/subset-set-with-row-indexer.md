# How To: Subset Set With Row Indexer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subset set with row indexer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: backend, indexer_si, indexer, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign unknown = backend

```python
_, DataFrame, _ = backend
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3, 4], 'b': [4, 5, 6, 7], 'c': [0.1, 0.2, 0.3, 0.4]})
```

### Step 3: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 4: Assign subset = value

```python
subset = df[1:4]
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [0, 0, 4], 'b': [0, 0, 7], 'c': [0.0, 0.0, 0.4]}, index=range(1, 4))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

### Step 7: Call pytest.skip()

```python
pytest.skip('setitem with labels selects on columns')
```

### Step 8: Assign unknown = 0

```python
indexer_si(subset)[indexer] = 0
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 10: Assign unknown = 0

```python
df_orig[1:3] = 0
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 12: Assign warn = value

```python
warn = SettingWithCopyWarning if indexer_si is tm.setitem else None
```

### Step 13: Assign unknown = 0

```python
indexer_si(subset)[indexer] = 0
```

### Step 14: Assign unknown = 0

```python
indexer_si(subset)[indexer] = 0
```


## Complete Example

```python
# Setup
# Fixtures: backend, indexer_si, indexer, using_copy_on_write, warn_copy_on_write

# Workflow
_, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3, 4], 'b': [4, 5, 6, 7], 'c': [0.1, 0.2, 0.3, 0.4]})
df_orig = df.copy()
subset = df[1:4]
if indexer_si is tm.setitem and isinstance(indexer, np.ndarray) and (indexer.dtype == 'int'):
    pytest.skip('setitem with labels selects on columns')
if using_copy_on_write:
    indexer_si(subset)[indexer] = 0
elif warn_copy_on_write:
    with tm.assert_cow_warning():
        indexer_si(subset)[indexer] = 0
else:
    warn = SettingWithCopyWarning if indexer_si is tm.setitem else None
    with pd.option_context('chained_assignment', 'warn'):
        with tm.assert_produces_warning(warn):
            indexer_si(subset)[indexer] = 0
expected = DataFrame({'a': [0, 0, 4], 'b': [0, 0, 7], 'c': [0.0, 0.0, 0.4]}, index=range(1, 4))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    df_orig[1:3] = 0
    tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:319 | Complexity: Advanced | Last updated: 2026-06-02*