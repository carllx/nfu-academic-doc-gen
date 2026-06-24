# How To: Group Ohlc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test group ohlc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.groupby`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign obj = np.array(...)

```python
obj = np.array(np.random.default_rng(2).standard_normal(20), dtype=dtype)
```

### Step 2: Assign bins = np.array(...)

```python
bins = np.array([6, 12, 20])
```

### Step 3: Assign out = np.zeros(...)

```python
out = np.zeros((3, 4), dtype)
```

### Step 4: Assign counts = np.zeros(...)

```python
counts = np.zeros(len(out), dtype=np.int64)
```

### Step 5: Assign labels = ensure_platform_int(...)

```python
labels = ensure_platform_int(np.repeat(np.arange(3), np.diff(np.r_[0, bins])))
```

### Step 6: Assign func = value

```python
func = libgroupby.group_ohlc
```

### Step 7: Call func()

```python
func(out, counts, obj[:, None], labels)
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([_ohlc(obj[:6]), _ohlc(obj[6:12]), _ohlc(obj[12:])])
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(out, expected)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(counts, np.array([6, 6, 8], dtype=np.int64))
```

### Step 11: Assign unknown = value

```python
obj[:6] = np.nan
```

### Step 12: Call func()

```python
func(out, counts, obj[:, None], labels)
```

### Step 13: Assign unknown = value

```python
expected[0] = np.nan
```

### Step 14: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(out, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
obj = np.array(np.random.default_rng(2).standard_normal(20), dtype=dtype)
bins = np.array([6, 12, 20])
out = np.zeros((3, 4), dtype)
counts = np.zeros(len(out), dtype=np.int64)
labels = ensure_platform_int(np.repeat(np.arange(3), np.diff(np.r_[0, bins])))
func = libgroupby.group_ohlc
func(out, counts, obj[:, None], labels)

def _ohlc(group):
    if isna(group).all():
        return np.repeat(np.nan, 4)
    return [group[0], group.max(), group.min(), group[-1]]
expected = np.array([_ohlc(obj[:6]), _ohlc(obj[6:12]), _ohlc(obj[12:])])
tm.assert_almost_equal(out, expected)
tm.assert_numpy_array_equal(counts, np.array([6, 6, 8], dtype=np.int64))
obj[:6] = np.nan
func(out, counts, obj[:, None], labels)
expected[0] = np.nan
tm.assert_almost_equal(out, expected)
```

## Next Steps


---

*Source: test_libgroupby.py:135 | Complexity: Advanced | Last updated: 2026-06-02*