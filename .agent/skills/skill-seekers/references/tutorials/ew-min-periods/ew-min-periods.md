# How To: Ew Min Periods

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ew min periods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: min_periods, name
```

## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal(50)
```

**Verification:**
```python
assert result[:11].isna().all()
```

### Step 2: Assign unknown = value

```python
arr[:10] = np.nan
```

**Verification:**
```python
assert not result[11:].isna().any()
```

### Step 3: Assign unknown = value

```python
arr[-10:] = np.nan
```

**Verification:**
```python
assert result[:10].isna().all()
```

### Step 4: Assign s = Series(...)

```python
s = Series(arr)
```

**Verification:**
```python
assert not result[10:].isna().any()
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(s.ewm(com=50, min_periods=2), name)()
```

**Verification:**
```python
assert result[:11].isna().all()
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(s.ewm(com=50, min_periods=min_periods), name)()
```

**Verification:**
```python
assert not result[11:].isna().any()
```

### Step 7: Assign result = getattr(...)

```python
result = getattr(Series(dtype=object).ewm(com=50, min_periods=min_periods), name)()
```

**Verification:**
```python
assert result2.dtype == np.float64
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series(dtype='float64'))
```

### Step 9: Assign result = getattr(...)

```python
result = getattr(Series([1.0]).ewm(50, min_periods=min_periods), name)()
```

### Step 10: Assign result2 = getattr(...)

```python
result2 = getattr(Series(np.arange(50)).ewm(span=10), name)()
```

**Verification:**
```python
assert result2.dtype == np.float64
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series([1.0]))
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series([np.nan]))
```


## Complete Example

```python
# Setup
# Fixtures: min_periods, name

# Workflow
arr = np.random.default_rng(2).standard_normal(50)
arr[:10] = np.nan
arr[-10:] = np.nan
s = Series(arr)
result = getattr(s.ewm(com=50, min_periods=2), name)()
assert result[:11].isna().all()
assert not result[11:].isna().any()
result = getattr(s.ewm(com=50, min_periods=min_periods), name)()
if name == 'mean':
    assert result[:10].isna().all()
    assert not result[10:].isna().any()
else:
    assert result[:11].isna().all()
    assert not result[11:].isna().any()
result = getattr(Series(dtype=object).ewm(com=50, min_periods=min_periods), name)()
tm.assert_series_equal(result, Series(dtype='float64'))
result = getattr(Series([1.0]).ewm(50, min_periods=min_periods), name)()
if name == 'mean':
    tm.assert_series_equal(result, Series([1.0]))
else:
    tm.assert_series_equal(result, Series([np.nan]))
result2 = getattr(Series(np.arange(50)).ewm(span=10), name)()
assert result2.dtype == np.float64
```

## Next Steps


---

*Source: test_ewm.py:486 | Complexity: Advanced | Last updated: 2026-06-02*