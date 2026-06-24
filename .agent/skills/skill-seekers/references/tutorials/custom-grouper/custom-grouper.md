# How To: Custom Grouper

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom grouper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: index, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = index.as_unit(...)

```python
dti = index.as_unit(unit)
```

**Verification:**
```python
assert g.ngroups == 2593
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.array([1] * len(dti)), index=dti, dtype='int64')
```

**Verification:**
```python
assert notna(g.mean()).all()
```

### Step 3: Assign b = Grouper(...)

```python
b = Grouper(freq=Minute(5))
```

### Step 4: Assign g = s.groupby(...)

```python
g = s.groupby(b)
```

### Step 5: Call g.ohlc()

```python
g.ohlc()
```

### Step 6: Assign funcs = value

```python
funcs = ['sum', 'mean', 'prod', 'min', 'max', 'var']
```

### Step 7: Assign b = Grouper(...)

```python
b = Grouper(freq=Minute(5), closed='right', label='right')
```

### Step 8: Assign g = s.groupby(...)

```python
g = s.groupby(b)
```

### Step 9: Call g.ohlc()

```python
g.ohlc()
```

### Step 10: Assign funcs = value

```python
funcs = ['sum', 'mean', 'prod', 'min', 'max', 'var']
```

**Verification:**
```python
assert g.ngroups == 2593
```

### Step 11: Assign arr = value

```python
arr = [1] + [5] * 2592
```

### Step 12: Assign idx = value

```python
idx = dti[0:-1:5]
```

### Step 13: Assign idx = idx.append(...)

```python
idx = idx.append(dti[-1:])
```

### Step 14: Assign idx = DatetimeIndex.as_unit(...)

```python
idx = DatetimeIndex(idx, freq='5min').as_unit(unit)
```

### Step 15: Assign expect = Series(...)

```python
expect = Series(arr, index=idx)
```

### Step 16: Assign result = g.agg(...)

```python
result = g.agg('sum')
```

### Step 17: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expect)
```

### Step 18: Call g._cython_agg_general()

```python
g._cython_agg_general(f, alt=None, numeric_only=True)
```

### Step 19: Call g._cython_agg_general()

```python
g._cython_agg_general(f, alt=None, numeric_only=True)
```


## Complete Example

```python
# Setup
# Fixtures: index, unit

# Workflow
dti = index.as_unit(unit)
s = Series(np.array([1] * len(dti)), index=dti, dtype='int64')
b = Grouper(freq=Minute(5))
g = s.groupby(b)
g.ohlc()
funcs = ['sum', 'mean', 'prod', 'min', 'max', 'var']
for f in funcs:
    g._cython_agg_general(f, alt=None, numeric_only=True)
b = Grouper(freq=Minute(5), closed='right', label='right')
g = s.groupby(b)
g.ohlc()
funcs = ['sum', 'mean', 'prod', 'min', 'max', 'var']
for f in funcs:
    g._cython_agg_general(f, alt=None, numeric_only=True)
assert g.ngroups == 2593
assert notna(g.mean()).all()
arr = [1] + [5] * 2592
idx = dti[0:-1:5]
idx = idx.append(dti[-1:])
idx = DatetimeIndex(idx, freq='5min').as_unit(unit)
expect = Series(arr, index=idx)
result = g.agg('sum')
tm.assert_series_equal(result, expect)
```

## Next Steps


---

*Source: test_datetime_index.py:72 | Complexity: Advanced | Last updated: 2026-06-02*