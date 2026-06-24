# How To: Idxmin Idxmax Extremes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test idxmin idxmax extremes

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
# Fixtures: how, any_real_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign info = value

```python
info = np.iinfo if 'int' in any_real_numpy_dtype else np.finfo
```

### Step 2: Assign min_value = value

```python
min_value = info(any_real_numpy_dtype).min
```

### Step 3: Assign max_value = value

```python
max_value = info(any_real_numpy_dtype).max
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [2, 1, 1, 2], 'b': [min_value, max_value, max_value, min_value]}, dtype=any_real_numpy_dtype)
```

### Step 5: Assign gb = df.groupby(...)

```python
gb = df.groupby('a')
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(gb, how)()
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [1, 0]}, index=pd.Index([1, 2], name='a', dtype=any_real_numpy_dtype))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: how, any_real_numpy_dtype

# Workflow
if any_real_numpy_dtype is int or any_real_numpy_dtype is float:
    return
info = np.iinfo if 'int' in any_real_numpy_dtype else np.finfo
min_value = info(any_real_numpy_dtype).min
max_value = info(any_real_numpy_dtype).max
df = DataFrame({'a': [2, 1, 1, 2], 'b': [min_value, max_value, max_value, min_value]}, dtype=any_real_numpy_dtype)
gb = df.groupby('a')
result = getattr(gb, how)()
expected = DataFrame({'b': [1, 0]}, index=pd.Index([1, 2], name='a', dtype=any_real_numpy_dtype))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:203 | Complexity: Advanced | Last updated: 2026-06-02*