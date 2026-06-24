# How To: Mul

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mul

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
a = pd.array(['a', 'b', None], dtype=dtype)
```

### Step 2: Assign result = value

```python
result = a * 2
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(['aa', 'bb', None], dtype=dtype)
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = 2 * a
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
a = pd.array(['a', 'b', None], dtype=dtype)
result = a * 2
expected = pd.array(['aa', 'bb', None], dtype=dtype)
tm.assert_extension_array_equal(result, expected)
result = 2 * a
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_string.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*