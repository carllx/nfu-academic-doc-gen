# How To: Categorical Nan Only Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical nan only columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.tests.io.pytables.common`

**Setup Required:**
```python
# Fixtures: tmp_path, setup_path
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', 'b', 'c', np.nan], 'b': [np.nan, np.nan, np.nan, np.nan], 'c': [1, 2, 3, 4], 'd': Series([None] * 4, dtype=object)})
```

### Step 2: Assign unknown = df.a.astype(...)

```python
df['a'] = df.a.astype('category')
```

### Step 3: Assign unknown = df.b.astype(...)

```python
df['b'] = df.b.astype('category')
```

### Step 4: Assign unknown = df.b.astype(...)

```python
df['d'] = df.b.astype('category')
```

### Step 5: Assign expected = df

```python
expected = df
```

### Step 6: Assign path = value

```python
path = tmp_path / setup_path
```

### Step 7: Call df.to_hdf()

```python
df.to_hdf(path, key='df', format='table', data_columns=True)
```

### Step 8: Assign result = read_hdf(...)

```python
result = read_hdf(path, 'df')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path, setup_path

# Workflow
df = DataFrame({'a': ['a', 'b', 'c', np.nan], 'b': [np.nan, np.nan, np.nan, np.nan], 'c': [1, 2, 3, 4], 'd': Series([None] * 4, dtype=object)})
df['a'] = df.a.astype('category')
df['b'] = df.b.astype('category')
df['d'] = df.b.astype('category')
expected = df
path = tmp_path / setup_path
df.to_hdf(path, key='df', format='table', data_columns=True)
result = read_hdf(path, 'df')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:171 | Complexity: Advanced | Last updated: 2026-06-02*