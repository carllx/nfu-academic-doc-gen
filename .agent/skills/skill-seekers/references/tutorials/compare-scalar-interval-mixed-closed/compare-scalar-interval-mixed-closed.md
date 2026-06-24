# How To: Compare Scalar Interval Mixed Closed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare scalar interval mixed closed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: op, closed, other_closed
```

## Step-by-Step Guide

### Step 1: Assign interval_array = IntervalArray.from_arrays(...)

```python
interval_array = IntervalArray.from_arrays(range(2), range(1, 3), closed=closed)
```

### Step 2: Assign other = Interval(...)

```python
other = Interval(0, 1, closed=other_closed)
```

### Step 3: Assign result = op(...)

```python
result = op(interval_array, other)
```

### Step 4: Assign expected = self.elementwise_comparison(...)

```python
expected = self.elementwise_comparison(op, interval_array, other)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op, closed, other_closed

# Workflow
interval_array = IntervalArray.from_arrays(range(2), range(1, 3), closed=closed)
other = Interval(0, 1, closed=other_closed)
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*