# How To: Add

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add

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

### Step 1: Assign a = pd.Series(...)

```python
a = pd.Series(['a', 'b', 'c', None, None], dtype=dtype)
```

### Step 2: Assign b = pd.Series(...)

```python
b = pd.Series(['x', 'y', None, 'z', None], dtype=dtype)
```

### Step 3: Assign result = value

```python
result = a + b
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(['ax', 'by', None, None, None], dtype=dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = a.add(...)

```python
result = a.add(b)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = a.radd(...)

```python
result = a.radd(b)
```

### Step 9: Assign expected = pd.Series(...)

```python
expected = pd.Series(['xa', 'yb', None, None, None], dtype=dtype)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = a.add(...)

```python
result = a.add(b, fill_value='-')
```

### Step 12: Assign expected = pd.Series(...)

```python
expected = pd.Series(['ax', 'by', 'c-', '-z', None], dtype=dtype)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
a = pd.Series(['a', 'b', 'c', None, None], dtype=dtype)
b = pd.Series(['x', 'y', None, 'z', None], dtype=dtype)
result = a + b
expected = pd.Series(['ax', 'by', None, None, None], dtype=dtype)
tm.assert_series_equal(result, expected)
result = a.add(b)
tm.assert_series_equal(result, expected)
result = a.radd(b)
expected = pd.Series(['xa', 'yb', None, None, None], dtype=dtype)
tm.assert_series_equal(result, expected)
result = a.add(b, fill_value='-')
expected = pd.Series(['ax', 'by', 'c-', '-z', None], dtype=dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_string.py:197 | Complexity: Advanced | Last updated: 2026-06-02*