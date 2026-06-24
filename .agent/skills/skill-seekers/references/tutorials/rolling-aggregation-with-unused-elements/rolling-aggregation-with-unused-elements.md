# How To: Rolling Aggregation With Unused Elements

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling aggregation with unused elements

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.window.aggregations`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: rolling_aggregation
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
minp, width = (0, 5)
```

**Verification:**
```python
assert np.isfinite(expected.values).all(), 'Not all expected values are finite'
```

### Step 2: Assign size = value

```python
size = 2 * width + 5
```

### Step 3: Assign values = np.arange(...)

```python
values = np.arange(1, size + 1, dtype=np.float64)
```

### Step 4: Assign unknown = value

```python
values[width:width + 2] = sys.float_info.min
```

### Step 5: Assign unknown = value

```python
values[width + 2] = np.nan
```

### Step 6: Assign unknown = value

```python
values[width + 3:width + 5] = sys.float_info.max
```

### Step 7: Assign start = np.array(...)

```python
start = np.array([0, size - width], dtype=np.int64)
```

### Step 8: Assign end = np.array(...)

```python
end = np.array([width, size], dtype=np.int64)
```

### Step 9: Assign loc = np.array(...)

```python
loc = np.array([j for i in range(len(start)) for j in range(start[i], end[i])], dtype=np.int32)
```

### Step 10: Assign result = Series(...)

```python
result = Series(rolling_aggregation(values, start, end, minp))
```

### Step 11: Assign compact_values = np.array(...)

```python
compact_values = np.array(values[loc], dtype=np.float64)
```

### Step 12: Assign compact_start = np.arange(...)

```python
compact_start = np.arange(0, len(start) * width, width, dtype=np.int64)
```

### Step 13: Assign compact_end = value

```python
compact_end = compact_start + width
```

### Step 14: Assign expected = Series(...)

```python
expected = Series(rolling_aggregation(compact_values, compact_start, compact_end, minp))
```

**Verification:**
```python
assert np.isfinite(expected.values).all(), 'Not all expected values are finite'
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: rolling_aggregation

# Workflow
minp, width = (0, 5)
size = 2 * width + 5
values = np.arange(1, size + 1, dtype=np.float64)
values[width:width + 2] = sys.float_info.min
values[width + 2] = np.nan
values[width + 3:width + 5] = sys.float_info.max
start = np.array([0, size - width], dtype=np.int64)
end = np.array([width, size], dtype=np.int64)
loc = np.array([j for i in range(len(start)) for j in range(start[i], end[i])], dtype=np.int32)
result = Series(rolling_aggregation(values, start, end, minp))
compact_values = np.array(values[loc], dtype=np.float64)
compact_start = np.arange(0, len(start) * width, width, dtype=np.int64)
compact_end = compact_start + width
expected = Series(rolling_aggregation(compact_values, compact_start, compact_end, minp))
assert np.isfinite(expected.values).all(), 'Not all expected values are finite'
tm.assert_equal(expected, result)
```

## Next Steps


---

*Source: test_cython_aggregations.py:89 | Complexity: Advanced | Last updated: 2026-06-02*