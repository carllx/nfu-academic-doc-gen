# How To: Array Strptime Resolution Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array strptime resolution mixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.strptime`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2016, 1, 2, 3, 4, 5, 678900, tzinfo=tz)
```

### Step 2: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp(dt).as_unit('ns')
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([dt, ts], dtype=object)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([Timestamp(dt).as_unit('ns').asm8, ts.asm8], dtype='M8[ns]')
```

### Step 5: Assign fmt = '%Y-%m-%d %H:%M:%S'

```python
fmt = '%Y-%m-%d %H:%M:%S'
```

### Step 6: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 8: Assign fmt = 'ISO8601'

```python
fmt = 'ISO8601'
```

### Step 9: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dt = datetime(2016, 1, 2, 3, 4, 5, 678900, tzinfo=tz)
ts = Timestamp(dt).as_unit('ns')
arr = np.array([dt, ts], dtype=object)
expected = np.array([Timestamp(dt).as_unit('ns').asm8, ts.asm8], dtype='M8[ns]')
fmt = '%Y-%m-%d %H:%M:%S'
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
fmt = 'ISO8601'
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_strptime.py:57 | Complexity: Advanced | Last updated: 2026-06-02*