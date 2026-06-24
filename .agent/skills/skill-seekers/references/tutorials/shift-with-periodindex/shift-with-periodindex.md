# How To: Shift With Periodindex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift with periodindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign ps = DataFrame(...)

```python
ps = DataFrame(np.arange(4, dtype=float), index=pd.period_range('2020-01-01', periods=4))
```

### Step 2: Assign ps = tm.get_obj(...)

```python
ps = tm.get_obj(ps, frame_or_series)
```

### Step 3: Assign shifted = ps.shift(...)

```python
shifted = ps.shift(1)
```

### Step 4: Assign unshifted = shifted.shift(...)

```python
unshifted = shifted.shift(-1)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(shifted.index, ps.index)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(unshifted.index, ps.index)
```

### Step 7: Assign shifted2 = ps.shift(...)

```python
shifted2 = ps.shift(1, 'D')
```

### Step 8: Assign shifted3 = ps.shift(...)

```python
shifted3 = ps.shift(1, offsets.Day())
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(shifted2, shifted3)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(ps, shifted2.shift(-1, 'D'))
```

### Step 11: Assign msg = 'does not match PeriodIndex freq'

```python
msg = 'does not match PeriodIndex freq'
```

### Step 12: Assign shifted4 = ps.shift(...)

```python
shifted4 = ps.shift(1, freq='D')
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(shifted2, shifted4)
```

### Step 14: Assign shifted5 = ps.shift(...)

```python
shifted5 = ps.shift(1, freq=offsets.Day())
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(shifted5, shifted4)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(unshifted.iloc[:, 0].dropna().values, ps.iloc[:-1, 0].values)
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(unshifted.dropna().values, ps.values[:-1])
```

### Step 18: Call ps.shift()

```python
ps.shift(freq='W')
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
ps = DataFrame(np.arange(4, dtype=float), index=pd.period_range('2020-01-01', periods=4))
ps = tm.get_obj(ps, frame_or_series)
shifted = ps.shift(1)
unshifted = shifted.shift(-1)
tm.assert_index_equal(shifted.index, ps.index)
tm.assert_index_equal(unshifted.index, ps.index)
if frame_or_series is DataFrame:
    tm.assert_numpy_array_equal(unshifted.iloc[:, 0].dropna().values, ps.iloc[:-1, 0].values)
else:
    tm.assert_numpy_array_equal(unshifted.dropna().values, ps.values[:-1])
shifted2 = ps.shift(1, 'D')
shifted3 = ps.shift(1, offsets.Day())
tm.assert_equal(shifted2, shifted3)
tm.assert_equal(ps, shifted2.shift(-1, 'D'))
msg = 'does not match PeriodIndex freq'
with pytest.raises(ValueError, match=msg):
    ps.shift(freq='W')
shifted4 = ps.shift(1, freq='D')
tm.assert_equal(shifted2, shifted4)
shifted5 = ps.shift(1, freq=offsets.Day())
tm.assert_equal(shifted5, shifted4)
```

## Next Steps


---

*Source: test_shift.py:242 | Complexity: Advanced | Last updated: 2026-06-02*