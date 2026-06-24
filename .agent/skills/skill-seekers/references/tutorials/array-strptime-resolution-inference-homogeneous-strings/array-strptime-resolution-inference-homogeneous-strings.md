# How To: Array Strptime Resolution Inference Homogeneous Strings

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array strptime resolution inference homogeneous strings

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

### Step 2: Assign fmt = '%Y-%m-%d %H:%M:%S'

```python
fmt = '%Y-%m-%d %H:%M:%S'
```

### Step 3: Assign dtstr = dt.strftime(...)

```python
dtstr = dt.strftime(fmt)
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array([dtstr] * 3, dtype=object)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([dt.replace(tzinfo=None)] * 3, dtype='M8[s]')
```

### Step 6: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 8: Assign fmt = '%Y-%m-%d %H:%M:%S.%f'

```python
fmt = '%Y-%m-%d %H:%M:%S.%f'
```

### Step 9: Assign dtstr = dt.strftime(...)

```python
dtstr = dt.strftime(fmt)
```

### Step 10: Assign arr = np.array(...)

```python
arr = np.array([dtstr] * 3, dtype=object)
```

### Step 11: Assign expected = np.array(...)

```python
expected = np.array([dt.replace(tzinfo=None)] * 3, dtype='M8[us]')
```

### Step 12: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 14: Assign fmt = 'ISO8601'

```python
fmt = 'ISO8601'
```

### Step 15: Assign unknown = array_strptime(...)

```python
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dt = datetime(2016, 1, 2, 3, 4, 5, 678900, tzinfo=tz)
fmt = '%Y-%m-%d %H:%M:%S'
dtstr = dt.strftime(fmt)
arr = np.array([dtstr] * 3, dtype=object)
expected = np.array([dt.replace(tzinfo=None)] * 3, dtype='M8[s]')
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
fmt = '%Y-%m-%d %H:%M:%S.%f'
dtstr = dt.strftime(fmt)
arr = np.array([dtstr] * 3, dtype=object)
expected = np.array([dt.replace(tzinfo=None)] * 3, dtype='M8[us]')
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
fmt = 'ISO8601'
res, _ = array_strptime(arr, fmt=fmt, utc=False, creso=creso_infer)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_strptime.py:33 | Complexity: Advanced | Last updated: 2026-06-02*