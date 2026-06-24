# How To: Fillna

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=date_range('2020-01-01', periods=5))
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts, ts.fillna(method='ffill'))
```

### Step 3: Assign unknown = value

```python
ts.iloc[2] = np.nan
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([0.0, 1.0, 1.0, 3.0, 4.0], index=ts.index)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts.fillna(method='ffill'), exp)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series([0.0, 1.0, 3.0, 3.0, 4.0], index=ts.index)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts.fillna(method='backfill'), exp)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series([0.0, 1.0, 5.0, 3.0, 4.0], index=ts.index)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts.fillna(value=5), exp)
```

### Step 10: Assign msg = "Must specify a fill 'value' or 'method'"

```python
msg = "Must specify a fill 'value' or 'method'"
```

### Step 11: Call ts.fillna()

```python
ts.fillna()
```


## Complete Example

```python
# Workflow
ts = Series([0.0, 1.0, 2.0, 3.0, 4.0], index=date_range('2020-01-01', periods=5))
tm.assert_series_equal(ts, ts.fillna(method='ffill'))
ts.iloc[2] = np.nan
exp = Series([0.0, 1.0, 1.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(method='ffill'), exp)
exp = Series([0.0, 1.0, 3.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(method='backfill'), exp)
exp = Series([0.0, 1.0, 5.0, 3.0, 4.0], index=ts.index)
tm.assert_series_equal(ts.fillna(value=5), exp)
msg = "Must specify a fill 'value' or 'method'"
with pytest.raises(ValueError, match=msg):
    ts.fillna()
```

## Next Steps


---

*Source: test_fillna.py:74 | Complexity: Advanced | Last updated: 2026-06-02*