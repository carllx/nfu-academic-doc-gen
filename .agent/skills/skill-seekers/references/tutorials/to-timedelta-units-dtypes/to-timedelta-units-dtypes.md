# How To: To Timedelta Units Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to timedelta units dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: dtype, unit
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1] * 5, dtype=dtype)
```

### Step 2: Assign result = to_timedelta(...)

```python
result = to_timedelta(arr, unit=unit)
```

### Step 3: Assign exp_dtype = value

```python
exp_dtype = 'm8[ns]' if dtype == 'int64' else 'm8[s]'
```

### Step 4: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([np.timedelta64(1, unit)] * 5, dtype=exp_dtype)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, unit

# Workflow
arr = np.array([1] * 5, dtype=dtype)
result = to_timedelta(arr, unit=unit)
exp_dtype = 'm8[ns]' if dtype == 'int64' else 'm8[s]'
expected = TimedeltaIndex([np.timedelta64(1, unit)] * 5, dtype=exp_dtype)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_to_timedelta.py:79 | Complexity: Intermediate | Last updated: 2026-06-02*