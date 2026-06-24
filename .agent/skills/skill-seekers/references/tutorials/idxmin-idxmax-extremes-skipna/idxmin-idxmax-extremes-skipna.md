# How To: Idxmin Idxmax Extremes Skipna

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test idxmin idxmax extremes skipna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: skipna, how, float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign min_value = value

```python
min_value = np.finfo(float_numpy_dtype).min
```

### Step 2: Assign max_value = value

```python
max_value = np.finfo(float_numpy_dtype).max
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Series(np.repeat(range(1, 6), repeats=2), dtype='intp'), 'b': Series([np.nan, min_value, np.nan, max_value, min_value, np.nan, max_value, np.nan, np.nan, np.nan], dtype=float_numpy_dtype)})
```

### Step 4: Assign gb = df.groupby(...)

```python
gb = df.groupby('a')
```

### Step 5: Assign warn = value

```python
warn = None if skipna else FutureWarning
```

### Step 6: Assign msg = value

```python
msg = f'The behavior of DataFrameGroupBy.{how} with all-NA values'
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': values}, index=pd.Index(range(1, 6), name='a', dtype='intp'))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = getattr(...)

```python
result = getattr(gb, how)(skipna=skipna)
```

### Step 10: Assign values = value

```python
values = [1, 3, 4, 6, np.nan]
```

### Step 11: Assign values = value

```python
values = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: skipna, how, float_numpy_dtype

# Workflow
min_value = np.finfo(float_numpy_dtype).min
max_value = np.finfo(float_numpy_dtype).max
df = DataFrame({'a': Series(np.repeat(range(1, 6), repeats=2), dtype='intp'), 'b': Series([np.nan, min_value, np.nan, max_value, min_value, np.nan, max_value, np.nan, np.nan, np.nan], dtype=float_numpy_dtype)})
gb = df.groupby('a')
warn = None if skipna else FutureWarning
msg = f'The behavior of DataFrameGroupBy.{how} with all-NA values'
with tm.assert_produces_warning(warn, match=msg):
    result = getattr(gb, how)(skipna=skipna)
if skipna:
    values = [1, 3, 4, 6, np.nan]
else:
    values = np.nan
expected = DataFrame({'b': values}, index=pd.Index(range(1, 6), name='a', dtype='intp'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:224 | Complexity: Advanced | Last updated: 2026-06-02*