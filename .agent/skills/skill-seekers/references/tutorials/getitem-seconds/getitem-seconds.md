# How To: Getitem Seconds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem seconds

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign didx = date_range(...)

```python
didx = date_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
```

### Step 2: Assign pidx = period_range(...)

```python
pidx = period_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
```

### Step 3: Assign values = value

```python
values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9h', '2013/02/01 09:00']
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).random(len(idx)), index=idx)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser['2013/01/01 10:00'], ser[3600:3660])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser['2013/01/01 9h'], ser[:3600])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser[d], ser)
```

### Step 8: idx[val]

```python
idx[val]
```


## Complete Example

```python
# Workflow
didx = date_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
pidx = period_range(start='2013/01/01 09:00:00', freq='s', periods=4000)
for idx in [didx, pidx]:
    values = ['2014', '2013/02', '2013/01/02', '2013/02/01 9h', '2013/02/01 09:00']
    for val in values:
        with pytest.raises(IndexError, match='only integers, slices'):
            idx[val]
    ser = Series(np.random.default_rng(2).random(len(idx)), index=idx)
    tm.assert_series_equal(ser['2013/01/01 10:00'], ser[3600:3660])
    tm.assert_series_equal(ser['2013/01/01 9h'], ser[:3600])
    for d in ['2013/01/01', '2013/01', '2013']:
        tm.assert_series_equal(ser[d], ser)
```

## Next Steps


---

*Source: test_indexing.py:175 | Complexity: Advanced | Last updated: 2026-06-02*