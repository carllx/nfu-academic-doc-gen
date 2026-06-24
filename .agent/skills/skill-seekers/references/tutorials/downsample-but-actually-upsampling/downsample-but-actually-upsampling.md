# How To: Downsample But Actually Upsampling

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test downsample but actually upsampling

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2012', periods=100, freq='s')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.arange(len(rng), dtype='int64'), index=rng)
```

### Step 3: Assign result = ts.resample.asfreq(...)

```python
result = ts.resample('20s').asfreq()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([0, 20, 40, 60, 80], index=date_range('2012-01-01 00:00:00', freq='20s', periods=5))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2012', periods=100, freq='s')
ts = Series(np.arange(len(rng), dtype='int64'), index=rng)
result = ts.resample('20s').asfreq()
expected = Series([0, 20, 40, 60, 80], index=date_range('2012-01-01 00:00:00', freq='20s', periods=5))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:209 | Complexity: Intermediate | Last updated: 2026-06-02*