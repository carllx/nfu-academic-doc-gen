# How To: Datetime Array Find Type

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime array find type

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

### Step 1: Assign dt = np.datetime64(...)

```python
dt = np.datetime64('1970-01-01', 'M')
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('M8[M]'))
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([dt])
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 3: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('M8[M]'))
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 4: Assign dt = datetime.date(...)

```python
dt = datetime.date(1970, 1, 1)
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 5: Assign arr = np.array(...)

```python
arr = np.array([dt])
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 6: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('O'))
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 7: Assign dt = datetime.datetime(...)

```python
dt = datetime.datetime(1970, 1, 1, 12, 30, 40)
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('M8[D]'))
```

### Step 8: Assign arr = np.array(...)

```python
arr = np.array([dt])
```

**Verification:**
```python
assert_equal(arr.dtype, np.dtype('M8[us]'))
```

### Step 9: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 10: Assign b = np.bool(...)

```python
b = np.bool(True)
```

### Step 11: Assign dm = np.datetime64(...)

```python
dm = np.datetime64('1970-01-01', 'M')
```

### Step 12: Assign d = datetime.date(...)

```python
d = datetime.date(1970, 1, 1)
```

### Step 13: Assign dt = datetime.datetime(...)

```python
dt = datetime.datetime(1970, 1, 1, 12, 30, 40)
```

### Step 14: Assign arr = np.array(...)

```python
arr = np.array([b, dm])
```

### Step 15: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 16: Assign arr = np.array(...)

```python
arr = np.array([b, d])
```

### Step 17: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 18: Assign arr = np.array(...)

```python
arr = np.array([b, dt])
```

### Step 19: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('O'))
```

### Step 20: Assign arr = np.array.astype(...)

```python
arr = np.array([d, d]).astype('datetime64')
```

### Step 21: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('M8[D]'))
```

### Step 22: Assign arr = np.array.astype(...)

```python
arr = np.array([dt, dt]).astype('datetime64')
```

### Step 23: Call assert_equal()

```python
assert_equal(arr.dtype, np.dtype('M8[us]'))
```


## Complete Example

```python
# Workflow
dt = np.datetime64('1970-01-01', 'M')
arr = np.array([dt])
assert_equal(arr.dtype, np.dtype('M8[M]'))
dt = datetime.date(1970, 1, 1)
arr = np.array([dt])
assert_equal(arr.dtype, np.dtype('O'))
dt = datetime.datetime(1970, 1, 1, 12, 30, 40)
arr = np.array([dt])
assert_equal(arr.dtype, np.dtype('O'))
b = np.bool(True)
dm = np.datetime64('1970-01-01', 'M')
d = datetime.date(1970, 1, 1)
dt = datetime.datetime(1970, 1, 1, 12, 30, 40)
arr = np.array([b, dm])
assert_equal(arr.dtype, np.dtype('O'))
arr = np.array([b, d])
assert_equal(arr.dtype, np.dtype('O'))
arr = np.array([b, dt])
assert_equal(arr.dtype, np.dtype('O'))
arr = np.array([d, d]).astype('datetime64')
assert_equal(arr.dtype, np.dtype('M8[D]'))
arr = np.array([dt, dt]).astype('datetime64')
assert_equal(arr.dtype, np.dtype('M8[us]'))
```

## Next Steps


---

*Source: test_datetime.py:343 | Complexity: Advanced | Last updated: 2026-06-02*