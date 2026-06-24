# How To: Union Bug 1745

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union bug 1745

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign left = TimedeltaIndex(...)

```python
left = TimedeltaIndex(['1 day 15:19:49.695000'])
```

### Step 2: Assign right = TimedeltaIndex(...)

```python
right = TimedeltaIndex(['2 day 13:04:21.322000', '1 day 15:27:24.873000', '1 day 15:31:05.350000'])
```

### Step 3: Assign result = left.union(...)

```python
result = left.union(right)
```

### Step 4: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(sorted(set(left) | set(right)))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```


## Complete Example

```python
# Workflow
left = TimedeltaIndex(['1 day 15:19:49.695000'])
right = TimedeltaIndex(['2 day 13:04:21.322000', '1 day 15:27:24.873000', '1 day 15:31:05.350000'])
result = left.union(right)
exp = TimedeltaIndex(sorted(set(left) | set(right)))
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_setops.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*