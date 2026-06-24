# How To: With Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/2/2000', freq='4h')
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(len(rng)), index=rng)
```

### Step 3: Assign r = s.resample.mean(...)

```python
r = s.resample('2h').mean()
```

### Step 4: Assign result = r.asof(...)

```python
result = r.asof(r.index)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign unknown = value

```python
r.iloc[3:5] = np.nan
```

### Step 8: Assign result = r.asof(...)

```python
result = r.asof(r.index)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 5, 5, 6.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign unknown = value

```python
r.iloc[-3:] = np.nan
```

### Step 12: Assign result = r.asof(...)

```python
result = r.asof(r.index)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000', '1/2/2000', freq='4h')
s = Series(np.arange(len(rng)), index=rng)
r = s.resample('2h').mean()
result = r.asof(r.index)
expected = Series([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
tm.assert_series_equal(result, expected)
r.iloc[3:5] = np.nan
result = r.asof(r.index)
expected = Series([0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 5, 5, 6.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
tm.assert_series_equal(result, expected)
r.iloc[-3:] = np.nan
result = r.asof(r.index)
expected = Series([0, 0, 1, 1, 1, 1, 3, 3, 4, 4, 4, 4, 4.0], index=date_range('1/1/2000', '1/2/2000', freq='2h'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_asof.py:89 | Complexity: Advanced | Last updated: 2026-06-02*