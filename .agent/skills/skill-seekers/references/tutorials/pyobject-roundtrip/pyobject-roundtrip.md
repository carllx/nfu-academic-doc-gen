# How To: Pyobject Roundtrip

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pyobject roundtrip

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, -1020040340, -2942398, -1, 0, 1, 234523453, 1199164176], dtype=np.int64)
```

**Verification:**
```python
assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
```

### Step 2: Assign b = a.copy.view(...)

```python
b = a.copy().view(dtype=unit)
```

**Verification:**
```python
assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
```

### Step 3: Assign unknown = '-0001-01-01'

```python
b[0] = '-0001-01-01'
```

### Step 4: Assign unknown = '-0001-12-31'

```python
b[1] = '-0001-12-31'
```

### Step 5: Assign unknown = '0000-01-01'

```python
b[2] = '0000-01-01'
```

### Step 6: Assign unknown = '0001-01-01'

```python
b[3] = '0001-01-01'
```

### Step 7: Assign unknown = '1969-12-31'

```python
b[4] = '1969-12-31'
```

### Step 8: Assign unknown = '1970-01-01'

```python
b[5] = '1970-01-01'
```

### Step 9: Assign unknown = '9999-12-31'

```python
b[6] = '9999-12-31'
```

### Step 10: Assign unknown = '10000-01-01'

```python
b[7] = '10000-01-01'
```

### Step 11: Assign unknown = 'NaT'

```python
b[8] = 'NaT'
```

### Step 12: Call assert_equal()

```python
assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
```

### Step 13: Assign b = a.copy.view(...)

```python
b = a.copy().view(dtype=unit)
```

### Step 14: Assign unknown = '-0001-01-01T00'

```python
b[0] = '-0001-01-01T00'
```

### Step 15: Assign unknown = '-0001-12-31T00'

```python
b[1] = '-0001-12-31T00'
```

### Step 16: Assign unknown = '0000-01-01T00'

```python
b[2] = '0000-01-01T00'
```

### Step 17: Assign unknown = '0001-01-01T00'

```python
b[3] = '0001-01-01T00'
```

### Step 18: Assign unknown = '1969-12-31T23:59:59.999999'

```python
b[4] = '1969-12-31T23:59:59.999999'
```

### Step 19: Assign unknown = '1970-01-01T00'

```python
b[5] = '1970-01-01T00'
```

### Step 20: Assign unknown = '9999-12-31T23:59:59.999999'

```python
b[6] = '9999-12-31T23:59:59.999999'
```

### Step 21: Assign unknown = '10000-01-01T00'

```python
b[7] = '10000-01-01T00'
```

### Step 22: Assign unknown = 'NaT'

```python
b[8] = 'NaT'
```

### Step 23: Call assert_equal()

```python
assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
```


## Complete Example

```python
# Workflow
a = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, -1020040340, -2942398, -1, 0, 1, 234523453, 1199164176], dtype=np.int64)
for unit in ['M8[D]', 'M8[W]', 'M8[M]', 'M8[Y]']:
    b = a.copy().view(dtype=unit)
    b[0] = '-0001-01-01'
    b[1] = '-0001-12-31'
    b[2] = '0000-01-01'
    b[3] = '0001-01-01'
    b[4] = '1969-12-31'
    b[5] = '1970-01-01'
    b[6] = '9999-12-31'
    b[7] = '10000-01-01'
    b[8] = 'NaT'
    assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
for unit in ['M8[as]', 'M8[16fs]', 'M8[ps]', 'M8[us]', 'M8[300as]', 'M8[20us]']:
    b = a.copy().view(dtype=unit)
    b[0] = '-0001-01-01T00'
    b[1] = '-0001-12-31T00'
    b[2] = '0000-01-01T00'
    b[3] = '0001-01-01T00'
    b[4] = '1969-12-31T23:59:59.999999'
    b[5] = '1970-01-01T00'
    b[6] = '9999-12-31T23:59:59.999999'
    b[7] = '10000-01-01T00'
    b[8] = 'NaT'
    assert_equal(b.astype(object).astype(unit), b, f'Error roundtripping unit {unit}')
```

## Next Steps


---

*Source: test_datetime.py:960 | Complexity: Advanced | Last updated: 2026-06-02*