# How To: Numeric Ea Axis 1

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric ea axis 1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: method, skipna, min_count, any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series([0, 1, 2, 3], dtype=any_numeric_ea_dtype), 'b': Series([0, 1, pd.NA, 3], dtype=any_numeric_ea_dtype)})
```

### Step 2: Assign expected_df = DataFrame(...)

```python
expected_df = DataFrame({'a': [0.0, 1.0, 2.0, 3.0], 'b': [0.0, 1.0, np.nan, 3.0]})
```

### Step 3: Assign kwargs = value

```python
kwargs = {}
```

### Step 4: Assign warn = None

```python
warn = None
```

### Step 5: Assign msg = None

```python
msg = None
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign expected_dtype = 'int64'

```python
expected_dtype = 'int64'
```

### Step 8: Assign unknown = skipna

```python
kwargs['skipna'] = skipna
```

### Step 9: Assign unknown = min_count

```python
kwargs['min_count'] = min_count
```

### Step 10: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 11: Assign msg = value

```python
msg = f'The behavior of DataFrame.{method} with all-NA values'
```

### Step 12: Assign result = getattr(...)

```python
result = getattr(df, method)(axis=1, **kwargs)
```

### Step 13: Assign expected = getattr(...)

```python
expected = getattr(expected_df, method)(axis=1, **kwargs)
```

### Step 14: Assign expected = expected.astype(...)

```python
expected = expected.astype(expected_dtype)
```

### Step 15: Assign expected_dtype = 'boolean'

```python
expected_dtype = 'boolean'
```

### Step 16: Assign expected_dtype = 'Float64'

```python
expected_dtype = 'Float64'
```

### Step 17: Assign expected_dtype = any_numeric_ea_dtype

```python
expected_dtype = any_numeric_ea_dtype
```


## Complete Example

```python
# Setup
# Fixtures: method, skipna, min_count, any_numeric_ea_dtype

# Workflow
df = DataFrame({'a': Series([0, 1, 2, 3], dtype=any_numeric_ea_dtype), 'b': Series([0, 1, pd.NA, 3], dtype=any_numeric_ea_dtype)})
expected_df = DataFrame({'a': [0.0, 1.0, 2.0, 3.0], 'b': [0.0, 1.0, np.nan, 3.0]})
if method in ('count', 'nunique'):
    expected_dtype = 'int64'
elif method in ('all', 'any'):
    expected_dtype = 'boolean'
elif method in ('kurt', 'kurtosis', 'mean', 'median', 'sem', 'skew', 'std', 'var') and (not any_numeric_ea_dtype.startswith('Float')):
    expected_dtype = 'Float64'
else:
    expected_dtype = any_numeric_ea_dtype
kwargs = {}
if method not in ('count', 'nunique', 'quantile'):
    kwargs['skipna'] = skipna
if method in ('prod', 'product', 'sum'):
    kwargs['min_count'] = min_count
warn = None
msg = None
if not skipna and method in ('idxmax', 'idxmin'):
    warn = FutureWarning
    msg = f'The behavior of DataFrame.{method} with all-NA values'
with tm.assert_produces_warning(warn, match=msg):
    result = getattr(df, method)(axis=1, **kwargs)
with tm.assert_produces_warning(warn, match=msg):
    expected = getattr(expected_df, method)(axis=1, **kwargs)
if method not in ('idxmax', 'idxmin'):
    expected = expected.astype(expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:2084 | Complexity: Advanced | Last updated: 2026-06-02*