# How To: Nat Comparisons

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nat comparisons

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.conversion`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: dtype, index_or_series, reverse, pair, op, expected
```

## Step-by-Step Guide

### Step 1: Assign box = index_or_series

```python
box = index_or_series
```

### Step 2: Assign unknown = pair

```python
lhs, rhs = pair
```

### Step 3: Assign left = Series(...)

```python
left = Series(lhs, dtype=dtype)
```

### Step 4: Assign right = box(...)

```python
right = box(rhs, dtype=dtype)
```

### Step 5: Assign result = op(...)

```python
result = op(left, right)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign unknown = value

```python
lhs, rhs = (rhs, lhs)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, index_or_series, reverse, pair, op, expected

# Workflow
box = index_or_series
lhs, rhs = pair
if reverse:
    lhs, rhs = (rhs, lhs)
left = Series(lhs, dtype=dtype)
right = box(rhs, dtype=dtype)
result = op(left, right)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime64.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*