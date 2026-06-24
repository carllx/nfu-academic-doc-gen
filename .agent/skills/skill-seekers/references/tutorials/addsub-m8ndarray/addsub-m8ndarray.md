# How To: Addsub M8Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test addsub m8ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: shape
```

## Step-by-Step Guide

### Step 1: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp('2020-04-04 15:45').as_unit('ns')
```

### Step 2: Assign other = np.arange.astype.reshape(...)

```python
other = np.arange(6).astype('m8[h]').reshape(shape)
```

### Step 3: Assign result = value

```python
result = ts + other
```

### Step 4: Assign ex_stamps = value

```python
ex_stamps = [ts + Timedelta(hours=n) for n in range(6)]
```

### Step 5: Assign expected = np.array.reshape(...)

```python
expected = np.array([x.asm8 for x in ex_stamps], dtype='M8[ns]').reshape(shape)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = other + ts
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = ts - other
```

### Step 10: Assign ex_stamps = value

```python
ex_stamps = [ts - Timedelta(hours=n) for n in range(6)]
```

### Step 11: Assign expected = np.array.reshape(...)

```python
expected = np.array([x.asm8 for x in ex_stamps], dtype='M8[ns]').reshape(shape)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 13: Assign msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timestamp'"

```python
msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timestamp'"
```

### Step 14: other - ts

```python
other - ts
```


## Complete Example

```python
# Setup
# Fixtures: shape

# Workflow
ts = Timestamp('2020-04-04 15:45').as_unit('ns')
other = np.arange(6).astype('m8[h]').reshape(shape)
result = ts + other
ex_stamps = [ts + Timedelta(hours=n) for n in range(6)]
expected = np.array([x.asm8 for x in ex_stamps], dtype='M8[ns]').reshape(shape)
tm.assert_numpy_array_equal(result, expected)
result = other + ts
tm.assert_numpy_array_equal(result, expected)
result = ts - other
ex_stamps = [ts - Timedelta(hours=n) for n in range(6)]
expected = np.array([x.asm8 for x in ex_stamps], dtype='M8[ns]').reshape(shape)
tm.assert_numpy_array_equal(result, expected)
msg = "unsupported operand type\\(s\\) for -: 'numpy.ndarray' and 'Timestamp'"
with pytest.raises(TypeError, match=msg):
    other - ts
```

## Next Steps


---

*Source: test_arithmetic.py:237 | Complexity: Advanced | Last updated: 2026-06-02*