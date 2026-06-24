# How To: Append Hierarchical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append hierarchical

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path, multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign df = multiindex_dataframe_random_data

```python
df = multiindex_dataframe_random_data
```

### Step 2: Assign df.columns.name = None

```python
df.columns.name = None
```

### Step 3: Assign path = value

```python
path = tmp_path / 'test.hdf'
```

### Step 4: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table')
```

### Step 5: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df', columns=['A', 'B'])
```

### Step 6: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=['A', 'B'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call store.append()

```python
store.append('mi', df)
```

### Step 9: Assign result = store.select(...)

```python
result = store.select('mi')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df)
```

### Step 11: Assign result = store.select(...)

```python
result = store.select('mi', columns=['A', 'B'])
```

### Step 12: Assign expected = df.reindex(...)

```python
expected = df.reindex(columns=['A', 'B'])
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path, multiindex_dataframe_random_data

# Workflow
df = multiindex_dataframe_random_data
df.columns.name = None
with ensure_clean_store(setup_path) as store:
    store.append('mi', df)
    result = store.select('mi')
    tm.assert_frame_equal(result, df)
    result = store.select('mi', columns=['A', 'B'])
    expected = df.reindex(columns=['A', 'B'])
    tm.assert_frame_equal(result, expected)
path = tmp_path / 'test.hdf'
df.to_hdf(path, key='df', format='table')
result = read_hdf(path, 'df', columns=['A', 'B'])
expected = df.reindex(columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:663 | Complexity: Advanced | Last updated: 2026-06-02*