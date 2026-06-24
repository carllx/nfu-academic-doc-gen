# How To: Union Sort False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union sort false

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('1day', periods=5)
```

**Verification:**
```python
assert left._can_fast_union(right)
```

### Step 2: Assign left = value

```python
left = tdi[3:]
```

### Step 3: Assign right = value

```python
right = tdi[:3]
```

**Verification:**
```python
assert left._can_fast_union(right)
```

### Step 4: Assign result = left.union(...)

```python
result = left.union(right)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, tdi)
```

### Step 6: Assign result = left.union(...)

```python
result = left.union(right, sort=False)
```

### Step 7: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex(['4 Days', '5 Days', '1 Days', '2 Day', '3 Days'])
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
tdi = timedelta_range('1day', periods=5)
left = tdi[3:]
right = tdi[:3]
assert left._can_fast_union(right)
result = left.union(right)
tm.assert_index_equal(result, tdi)
result = left.union(right, sort=False)
expected = TimedeltaIndex(['4 Days', '5 Days', '1 Days', '2 Day', '3 Days'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:28 | Complexity: Advanced | Last updated: 2026-06-02*