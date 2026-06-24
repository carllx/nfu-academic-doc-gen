# How To: Union Bug 1730

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union bug 1730

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign rng_a = timedelta_range(...)

```python
rng_a = timedelta_range('1 day', periods=4, freq='3h')
```

### Step 2: Assign rng_b = timedelta_range(...)

```python
rng_b = timedelta_range('1 day', periods=4, freq='4h')
```

### Step 3: Assign result = rng_a.union(...)

```python
result = rng_a.union(rng_b)
```

### Step 4: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(sorted(set(rng_a) | set(rng_b)))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```


## Complete Example

```python
# Workflow
rng_a = timedelta_range('1 day', periods=4, freq='3h')
rng_b = timedelta_range('1 day', periods=4, freq='4h')
result = rng_a.union(rng_b)
exp = TimedeltaIndex(sorted(set(rng_a) | set(rng_b)))
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_setops.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*