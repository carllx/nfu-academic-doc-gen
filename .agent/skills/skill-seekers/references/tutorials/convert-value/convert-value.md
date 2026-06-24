# How To: Convert Value

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test convert value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path, where, df, expected
```

## Step-by-Step Guide

### Step 1: Assign df.col = df.col.astype(...)

```python
df.col = df.col.astype('category')
```

### Step 2: Assign max_widths = value

```python
max_widths = {'col': 1}
```

### Step 3: Assign categorical_values = sorted(...)

```python
categorical_values = sorted(df.col.unique())
```

### Step 4: Assign expected.col = expected.col.astype(...)

```python
expected.col = expected.col.astype('category')
```

### Step 5: Assign expected.col = expected.col.cat.set_categories(...)

```python
expected.col = expected.col.cat.set_categories(categorical_values)
```

### Step 6: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table', min_itemsize=max_widths)
```

### Step 8: Assign result = read_hdf(...)

```python
result = read_hdf(path, where=where)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path, where, df, expected

# Workflow
df.col = df.col.astype('category')
max_widths = {'col': 1}
categorical_values = sorted(df.col.unique())
expected.col = expected.col.astype('category')
expected.col = expected.col.cat.set_categories(categorical_values)
path = tmp_path / setup_path
df.to_hdf(path, key='df', format='table', min_itemsize=max_widths)
result = read_hdf(path, where=where)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:200 | Complexity: Advanced | Last updated: 2026-06-02*