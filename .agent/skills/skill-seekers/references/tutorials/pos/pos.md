# How To: Pos

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pos

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

**Verification:**
```python
assert not tm.shares_memory(result, arr)
```

### Step 2: Assign arr = TimedeltaArray._from_sequence(...)

```python
arr = TimedeltaArray._from_sequence(vals)
```

**Verification:**
```python
assert not tm.shares_memory(result2, arr)
```

### Step 3: Assign result = value

```python
result = +arr
```

### Step 4: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, arr)
```

**Verification:**
```python
assert not tm.shares_memory(result, arr)
```

### Step 5: Assign result2 = np.positive(...)

```python
result2 = np.positive(arr)
```

### Step 6: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result2, arr)
```

**Verification:**
```python
assert not tm.shares_memory(result2, arr)
```


## Complete Example

```python
# Workflow
vals = np.array([-3600 * 10 ** 9, 'NaT', 7200 * 10 ** 9], dtype='m8[ns]')
arr = TimedeltaArray._from_sequence(vals)
result = +arr
tm.assert_timedelta_array_equal(result, arr)
assert not tm.shares_memory(result, arr)
result2 = np.positive(arr)
tm.assert_timedelta_array_equal(result2, arr)
assert not tm.shares_memory(result2, arr)
```

## Next Steps


---

*Source: test_timedeltas.py:278 | Complexity: Intermediate | Last updated: 2026-06-02*