# How To: Rolling Aggregation Boundary Consistency

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rolling aggregation boundary consistency

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
minp, step, width, size, selection = (0, 1, 3, 11, [2, 7])
```

### Step 2: Assign values = np.arange(...)

```python
values = np.arange(1, 1 + size, dtype=np.float64)
```

### Step 3: Assign end = np.arange(...)

```python
end = np.arange(width, size, step, dtype=np.int64)
```

### Step 4: Assign start = value

```python
start = end - width
```

### Step 5: Assign selarr = np.array(...)

```python
selarr = np.array(selection, dtype=np.int32)
```

### Step 6: Assign result = Series(...)

```python
result = Series(rolling_aggregation(values, start[selarr], end[selarr], minp))
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(rolling_aggregation(values, start, end, minp)[selarr])
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: rolling_aggregation

# Workflow
minp, step, width, size, selection = (0, 1, 3, 11, [2, 7])
values = np.arange(1, 1 + size, dtype=np.float64)
end = np.arange(width, size, step, dtype=np.int64)
start = end - width
selarr = np.array(selection, dtype=np.int32)
result = Series(rolling_aggregation(values, start[selarr], end[selarr], minp))
expected = Series(rolling_aggregation(values, start, end, minp)[selarr])
tm.assert_equal(expected, result)
```

## Next Steps


---

*Source: test_cython_aggregations.py:77 | Complexity: Advanced | Last updated: 2026-06-02*