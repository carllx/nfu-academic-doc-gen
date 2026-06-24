# How To: Astype Datetime

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype datetime

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
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(iNaT, dtype=f'M8[{unit}]', index=range(5))
```

**Verification:**
```python
assert ser.dtype == np.object_
```

### Step 2: Assign ser = ser.astype(...)

```python
ser = ser.astype('O')
```

**Verification:**
```python
assert ser.dtype == np.object_
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([datetime(2001, 1, 2, 0, 0)])
```

**Verification:**
```python
assert ser.dtype == f'M8[{unit}]'
```

### Step 4: Assign ser = ser.astype(...)

```python
ser = ser.astype('O')
```

**Verification:**
```python
assert ser.dtype == np.object_
```

### Step 5: Assign ser = Series(...)

```python
ser = Series([datetime(2001, 1, 2, 0, 0) for i in range(3)], dtype=f'M8[{unit}]')
```

### Step 6: Assign unknown = value

```python
ser[1] = np.nan
```

**Verification:**
```python
assert ser.dtype == f'M8[{unit}]'
```

### Step 7: Assign ser = ser.astype(...)

```python
ser = ser.astype('O')
```

**Verification:**
```python
assert ser.dtype == np.object_
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
ser = Series(iNaT, dtype=f'M8[{unit}]', index=range(5))
ser = ser.astype('O')
assert ser.dtype == np.object_
ser = Series([datetime(2001, 1, 2, 0, 0)])
ser = ser.astype('O')
assert ser.dtype == np.object_
ser = Series([datetime(2001, 1, 2, 0, 0) for i in range(3)], dtype=f'M8[{unit}]')
ser[1] = np.nan
assert ser.dtype == f'M8[{unit}]'
ser = ser.astype('O')
assert ser.dtype == np.object_
```

## Next Steps


---

*Source: test_astype.py:236 | Complexity: Intermediate | Last updated: 2026-06-02*