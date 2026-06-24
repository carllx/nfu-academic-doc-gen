# How To: From Td64 Retain Resolution

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from td64 retain resolution

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.dtypes`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign obj = np.timedelta64(...)

```python
obj = np.timedelta64(12345, 'ms')
```

**Verification:**
```python
assert td._value == obj.view('i8')
```

### Step 2: Assign td = Timedelta(...)

```python
td = Timedelta(obj)
```

**Verification:**
```python
assert td._creso == NpyDatetimeUnit.NPY_FR_ms.value
```

### Step 3: Assign obj2 = np.timedelta64(...)

```python
obj2 = np.timedelta64(1234, 'D')
```

**Verification:**
```python
assert td2._creso == NpyDatetimeUnit.NPY_FR_s.value
```

### Step 4: Assign td2 = Timedelta(...)

```python
td2 = Timedelta(obj2)
```

**Verification:**
```python
assert td2 == obj2
```

### Step 5: Assign obj3 = np.timedelta64(...)

```python
obj3 = np.timedelta64(1000000000000000000, 'us')
```

**Verification:**
```python
assert td2.days == 1234
```

### Step 6: Assign td3 = Timedelta(...)

```python
td3 = Timedelta(obj3)
```

**Verification:**
```python
assert td3.total_seconds() == 1000000000000
```


## Complete Example

```python
# Workflow
obj = np.timedelta64(12345, 'ms')
td = Timedelta(obj)
assert td._value == obj.view('i8')
assert td._creso == NpyDatetimeUnit.NPY_FR_ms.value
obj2 = np.timedelta64(1234, 'D')
td2 = Timedelta(obj2)
assert td2._creso == NpyDatetimeUnit.NPY_FR_s.value
assert td2 == obj2
assert td2.days == 1234
obj3 = np.timedelta64(1000000000000000000, 'us')
td3 = Timedelta(obj3)
assert td3.total_seconds() == 1000000000000
assert td3._creso == NpyDatetimeUnit.NPY_FR_us.value
```

## Next Steps


---

*Source: test_constructors.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*