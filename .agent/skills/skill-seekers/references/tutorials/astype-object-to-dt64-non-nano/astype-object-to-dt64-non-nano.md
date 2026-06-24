# How To: Astype Object To Dt64 Non Nano

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype object to dt64 non nano

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2999-01-01')
```

### Step 2: Assign dtype = 'M8[us]'

```python
dtype = 'M8[us]'
```

### Step 3: Assign vals = value

```python
vals = [ts, '2999-01-02 03:04:05.678910', 2500]
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(vals, dtype=object)
```

### Step 5: Assign result = ser.astype(...)

```python
result = ser.astype(dtype)
```

### Step 6: Assign pointwise = value

```python
pointwise = [vals[0].tz_localize(tz), Timestamp(vals[1], tz=tz), to_datetime(vals[2], unit='us', utc=True).tz_convert(tz)]
```

### Step 7: Assign exp_vals = value

```python
exp_vals = [x.as_unit('us').asm8 for x in pointwise]
```

### Step 8: Assign exp_arr = np.array(...)

```python
exp_arr = np.array(exp_vals, dtype='M8[us]')
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(exp_arr, dtype='M8[us]')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign dtype = value

```python
dtype = f'M8[us, {tz}]'
```

### Step 12: Assign expected = expected.dt.tz_localize.dt.tz_convert(...)

```python
expected = expected.dt.tz_localize('UTC').dt.tz_convert(tz)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
ts = Timestamp('2999-01-01')
dtype = 'M8[us]'
if tz is not None:
    dtype = f'M8[us, {tz}]'
vals = [ts, '2999-01-02 03:04:05.678910', 2500]
ser = Series(vals, dtype=object)
result = ser.astype(dtype)
pointwise = [vals[0].tz_localize(tz), Timestamp(vals[1], tz=tz), to_datetime(vals[2], unit='us', utc=True).tz_convert(tz)]
exp_vals = [x.as_unit('us').asm8 for x in pointwise]
exp_arr = np.array(exp_vals, dtype='M8[us]')
expected = Series(exp_arr, dtype='M8[us]')
if tz is not None:
    expected = expected.dt.tz_localize('UTC').dt.tz_convert(tz)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:112 | Complexity: Advanced | Last updated: 2026-06-02*