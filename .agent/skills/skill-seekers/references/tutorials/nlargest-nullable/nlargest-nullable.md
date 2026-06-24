# How To: Nlargest Nullable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest nullable

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_numeric_ea_dtype

```python
dtype = any_numeric_ea_dtype
```

### Step 2: Assign arr = arr.astype(...)

```python
arr = arr.astype(dtype.lower(), copy=False)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(arr.copy(), dtype=dtype)
```

### Step 4: Assign unknown = value

```python
ser[1] = pd.NA
```

### Step 5: Assign result = ser.nlargest(...)

```python
result = ser.nlargest(5)
```

### Step 6: Assign expected = Series.nlargest.astype(...)

```python
expected = Series(np.delete(arr, 1), index=ser.index.delete(1)).nlargest(5).astype(dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign arr = np.random.default_rng.integers(...)

```python
arr = np.random.default_rng(2).integers(1, 10, 10)
```

### Step 9: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal(10)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype

# Workflow
dtype = any_numeric_ea_dtype
if dtype.startswith('UInt'):
    arr = np.random.default_rng(2).integers(1, 10, 10)
else:
    arr = np.random.default_rng(2).standard_normal(10)
arr = arr.astype(dtype.lower(), copy=False)
ser = Series(arr.copy(), dtype=dtype)
ser[1] = pd.NA
result = ser.nlargest(5)
expected = Series(np.delete(arr, 1), index=ser.index.delete(1)).nlargest(5).astype(dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:217 | Complexity: Advanced | Last updated: 2026-06-02*