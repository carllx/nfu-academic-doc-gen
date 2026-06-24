# How To: Corr Callable Method

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corr callable method

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
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign my_corr = value

```python
my_corr = lambda a, b: 1.0 if (a == b).all() else 0.0
```

**Verification:**
```python
assert np.isnan(datetime_series[::2].corr(datetime_series[1::2], method=my_corr))
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series([1, 2, 3, 4, 5])
```

### Step 3: Assign s2 = Series(...)

```python
s2 = Series([5, 4, 3, 2, 1])
```

### Step 4: Assign expected = 0

```python
expected = 0
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(s1.corr(s2, method=my_corr), expected)
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(datetime_series.corr(datetime_series, method=my_corr), 1.0)
```

### Step 7: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(datetime_series[:15].corr(datetime_series[5:], method=my_corr), 1.0)
```

**Verification:**
```python
assert np.isnan(datetime_series[::2].corr(datetime_series[1::2], method=my_corr))
```

### Step 8: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame([s1, s2])
```

### Step 9: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([{0: 1.0, 1: 0}, {0: 0, 1: 1.0}])
```

### Step 10: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(df.transpose().corr(method=my_corr), expected)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
my_corr = lambda a, b: 1.0 if (a == b).all() else 0.0
s1 = Series([1, 2, 3, 4, 5])
s2 = Series([5, 4, 3, 2, 1])
expected = 0
tm.assert_almost_equal(s1.corr(s2, method=my_corr), expected)
tm.assert_almost_equal(datetime_series.corr(datetime_series, method=my_corr), 1.0)
tm.assert_almost_equal(datetime_series[:15].corr(datetime_series[5:], method=my_corr), 1.0)
assert np.isnan(datetime_series[::2].corr(datetime_series[1::2], method=my_corr))
df = pd.DataFrame([s1, s2])
expected = pd.DataFrame([{0: 1.0, 1: 0}, {0: 0, 1: 1.0}])
tm.assert_almost_equal(df.transpose().corr(method=my_corr), expected)
```

## Next Steps


---

*Source: test_cov_corr.py:156 | Complexity: Advanced | Last updated: 2026-06-02*