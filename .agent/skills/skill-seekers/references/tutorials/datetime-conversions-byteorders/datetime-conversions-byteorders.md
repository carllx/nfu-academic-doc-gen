# How To: Datetime Conversions Byteorders

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetime conversions byteorders

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
# Fixtures: str_dtype, time_dtype
```

## Step-by-Step Guide

### Step 1: Assign times = np.array(...)

```python
times = np.array(['2017', 'NaT'], dtype=time_dtype)
```

**Verification:**
```python
assert_array_equal(res, to_strings)
```

### Step 2: Assign from_strings = np.array(...)

```python
from_strings = np.array(['2017', 'NaT'], dtype=str_dtype)
```

**Verification:**
```python
assert_array_equal(res, to_strings)
```

### Step 3: Assign to_strings = times.astype(...)

```python
to_strings = times.astype(str_dtype)
```

**Verification:**
```python
assert_array_equal(res, to_strings)
```

### Step 4: Assign times_swapped = times.astype(...)

```python
times_swapped = times.astype(times.dtype.newbyteorder())
```

**Verification:**
```python
assert_array_equal(res, times)
```

### Step 5: Assign res = times_swapped.astype(...)

```python
res = times_swapped.astype(str_dtype)
```

**Verification:**
```python
assert_array_equal(res, times)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, to_strings)
```

**Verification:**
```python
assert_array_equal(res, times)
```

### Step 7: Assign res = times_swapped.astype(...)

```python
res = times_swapped.astype(to_strings.dtype.newbyteorder())
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(res, to_strings)
```

### Step 9: Assign res = times.astype(...)

```python
res = times.astype(to_strings.dtype.newbyteorder())
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(res, to_strings)
```

### Step 11: Assign from_strings_swapped = from_strings.astype(...)

```python
from_strings_swapped = from_strings.astype(from_strings.dtype.newbyteorder())
```

### Step 12: Assign res = from_strings_swapped.astype(...)

```python
res = from_strings_swapped.astype(time_dtype)
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(res, times)
```

### Step 14: Assign res = from_strings_swapped.astype(...)

```python
res = from_strings_swapped.astype(times.dtype.newbyteorder())
```

### Step 15: Call assert_array_equal()

```python
assert_array_equal(res, times)
```

### Step 16: Assign res = from_strings.astype(...)

```python
res = from_strings.astype(times.dtype.newbyteorder())
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(res, times)
```


## Complete Example

```python
# Setup
# Fixtures: str_dtype, time_dtype

# Workflow
times = np.array(['2017', 'NaT'], dtype=time_dtype)
from_strings = np.array(['2017', 'NaT'], dtype=str_dtype)
to_strings = times.astype(str_dtype)
times_swapped = times.astype(times.dtype.newbyteorder())
res = times_swapped.astype(str_dtype)
assert_array_equal(res, to_strings)
res = times_swapped.astype(to_strings.dtype.newbyteorder())
assert_array_equal(res, to_strings)
res = times.astype(to_strings.dtype.newbyteorder())
assert_array_equal(res, to_strings)
from_strings_swapped = from_strings.astype(from_strings.dtype.newbyteorder())
res = from_strings_swapped.astype(time_dtype)
assert_array_equal(res, times)
res = from_strings_swapped.astype(times.dtype.newbyteorder())
assert_array_equal(res, times)
res = from_strings.astype(times.dtype.newbyteorder())
assert_array_equal(res, times)
```

## Next Steps


---

*Source: test_datetime.py:787 | Complexity: Advanced | Last updated: 2026-06-02*