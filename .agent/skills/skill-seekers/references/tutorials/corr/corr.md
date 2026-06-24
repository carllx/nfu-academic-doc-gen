# How To: Corr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test corr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series, dtype
```

## Step-by-Step Guide

### Step 1: Assign stats = pytest.importorskip(...)

```python
stats = pytest.importorskip('scipy.stats')
```

**Verification:**
```python
assert isna(datetime_series[:15].corr(datetime_series[5:], min_periods=12))
```

### Step 2: Assign datetime_series = datetime_series.astype(...)

```python
datetime_series = datetime_series.astype(dtype)
```

**Verification:**
```python
assert isna(ts1.corr(ts2, min_periods=12))
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(datetime_series.corr(datetime_series), 1)
```

**Verification:**
```python
assert np.isnan(datetime_series[::2].corr(datetime_series[1::2]))
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(datetime_series[:15].corr(datetime_series[5:]), 1)
```

**Verification:**
```python
assert isna(cp.corr(cp))
```

### Step 5: Assign ts1 = unknown.reindex(...)

```python
ts1 = datetime_series[:15].reindex(datetime_series.index)
```

### Step 6: Assign ts2 = unknown.reindex(...)

```python
ts2 = datetime_series[5:].reindex(datetime_series.index)
```

**Verification:**
```python
assert isna(ts1.corr(ts2, min_periods=12))
```

### Step 7: Assign cp = unknown.copy(...)

```python
cp = datetime_series[:10].copy()
```

### Step 8: Assign unknown = value

```python
cp[:] = np.nan
```

**Verification:**
```python
assert isna(cp.corr(cp))
```

### Step 9: Assign A = Series(...)

```python
A = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
```

### Step 10: Assign B = A.copy(...)

```python
B = A.copy()
```

### Step 11: Assign result = A.corr(...)

```python
result = A.corr(B)
```

### Step 12: Assign unknown = stats.pearsonr(...)

```python
expected, _ = stats.pearsonr(A, B)
```

### Step 13: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series, dtype

# Workflow
stats = pytest.importorskip('scipy.stats')
datetime_series = datetime_series.astype(dtype)
tm.assert_almost_equal(datetime_series.corr(datetime_series), 1)
tm.assert_almost_equal(datetime_series[:15].corr(datetime_series[5:]), 1)
assert isna(datetime_series[:15].corr(datetime_series[5:], min_periods=12))
ts1 = datetime_series[:15].reindex(datetime_series.index)
ts2 = datetime_series[5:].reindex(datetime_series.index)
assert isna(ts1.corr(ts2, min_periods=12))
assert np.isnan(datetime_series[::2].corr(datetime_series[1::2]))
cp = datetime_series[:10].copy()
cp[:] = np.nan
assert isna(cp.corr(cp))
A = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10), name='ts')
B = A.copy()
result = A.corr(B)
expected, _ = stats.pearsonr(A, B)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_cov_corr.py:60 | Complexity: Advanced | Last updated: 2026-06-02*