# How To: Asfreq Fillvalue

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq fillvalue

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2016', periods=10, freq='2s')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.arange(len(rng)), index=rng, dtype='float')
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'one': ts})
```

### Step 4: Assign unknown = None

```python
df.loc['2016-01-01 00:00:08', 'one'] = None
```

### Step 5: Assign actual_df = df.asfreq(...)

```python
actual_df = df.asfreq(freq='1s', fill_value=9.0)
```

### Step 6: Assign expected_df = df.asfreq.fillna(...)

```python
expected_df = df.asfreq(freq='1s').fillna(9.0)
```

### Step 7: Assign unknown = None

```python
expected_df.loc['2016-01-01 00:00:08', 'one'] = None
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected_df, actual_df)
```

### Step 9: Assign expected_series = ts.asfreq.fillna(...)

```python
expected_series = ts.asfreq(freq='1s').fillna(9.0)
```

### Step 10: Assign actual_series = ts.asfreq(...)

```python
actual_series = ts.asfreq(freq='1s', fill_value=9.0)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected_series, actual_series)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2016', periods=10, freq='2s')
ts = Series(np.arange(len(rng)), index=rng, dtype='float')
df = DataFrame({'one': ts})
df.loc['2016-01-01 00:00:08', 'one'] = None
actual_df = df.asfreq(freq='1s', fill_value=9.0)
expected_df = df.asfreq(freq='1s').fillna(9.0)
expected_df.loc['2016-01-01 00:00:08', 'one'] = None
tm.assert_frame_equal(expected_df, actual_df)
expected_series = ts.asfreq(freq='1s').fillna(9.0)
actual_series = ts.asfreq(freq='1s', fill_value=9.0)
tm.assert_series_equal(expected_series, actual_series)
```

## Next Steps


---

*Source: test_asfreq.py:170 | Complexity: Advanced | Last updated: 2026-06-02*