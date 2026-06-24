# How To: Resample Empty Dataframe

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample empty dataframe

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.groupby`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.indexes.timedeltas`
- `pandas.core.resample`

**Setup Required:**
```python
# Fixtures: empty_frame_dti, freq, resample_method
```

## Step-by-Step Guide

### Step 1: Assign df = empty_frame_dti

```python
df = empty_frame_dti
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 2: Assign rs = df.resample(...)

```python
rs = df.resample(freq, group_keys=False)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(rs, resample_method)()
```

### Step 4: Assign expected.index = _asfreq_compat(...)

```python
expected.index = _asfreq_compat(df.index, freq)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected.index)
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 7: Assign msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"

```python
msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
```

### Step 8: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([df.columns, ['open', 'high', 'low', 'close']])
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame([], index=df.index[:0].copy(), columns=mi, dtype=np.float64)
```

### Step 10: Assign expected.index = _asfreq_compat(...)

```python
expected.index = _asfreq_compat(df.index, freq)
```

### Step 11: Call df.resample()

```python
df.resample(freq, group_keys=False)
```

### Step 12: Assign freq = 'M'

```python
freq = 'M'
```

### Step 13: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 14: Assign expected = Series(...)

```python
expected = Series([], dtype=np.int64)
```


## Complete Example

```python
# Setup
# Fixtures: empty_frame_dti, freq, resample_method

# Workflow
df = empty_frame_dti
if freq == 'ME' and isinstance(df.index, TimedeltaIndex):
    msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
    with pytest.raises(ValueError, match=msg):
        df.resample(freq, group_keys=False)
    return
elif freq == 'ME' and isinstance(df.index, PeriodIndex):
    freq = 'M'
rs = df.resample(freq, group_keys=False)
result = getattr(rs, resample_method)()
if resample_method == 'ohlc':
    mi = MultiIndex.from_product([df.columns, ['open', 'high', 'low', 'close']])
    expected = DataFrame([], index=df.index[:0].copy(), columns=mi, dtype=np.float64)
    expected.index = _asfreq_compat(df.index, freq)
elif resample_method != 'size':
    expected = df.copy()
else:
    expected = Series([], dtype=np.int64)
expected.index = _asfreq_compat(df.index, freq)
tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:226 | Complexity: Advanced | Last updated: 2026-06-02*