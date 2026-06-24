# How To: Astype Freq Conversion

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype freq conversion

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('1 Day', periods=30)
```

**Verification:**
```python
assert expected.dtype == 'm8[s]'
```

### Step 2: Assign res = tdi.astype(...)

```python
res = tdi.astype('m8[s]')
```

### Step 3: Assign exp_values = np.asarray.astype(...)

```python
exp_values = np.asarray(tdi).astype('m8[s]')
```

### Step 4: Assign exp_tda = TimedeltaArray._simple_new(...)

```python
exp_tda = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype, freq=tdi.freq)
```

### Step 5: Assign expected = Index(...)

```python
expected = Index(exp_tda)
```

**Verification:**
```python
assert expected.dtype == 'm8[s]'
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```

### Step 7: Assign res = tdi._data.astype(...)

```python
res = tdi._data.astype('m8[s]')
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(res, expected._values)
```

### Step 9: Assign res = tdi.to_series.astype(...)

```python
res = tdi.to_series().astype('m8[s]')
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(res._values, expected._values._with_freq(None))
```


## Complete Example

```python
# Workflow
tdi = timedelta_range('1 Day', periods=30)
res = tdi.astype('m8[s]')
exp_values = np.asarray(tdi).astype('m8[s]')
exp_tda = TimedeltaArray._simple_new(exp_values, dtype=exp_values.dtype, freq=tdi.freq)
expected = Index(exp_tda)
assert expected.dtype == 'm8[s]'
tm.assert_index_equal(res, expected)
res = tdi._data.astype('m8[s]')
tm.assert_equal(res, expected._values)
res = tdi.to_series().astype('m8[s]')
tm.assert_equal(res._values, expected._values._with_freq(None))
```

## Next Steps


---

*Source: test_astype.py:132 | Complexity: Advanced | Last updated: 2026-06-02*