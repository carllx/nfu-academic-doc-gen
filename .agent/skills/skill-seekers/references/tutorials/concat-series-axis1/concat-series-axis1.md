# How To: Concat Series Axis1

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series axis1

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
```

### Step 2: Assign pieces = value

```python
pieces = [ts[:-2], ts[2:], ts[2:-2]]
```

### Step 3: Assign result = concat(...)

```python
result = concat(pieces, axis=1)
```

### Step 4: Assign expected = value

```python
expected = DataFrame(pieces).T
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = concat(...)

```python
result = concat(pieces, keys=['A', 'B', 'C'], axis=1)
```

### Step 7: Assign expected = value

```python
expected = DataFrame(pieces, index=['A', 'B', 'C']).T
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
pieces = [ts[:-2], ts[2:], ts[2:-2]]
result = concat(pieces, axis=1)
expected = DataFrame(pieces).T
tm.assert_frame_equal(result, expected)
result = concat(pieces, keys=['A', 'B', 'C'], axis=1)
expected = DataFrame(pieces, index=['A', 'B', 'C']).T
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:52 | Complexity: Advanced | Last updated: 2026-06-02*