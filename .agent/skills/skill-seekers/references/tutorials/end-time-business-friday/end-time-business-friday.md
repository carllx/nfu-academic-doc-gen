# How To: End Time Business Friday

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test end time business friday

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pi = period_range(...)

```python
pi = period_range('1990-01-05', freq='B', periods=1)
```

### Step 2: Assign result = value

```python
result = pi.end_time
```

### Step 3: Assign dti = date_range._with_freq(...)

```python
dti = date_range('1990-01-05', freq='D', periods=1)._with_freq(None)
```

### Step 4: Assign expected = value

```python
expected = dti + Timedelta(days=1, nanoseconds=-1)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
pi = period_range('1990-01-05', freq='B', periods=1)
result = pi.end_time
dti = date_range('1990-01-05', freq='D', periods=1)._with_freq(None)
expected = dti + Timedelta(days=1, nanoseconds=-1)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_scalar_compat.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*