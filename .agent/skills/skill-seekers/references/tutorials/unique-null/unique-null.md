# How To: Unique Null

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unique null

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: null_obj, index_or_series_obj
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series_obj

```python
obj = index_or_series_obj
```

### Step 2: Assign values = value

```python
values = obj._values
```

### Step 3: Assign unknown = null_obj

```python
values[0:2] = null_obj
```

### Step 4: Assign klass = type(...)

```python
klass = type(obj)
```

### Step 5: Assign repeated_values = np.repeat(...)

```python
repeated_values = np.repeat(values, range(1, len(values) + 1))
```

### Step 6: Assign obj = klass(...)

```python
obj = klass(repeated_values, dtype=obj.dtype)
```

### Step 7: Assign result = obj.unique(...)

```python
result = obj.unique()
```

### Step 8: Assign unique_values_raw = dict.fromkeys(...)

```python
unique_values_raw = dict.fromkeys(obj.values)
```

### Step 9: Assign unique_values_not_null = value

```python
unique_values_not_null = [val for val in unique_values_raw if not pd.isnull(val)]
```

### Step 10: Assign unique_values = value

```python
unique_values = [null_obj] + unique_values_not_null
```

### Step 11: Call pytest.skip()

```python
pytest.skip("type doesn't allow for NA operations")
```

### Step 12: Assign expected = pd.Index(...)

```python
expected = pd.Index(unique_values, dtype=obj.dtype)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 14: Assign expected = np.array(...)

```python
expected = np.array(unique_values, dtype=obj.dtype)
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 16: Call pytest.skip()

```python
pytest.skip("Test doesn't make sense on empty data")
```

### Step 17: Assign result = result.normalize(...)

```python
result = result.normalize()
```

### Step 18: Assign expected = expected.normalize(...)

```python
expected = expected.normalize()
```

### Step 19: Call pytest.skip()

```python
pytest.skip(f"MultiIndex can't hold '{null_obj}'")
```


## Complete Example

```python
# Setup
# Fixtures: null_obj, index_or_series_obj

# Workflow
obj = index_or_series_obj
if not allow_na_ops(obj):
    pytest.skip("type doesn't allow for NA operations")
elif len(obj) < 1:
    pytest.skip("Test doesn't make sense on empty data")
elif isinstance(obj, pd.MultiIndex):
    pytest.skip(f"MultiIndex can't hold '{null_obj}'")
values = obj._values
values[0:2] = null_obj
klass = type(obj)
repeated_values = np.repeat(values, range(1, len(values) + 1))
obj = klass(repeated_values, dtype=obj.dtype)
result = obj.unique()
unique_values_raw = dict.fromkeys(obj.values)
unique_values_not_null = [val for val in unique_values_raw if not pd.isnull(val)]
unique_values = [null_obj] + unique_values_not_null
if isinstance(obj, pd.Index):
    expected = pd.Index(unique_values, dtype=obj.dtype)
    if isinstance(obj.dtype, pd.DatetimeTZDtype):
        result = result.normalize()
        expected = expected.normalize()
    tm.assert_index_equal(result, expected, exact=True)
else:
    expected = np.array(unique_values, dtype=obj.dtype)
    tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_unique.py:33 | Complexity: Advanced | Last updated: 2026-06-02*