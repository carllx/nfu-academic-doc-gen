# How To: Add Datetimelike Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add datetimelike scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: tda, tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign ts = pd.Timestamp.as_unit(...)

```python
ts = pd.Timestamp('2016-01-01', tz=tz_naive_fixture).as_unit('ns')
```

### Step 2: Assign expected = value

```python
expected = tda.as_unit('ns') + ts
```

### Step 3: Assign res = value

```python
res = tda + ts
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```

### Step 5: Assign res = value

```python
res = ts + tda
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, expected)
```

### Step 7: Assign exp_values = value

```python
exp_values = tda._ndarray + ts.asm8
```

### Step 8: Assign expected = DatetimeArray._simple_new.tz_localize.tz_convert(...)

```python
expected = DatetimeArray._simple_new(exp_values, dtype=exp_values.dtype).tz_localize('UTC').tz_convert(ts.tz)
```

### Step 9: Assign result = value

```python
result = tda + ts
```

### Step 10: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = ts + tda
```

### Step 12: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tda, tz_naive_fixture

# Workflow
ts = pd.Timestamp('2016-01-01', tz=tz_naive_fixture).as_unit('ns')
expected = tda.as_unit('ns') + ts
res = tda + ts
tm.assert_extension_array_equal(res, expected)
res = ts + tda
tm.assert_extension_array_equal(res, expected)
ts += Timedelta(1)
exp_values = tda._ndarray + ts.asm8
expected = DatetimeArray._simple_new(exp_values, dtype=exp_values.dtype).tz_localize('UTC').tz_convert(ts.tz)
result = tda + ts
tm.assert_extension_array_equal(result, expected)
result = ts + tda
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:108 | Complexity: Advanced | Last updated: 2026-06-02*