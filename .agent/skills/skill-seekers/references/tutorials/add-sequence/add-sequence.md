# How To: Add Sequence

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add sequence

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

### Step 1: Assign a = pd.array(...)

```python
a = pd.array(['a', 'b', None, None], dtype=dtype)
```

### Step 2: Assign other = value

```python
other = ['x', None, 'y', None]
```

### Step 3: Assign result = value

```python
result = a + other
```

### Step 4: Assign expected = pd.array(...)

```python
expected = pd.array(['ax', None, None, None], dtype=dtype)
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = other + a
```

### Step 7: Assign expected = pd.array(...)

```python
expected = pd.array(['xa', None, None, None], dtype=dtype)
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
a = pd.array(['a', 'b', None, None], dtype=dtype)
other = ['x', None, 'y', None]
result = a + other
expected = pd.array(['ax', None, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)
result = other + a
expected = pd.array(['xa', None, None, None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_string.py:233 | Complexity: Advanced | Last updated: 2026-06-02*