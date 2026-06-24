# How To: Concat Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: request, to_concat_dtypes, result_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser_list = value

```python
ser_list = [pd.Series(['a', 'b', None], dtype=pd.StringDtype(storage, na_value)) for storage, na_value in to_concat_dtypes]
```

### Step 2: Assign result = pd.concat(...)

```python
result = pd.concat(ser_list, ignore_index=True)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(['a', 'b', None, 'a', 'b', None], dtype=pd.StringDtype(*result_dtype))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat(ser_list[::1], ignore_index=True)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Call pytest.skip()

```python
pytest.skip("Could not import 'pyarrow'")
```


## Complete Example

```python
# Setup
# Fixtures: request, to_concat_dtypes, result_dtype

# Workflow
if any((storage == 'pyarrow' for storage, _ in to_concat_dtypes)) and (not HAS_PYARROW):
    pytest.skip("Could not import 'pyarrow'")
ser_list = [pd.Series(['a', 'b', None], dtype=pd.StringDtype(storage, na_value)) for storage, na_value in to_concat_dtypes]
result = pd.concat(ser_list, ignore_index=True)
expected = pd.Series(['a', 'b', None, 'a', 'b', None], dtype=pd.StringDtype(*result_dtype))
tm.assert_series_equal(result, expected)
result = pd.concat(ser_list[::1], ignore_index=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*