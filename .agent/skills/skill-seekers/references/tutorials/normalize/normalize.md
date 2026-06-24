# How To: Normalize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test normalize

## Prerequisites

**Required Modules:**
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 9:30', periods=10, freq='D')
```

**Verification:**
```python
assert result.is_normalized
```

### Step 2: Assign result = rng.normalize(...)

```python
result = rng.normalize()
```

**Verification:**
```python
assert not rng.is_normalized
```

### Step 3: Assign expected = date_range(...)

```python
expected = date_range('1/1/2000', periods=10, freq='D')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign arr_ns = np.array.astype(...)

```python
arr_ns = np.array([1380585623454345752, 1380585612343234312]).astype('datetime64[ns]')
```

### Step 6: Assign rng_ns = DatetimeIndex(...)

```python
rng_ns = DatetimeIndex(arr_ns)
```

### Step 7: Assign rng_ns_normalized = rng_ns.normalize(...)

```python
rng_ns_normalized = rng_ns.normalize()
```

### Step 8: Assign arr_ns = np.array.astype(...)

```python
arr_ns = np.array([1380585600000000000, 1380585600000000000]).astype('datetime64[ns]')
```

### Step 9: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(arr_ns)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng_ns_normalized, expected)
```

**Verification:**
```python
assert result.is_normalized
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000 9:30', periods=10, freq='D')
result = rng.normalize()
expected = date_range('1/1/2000', periods=10, freq='D')
tm.assert_index_equal(result, expected)
arr_ns = np.array([1380585623454345752, 1380585612343234312]).astype('datetime64[ns]')
rng_ns = DatetimeIndex(arr_ns)
rng_ns_normalized = rng_ns.normalize()
arr_ns = np.array([1380585600000000000, 1380585600000000000]).astype('datetime64[ns]')
expected = DatetimeIndex(arr_ns)
tm.assert_index_equal(rng_ns_normalized, expected)
assert result.is_normalized
assert not rng.is_normalized
```

## Next Steps


---

*Source: test_normalize.py:17 | Complexity: Advanced | Last updated: 2026-06-02*