# How To: Pad Backfill Object Segfault

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pad backfill object segfault

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pandas._libs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign old = np.array(...)

```python
old = np.array([], dtype='O')
```

### Step 2: Assign new = np.array(...)

```python
new = np.array([datetime(2010, 12, 31)], dtype='O')
```

### Step 3: Assign result = unknown(...)

```python
result = libalgos.pad['object'](old, new)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([-1], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = unknown(...)

```python
result = libalgos.pad['object'](new, old)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([], dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = unknown(...)

```python
result = libalgos.backfill['object'](old, new)
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([-1], dtype=np.intp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 12: Assign result = unknown(...)

```python
result = libalgos.backfill['object'](new, old)
```

### Step 13: Assign expected = np.array(...)

```python
expected = np.array([], dtype=np.intp)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
old = np.array([], dtype='O')
new = np.array([datetime(2010, 12, 31)], dtype='O')
result = libalgos.pad['object'](old, new)
expected = np.array([-1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = libalgos.pad['object'](new, old)
expected = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = libalgos.backfill['object'](old, new)
expected = np.array([-1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
result = libalgos.backfill['object'](new, old)
expected = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_libalgos.py:92 | Complexity: Advanced | Last updated: 2026-06-02*