# How To: Compare Timedeltalike Scalar

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare timedeltalike scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: box_with_array, td_scalar
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign xbox = value

```python
xbox = box if box not in [Index, pd.array] else np.ndarray
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([timedelta(days=1), timedelta(days=2)])
```

### Step 4: Assign ser = tm.box_expected(...)

```python
ser = tm.box_expected(ser, box)
```

### Step 5: Assign actual = value

```python
actual = ser > td_scalar
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([False, True])
```

### Step 7: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(actual, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box_with_array, td_scalar

# Workflow
box = box_with_array
xbox = box if box not in [Index, pd.array] else np.ndarray
ser = Series([timedelta(days=1), timedelta(days=2)])
ser = tm.box_expected(ser, box)
actual = ser > td_scalar
expected = Series([False, True])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(actual, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:91 | Complexity: Advanced | Last updated: 2026-06-02*