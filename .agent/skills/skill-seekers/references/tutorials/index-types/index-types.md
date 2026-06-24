# How To: Index Types

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas.tests.io.pytables.common`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: setup_path
```

## Step-by-Step Guide

### Step 1: Assign values = np.random.default_rng.standard_normal(...)

```python
values = np.random.default_rng(2).standard_normal(2)
```

### Step 2: Assign func = value

```python
func = lambda lhs, rhs: tm.assert_series_equal(lhs, rhs, check_index_type=True)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(values, [0, 'y'])
```

### Step 4: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(values, [datetime.datetime.today(), 0])
```

### Step 6: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 7: Assign ser = Series(...)

```python
ser = Series(values, ['y', 0])
```

### Step 8: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 9: Assign ser = Series(...)

```python
ser = Series(values, [datetime.date.today(), 'a'])
```

### Step 10: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 11: Assign ser = Series(...)

```python
ser = Series(values, [0, 'y'])
```

### Step 12: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 13: Assign ser = Series(...)

```python
ser = Series(values, [datetime.datetime.today(), 0])
```

### Step 14: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 15: Assign ser = Series(...)

```python
ser = Series(values, ['y', 0])
```

### Step 16: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 17: Assign ser = Series(...)

```python
ser = Series(values, [datetime.date.today(), 'a'])
```

### Step 18: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 19: Assign ser = Series(...)

```python
ser = Series(values, [1.23, 'b'])
```

### Step 20: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 21: Assign ser = Series(...)

```python
ser = Series(values, [1, 1.53])
```

### Step 22: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 23: Assign ser = Series(...)

```python
ser = Series(values, [1, 5])
```

### Step 24: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 25: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex(['2012-01-01', '2012-01-02'], dtype='M8[ns]')
```

### Step 26: Assign ser = Series(...)

```python
ser = Series(values, index=dti)
```

### Step 27: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```

### Step 28: Assign ser.index = ser.index.as_unit(...)

```python
ser.index = ser.index.as_unit('s')
```

### Step 29: Call _check_roundtrip()

```python
_check_roundtrip(ser, func, path=setup_path)
```


## Complete Example

```python
# Setup
# Fixtures: setup_path

# Workflow
values = np.random.default_rng(2).standard_normal(2)
func = lambda lhs, rhs: tm.assert_series_equal(lhs, rhs, check_index_type=True)
ser = Series(values, [0, 'y'])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [datetime.datetime.today(), 0])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, ['y', 0])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [datetime.date.today(), 'a'])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [0, 'y'])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [datetime.datetime.today(), 0])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, ['y', 0])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [datetime.date.today(), 'a'])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [1.23, 'b'])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [1, 1.53])
_check_roundtrip(ser, func, path=setup_path)
ser = Series(values, [1, 5])
_check_roundtrip(ser, func, path=setup_path)
dti = DatetimeIndex(['2012-01-01', '2012-01-02'], dtype='M8[ns]')
ser = Series(values, index=dti)
_check_roundtrip(ser, func, path=setup_path)
ser.index = ser.index.as_unit('s')
_check_roundtrip(ser, func, path=setup_path)
```

## Next Steps


---

*Source: test_round_trip.py:300 | Complexity: Advanced | Last updated: 2026-06-02*