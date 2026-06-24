# How To: Join Overlapping Interval Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join overlapping interval level

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx_1 = MultiIndex.from_tuples(...)

```python
idx_1 = MultiIndex.from_tuples([(1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (1, Interval(2.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0)), (2, Interval(3.0, 5.0))], names=['num', 'interval'])
```

### Step 2: Assign idx_2 = MultiIndex.from_tuples(...)

```python
idx_2 = MultiIndex.from_tuples([(1, Interval(2.0, 5.0)), (1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (2, Interval(3.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0))], names=['num', 'interval'])
```

### Step 3: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples([(1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (1, Interval(2.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0)), (2, Interval(3.0, 5.0))], names=['num', 'interval'])
```

### Step 4: Assign result = idx_1.join(...)

```python
result = idx_1.join(idx_2, how='outer')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx_1 = MultiIndex.from_tuples([(1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (1, Interval(2.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0)), (2, Interval(3.0, 5.0))], names=['num', 'interval'])
idx_2 = MultiIndex.from_tuples([(1, Interval(2.0, 5.0)), (1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (2, Interval(3.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0))], names=['num', 'interval'])
expected = MultiIndex.from_tuples([(1, Interval(0.0, 1.0)), (1, Interval(1.0, 2.0)), (1, Interval(2.0, 5.0)), (2, Interval(0.0, 1.0)), (2, Interval(1.0, 3.0)), (2, Interval(3.0, 5.0))], names=['num', 'interval'])
result = idx_1.join(idx_2, how='outer')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*