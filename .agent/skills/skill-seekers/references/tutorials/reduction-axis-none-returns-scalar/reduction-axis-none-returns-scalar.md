# How To: Reduction Axis None Returns Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reduction axis none returns scalar

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
# Fixtures: method, numeric_only, dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), dtype=dtype)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(df, method)(axis=None, numeric_only=numeric_only)
```

### Step 3: Assign np_arr = df.to_numpy(...)

```python
np_arr = df.to_numpy(dtype=np.float64)
```

### Step 4: Assign comp_mod = pytest.importorskip(...)

```python
comp_mod = pytest.importorskip('scipy.stats')
```

### Step 5: Assign expected = getattr(...)

```python
expected = getattr(comp_mod, method)(np_arr, bias=False, axis=None)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Assign expected = getattr(...)

```python
expected = getattr(np, method)(np_arr, axis=None)
```

**Verification:**
```python
assert result == expected
```

### Step 8: Assign method = 'kurtosis'

```python
method = 'kurtosis'
```


## Complete Example

```python
# Setup
# Fixtures: method, numeric_only, dtype

# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((4, 4)), dtype=dtype)
result = getattr(df, method)(axis=None, numeric_only=numeric_only)
np_arr = df.to_numpy(dtype=np.float64)
if method in {'skew', 'kurt'}:
    comp_mod = pytest.importorskip('scipy.stats')
    if method == 'kurt':
        method = 'kurtosis'
    expected = getattr(comp_mod, method)(np_arr, bias=False, axis=None)
    tm.assert_almost_equal(result, expected)
else:
    expected = getattr(np, method)(np_arr, axis=None)
    assert result == expected
```

## Next Steps


---

*Source: test_reductions.py:1991 | Complexity: Advanced | Last updated: 2026-06-02*