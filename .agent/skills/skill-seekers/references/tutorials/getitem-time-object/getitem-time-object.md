# How To: Getitem Time Object

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem time object

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 3: Assign mask = value

```python
mask = (rng.hour == 9) & (rng.minute == 30)
```

### Step 4: Assign result = value

```python
result = ts[time(9, 30)]
```

### Step 5: Assign expected = value

```python
expected = ts[mask]
```

### Step 6: Assign result.index = result.index._with_freq(...)

```python
result.index = result.index._with_freq(None)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
mask = (rng.hour == 9) & (rng.minute == 30)
result = ts[time(9, 30)]
expected = ts[mask]
result.index = result.index._with_freq(None)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*