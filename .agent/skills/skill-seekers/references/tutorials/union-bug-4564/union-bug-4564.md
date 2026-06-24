# How To: Union Bug 4564

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union bug 4564

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign left = timedelta_range(...)

```python
left = timedelta_range('1 day', '30d')
```

### Step 2: Assign right = value

```python
right = left + pd.offsets.Minute(15)
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
left = timedelta_range('1 day', '30d')
right = left + pd.offsets.Minute(15)
result = left.union(right)
exp = TimedeltaIndex(sorted(set(left) | set(right)))
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_setops.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*