# How To: Argsort Dt64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test argsort dt64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([Timestamp(f'201301{i:02d}') for i in range(1, 6)], dtype=f'M8[{unit}]')
```

**Verification:**
```python
assert ser.dtype == f'datetime64[{unit}]'
```

### Step 2: Assign shifted = ser.shift(...)

```python
shifted = ser.shift(-1)
```

**Verification:**
```python
assert shifted.dtype == f'datetime64[{unit}]'
```

### Step 3: Assign result = ser.argsort(...)

```python
result = ser.argsort()
```

**Verification:**
```python
assert isna(shifted[4])
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(range(5), dtype=np.intp)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = 'The behavior of Series.argsort in the presence of NA values'

```python
msg = 'The behavior of Series.argsort in the presence of NA values'
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(list(range(4)) + [-1], dtype=np.intp)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = shifted.argsort(...)

```python
result = shifted.argsort()
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
ser = Series([Timestamp(f'201301{i:02d}') for i in range(1, 6)], dtype=f'M8[{unit}]')
assert ser.dtype == f'datetime64[{unit}]'
shifted = ser.shift(-1)
assert shifted.dtype == f'datetime64[{unit}]'
assert isna(shifted[4])
result = ser.argsort()
expected = Series(range(5), dtype=np.intp)
tm.assert_series_equal(result, expected)
msg = 'The behavior of Series.argsort in the presence of NA values'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = shifted.argsort()
expected = Series(list(range(4)) + [-1], dtype=np.intp)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_argsort.py:45 | Complexity: Advanced | Last updated: 2026-06-02*