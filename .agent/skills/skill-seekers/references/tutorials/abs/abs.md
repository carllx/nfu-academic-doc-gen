# How To: Abs

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test abs

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign vals = np.array(...)

```python
vals = np.array([-3600 * 10 ** 9, 'NaT', 7200 * 10 ** 9], dtype='m8[ns]')
```

### Step 2: Assign arr = TimedeltaArray._from_sequence(...)

```python
arr = TimedeltaArray._from_sequence(vals)
```

### Step 3: Assign evals = np.array(...)

```python
evals = np.array([3600 * 10 ** 9, 'NaT', 7200 * 10 ** 9], dtype='m8[ns]')
```

### Step 4: Assign expected = TimedeltaArray._from_sequence(...)

```python
expected = TimedeltaArray._from_sequence(evals)
```

### Step 5: Assign result = abs(...)

```python
result = abs(arr)
```

### Step 6: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```

### Step 7: Assign result2 = np.abs(...)

```python
result2 = np.abs(arr)
```

### Step 8: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result2, expected)
```


## Complete Example

```python
# Workflow
vals = np.array([-3600 * 10 ** 9, 'NaT', 7200 * 10 ** 9], dtype='m8[ns]')
arr = TimedeltaArray._from_sequence(vals)
evals = np.array([3600 * 10 ** 9, 'NaT', 7200 * 10 ** 9], dtype='m8[ns]')
expected = TimedeltaArray._from_sequence(evals)
result = abs(arr)
tm.assert_timedelta_array_equal(result, expected)
result2 = np.abs(arr)
tm.assert_timedelta_array_equal(result2, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:265 | Complexity: Advanced | Last updated: 2026-06-02*