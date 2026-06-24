# How To: Setitem With Array With Missing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem with array with missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.string_`
- `pandas.core.arrays.string_arrow`
- `pyarrow`
- `pyarrow.compute`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array(['a', 'b', 'c'], dtype=dtype)
```

### Step 2: Assign value = np.array(...)

```python
value = np.array(['A', None])
```

### Step 3: Assign value_orig = value.copy(...)

```python
value_orig = value.copy()
```

### Step 4: Assign unknown = value

```python
arr[[0, 1]] = value
```

### Step 5: Assign expected = pd.array(...)

```python
expected = pd.array(['A', pd.NA, 'c'], dtype=dtype)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(arr, expected)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(value, value_orig)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
arr = pd.array(['a', 'b', 'c'], dtype=dtype)
value = np.array(['A', None])
value_orig = value.copy()
arr[[0, 1]] = value
expected = pd.array(['A', pd.NA, 'c'], dtype=dtype)
tm.assert_extension_array_equal(arr, expected)
tm.assert_numpy_array_equal(value, value_orig)
```

## Next Steps


---

*Source: test_string.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*