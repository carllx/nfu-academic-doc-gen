# How To: Time Byteswapped Cast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test time byteswapped cast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pickle`
- `warnings`
- `zoneinfo`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: time1, time2
```

## Step-by-Step Guide

### Step 1: Assign dtype1 = np.dtype(...)

```python
dtype1 = np.dtype(time1)
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 2: Assign dtype2 = np.dtype(...)

```python
dtype2 = np.dtype(time2)
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 3: Assign times = np.array(...)

```python
times = np.array(['2017', 'NaT'], dtype=dtype1)
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 4: Assign expected = times.astype(...)

```python
expected = times.astype(dtype2)
```

### Step 5: Assign res = times.astype.astype(...)

```python
res = times.astype(dtype1.newbyteorder()).astype(dtype2)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 7: Assign res = times.astype(...)

```python
res = times.astype(dtype2.newbyteorder())
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 9: Assign res = times.astype.astype(...)

```python
res = times.astype(dtype1.newbyteorder()).astype(dtype2.newbyteorder())
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: time1, time2

# Workflow
dtype1 = np.dtype(time1)
dtype2 = np.dtype(time2)
times = np.array(['2017', 'NaT'], dtype=dtype1)
expected = times.astype(dtype2)
res = times.astype(dtype1.newbyteorder()).astype(dtype2)
assert_array_equal(res, expected)
res = times.astype(dtype2.newbyteorder())
assert_array_equal(res, expected)
res = times.astype(dtype1.newbyteorder()).astype(dtype2.newbyteorder())
assert_array_equal(res, expected)
```

## Next Steps


---

*Source: test_datetime.py:770 | Complexity: Advanced | Last updated: 2026-06-02*