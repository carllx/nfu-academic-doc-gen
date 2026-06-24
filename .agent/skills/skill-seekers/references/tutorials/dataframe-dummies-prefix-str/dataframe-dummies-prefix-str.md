# How To: Dataframe Dummies Prefix Str

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe dummies prefix str

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: df, sparse
```

## Step-by-Step Guide

### Step 1: Assign result = get_dummies(...)

```python
result = get_dummies(df, prefix='bad', sparse=sparse)
```

### Step 2: Assign bad_columns = value

```python
bad_columns = ['bad_a', 'bad_b', 'bad_b', 'bad_c']
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, True, False, True, False], [2, False, True, True, False], [3, True, False, False, True]], columns=['C'] + bad_columns)
```

### Step 4: Assign expected = expected.astype(...)

```python
expected = expected.astype({'C': np.int64})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = pd.concat(...)

```python
expected = pd.concat([Series([1, 2, 3], name='C'), Series([True, False, True], name='bad_a', dtype='Sparse[bool]'), Series([False, True, False], name='bad_b', dtype='Sparse[bool]'), Series([True, True, False], name='bad_b', dtype='Sparse[bool]'), Series([False, False, True], name='bad_c', dtype='Sparse[bool]')], axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: df, sparse

# Workflow
result = get_dummies(df, prefix='bad', sparse=sparse)
bad_columns = ['bad_a', 'bad_b', 'bad_b', 'bad_c']
expected = DataFrame([[1, True, False, True, False], [2, False, True, True, False], [3, True, False, False, True]], columns=['C'] + bad_columns)
expected = expected.astype({'C': np.int64})
if sparse:
    expected = pd.concat([Series([1, 2, 3], name='C'), Series([True, False, True], name='bad_a', dtype='Sparse[bool]'), Series([False, True, False], name='bad_b', dtype='Sparse[bool]'), Series([True, True, False], name='bad_b', dtype='Sparse[bool]'), Series([False, False, True], name='bad_c', dtype='Sparse[bool]')], axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_get_dummies.py:278 | Complexity: Intermediate | Last updated: 2026-06-02*