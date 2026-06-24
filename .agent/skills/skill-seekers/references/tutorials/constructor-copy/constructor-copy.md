# How To: Constructor Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor copy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `functools`
- `math`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`
- `pyarrow`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(list('abc'), name='name')
```

**Verification:**
```python
assert isinstance(new_index, Index)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array(index)
```

**Verification:**
```python
assert new_index.name == 'name'
```

### Step 3: Assign new_index = Index(...)

```python
new_index = Index(arr, copy=True, name='name')
```

**Verification:**
```python
assert new_index[0] != 'SOMEBIGLONGSTRING'
```

### Step 4: Assign unknown = 'SOMEBIGLONGSTRING'

```python
arr[0] = 'SOMEBIGLONGSTRING'
```

**Verification:**
```python
assert new_index[0] != 'SOMEBIGLONGSTRING'
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(new_index.values, pd.array(arr, dtype='str'))
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, new_index.values)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
index = Index(list('abc'), name='name')
arr = np.array(index)
new_index = Index(arr, copy=True, name='name')
assert isinstance(new_index, Index)
assert new_index.name == 'name'
if using_infer_string:
    tm.assert_extension_array_equal(new_index.values, pd.array(arr, dtype='str'))
else:
    tm.assert_numpy_array_equal(arr, new_index.values)
arr[0] = 'SOMEBIGLONGSTRING'
assert new_index[0] != 'SOMEBIGLONGSTRING'
```

## Next Steps


---

*Source: test_base.py:74 | Complexity: Intermediate | Last updated: 2026-06-02*