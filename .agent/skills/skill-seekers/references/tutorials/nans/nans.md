# How To: Nans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: q
```

## Step-by-Step Guide

### Step 1: Assign compare_func = partial(...)

```python
compare_func = partial(scoreatpercentile, per=q)
```

**Verification:**
```python
assert isna(result.iloc[23])
```

### Step 2: Assign obj = Series(...)

```python
obj = Series(np.random.default_rng(2).standard_normal(50))
```

**Verification:**
```python
assert not isna(result.iloc[24])
```

### Step 3: Assign unknown = value

```python
obj[:10] = np.nan
```

**Verification:**
```python
assert not isna(result.iloc[-6])
```

### Step 4: Assign unknown = value

```python
obj[-10:] = np.nan
```

**Verification:**
```python
assert isna(result.iloc[-5])
```

### Step 5: Assign result = obj.rolling.quantile(...)

```python
result = obj.rolling(50, min_periods=30).quantile(q)
```

**Verification:**
```python
assert isna(result.iloc[3])
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.iloc[-1], compare_func(obj[10:-10]))
```

**Verification:**
```python
assert notna(result.iloc[4])
```

### Step 7: Assign result = obj.rolling.quantile(...)

```python
result = obj.rolling(20, min_periods=15).quantile(q)
```

**Verification:**
```python
assert isna(result.iloc[23])
```

### Step 8: Assign obj2 = Series(...)

```python
obj2 = Series(np.random.default_rng(2).standard_normal(20))
```

### Step 9: Assign result = obj2.rolling.quantile(...)

```python
result = obj2.rolling(10, min_periods=5).quantile(q)
```

**Verification:**
```python
assert isna(result.iloc[3])
```

### Step 10: Assign result0 = obj.rolling.quantile(...)

```python
result0 = obj.rolling(20, min_periods=0).quantile(q)
```

### Step 11: Assign result1 = obj.rolling.quantile(...)

```python
result1 = obj.rolling(20, min_periods=1).quantile(q)
```

### Step 12: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result0, result1)
```


## Complete Example

```python
# Setup
# Fixtures: q

# Workflow
compare_func = partial(scoreatpercentile, per=q)
obj = Series(np.random.default_rng(2).standard_normal(50))
obj[:10] = np.nan
obj[-10:] = np.nan
result = obj.rolling(50, min_periods=30).quantile(q)
tm.assert_almost_equal(result.iloc[-1], compare_func(obj[10:-10]))
result = obj.rolling(20, min_periods=15).quantile(q)
assert isna(result.iloc[23])
assert not isna(result.iloc[24])
assert not isna(result.iloc[-6])
assert isna(result.iloc[-5])
obj2 = Series(np.random.default_rng(2).standard_normal(20))
result = obj2.rolling(10, min_periods=5).quantile(q)
assert isna(result.iloc[3])
assert notna(result.iloc[4])
result0 = obj.rolling(20, min_periods=0).quantile(q)
result1 = obj.rolling(20, min_periods=1).quantile(q)
tm.assert_almost_equal(result0, result1)
```

## Next Steps


---

*Source: test_rolling_quantile.py:89 | Complexity: Advanced | Last updated: 2026-06-02*