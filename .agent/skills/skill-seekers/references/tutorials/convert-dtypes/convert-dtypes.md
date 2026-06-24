# How To: Convert Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test convert dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: test_cases, params, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign unknown = test_cases

```python
data, maindtype, expected_default, expected_other = test_cases
```

### Step 2: Assign result = series.convert_dtypes(...)

```python
result = series.convert_dtypes(*params)
```

### Step 3: Assign param_names = value

```python
param_names = ['infer_objects', 'convert_string', 'convert_integer', 'convert_boolean', 'convert_floating']
```

### Step 4: Assign params_dict = dict(...)

```python
params_dict = dict(zip(param_names, params))
```

### Step 5: Assign expected_dtype = expected_default

```python
expected_dtype = expected_default
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series(data, dtype=expected_dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign copy = series.copy(...)

```python
copy = series.copy(deep=True)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(series, copy)
```

### Step 10: Assign msg = 'Cannot use .astype to convert from timezone-naive dtype'

```python
msg = 'Cannot use .astype to convert from timezone-naive dtype'
```

### Step 11: Assign series = pd.Series(...)

```python
series = pd.Series(data, dtype=maindtype)
```

### Step 12: Assign series = pd.Series(...)

```python
series = pd.Series(data)
```

### Step 13: Assign expected_dtype = pd.StringDtype(...)

```python
expected_dtype = pd.StringDtype(na_value=np.nan)
```

### Step 14: Assign unknown = value

```python
result[result.notna()] = np.nan
```

### Step 15: Call pd.Series()

```python
pd.Series(data, dtype=maindtype)
```

### Step 16: Assign expected_dtype = dtype

```python
expected_dtype = dtype
```

### Step 17: Assign unknown = value

```python
result[result.notna()] = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: test_cases, params, using_infer_string

# Workflow
data, maindtype, expected_default, expected_other = test_cases
if hasattr(data, 'dtype') and lib.is_np_dtype(data.dtype, 'M') and isinstance(maindtype, pd.DatetimeTZDtype):
    msg = 'Cannot use .astype to convert from timezone-naive dtype'
    with pytest.raises(TypeError, match=msg):
        pd.Series(data, dtype=maindtype)
    return
if maindtype is not None:
    series = pd.Series(data, dtype=maindtype)
else:
    series = pd.Series(data)
result = series.convert_dtypes(*params)
param_names = ['infer_objects', 'convert_string', 'convert_integer', 'convert_boolean', 'convert_floating']
params_dict = dict(zip(param_names, params))
expected_dtype = expected_default
for spec, dtype in expected_other.items():
    if all((params_dict[key] is val for key, val in zip(spec[::2], spec[1::2]))):
        expected_dtype = dtype
if using_infer_string and expected_default == 'string' and (expected_dtype == object) and params[0] and (not params[1]):
    expected_dtype = pd.StringDtype(na_value=np.nan)
expected = pd.Series(data, dtype=expected_dtype)
tm.assert_series_equal(result, expected)
copy = series.copy(deep=True)
if result.notna().sum() > 0 and result.dtype in ['interval[int64, right]']:
    with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
        result[result.notna()] = np.nan
else:
    result[result.notna()] = np.nan
tm.assert_series_equal(series, copy)
```

## Next Steps


---

*Source: test_convert_dtypes.py:188 | Complexity: Advanced | Last updated: 2026-06-02*