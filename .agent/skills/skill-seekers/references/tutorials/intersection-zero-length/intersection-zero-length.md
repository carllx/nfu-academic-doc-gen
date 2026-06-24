# How To: Intersection Zero Length

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test intersection zero length

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: period_1, period_2, sort
```

## Step-by-Step Guide

### Step 1: Assign index_1 = timedelta_range(...)

```python
index_1 = timedelta_range('1 day', periods=period_1, freq='h')
```

### Step 2: Assign index_2 = timedelta_range(...)

```python
index_2 = timedelta_range('1 day', periods=period_2, freq='h')
```

### Step 3: Assign expected = timedelta_range(...)

```python
expected = timedelta_range('1 day', periods=0, freq='h')
```

### Step 4: Assign result = index_1.intersection(...)

```python
result = index_1.intersection(index_2, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: period_1, period_2, sort

# Workflow
index_1 = timedelta_range('1 day', periods=period_1, freq='h')
index_2 = timedelta_range('1 day', periods=period_2, freq='h')
expected = timedelta_range('1 day', periods=0, freq='h')
result = index_1.intersection(index_2, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:125 | Complexity: Intermediate | Last updated: 2026-06-02*