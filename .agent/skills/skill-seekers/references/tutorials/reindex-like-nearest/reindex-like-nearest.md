# How To: Reindex Like Nearest

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex like nearest

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(np.arange(10, dtype='int64'))
```

### Step 2: Assign target = value

```python
target = [0.1, 0.9, 1.5, 2.0]
```

### Step 3: Assign other = ser.reindex(...)

```python
other = ser.reindex(target, method='nearest')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(np.around(target).astype('int64'), target)
```

### Step 5: Assign result = ser.reindex_like(...)

```python
result = ser.reindex_like(other, method='nearest')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 7: Assign result = ser.reindex_like(...)

```python
result = ser.reindex_like(other, method='nearest', tolerance=1)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 9: Assign result = ser.reindex_like(...)

```python
result = ser.reindex_like(other, method='nearest', tolerance=[1, 2, 3, 4])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Workflow
ser = Series(np.arange(10, dtype='int64'))
target = [0.1, 0.9, 1.5, 2.0]
other = ser.reindex(target, method='nearest')
expected = Series(np.around(target).astype('int64'), target)
result = ser.reindex_like(other, method='nearest')
tm.assert_series_equal(expected, result)
result = ser.reindex_like(other, method='nearest', tolerance=1)
tm.assert_series_equal(expected, result)
result = ser.reindex_like(other, method='nearest', tolerance=[1, 2, 3, 4])
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_reindex_like.py:28 | Complexity: Advanced | Last updated: 2026-06-02*