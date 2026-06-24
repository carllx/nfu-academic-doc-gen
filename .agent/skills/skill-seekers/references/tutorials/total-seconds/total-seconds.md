# How To: Total Seconds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test total seconds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: unit, tda
```

## Step-by-Step Guide

### Step 1: Assign as_nano = tda._ndarray.astype(...)

```python
as_nano = tda._ndarray.astype('m8[ns]')
```

### Step 2: Assign tda_nano = TimedeltaArray._simple_new(...)

```python
tda_nano = TimedeltaArray._simple_new(as_nano, dtype=as_nano.dtype)
```

### Step 3: Assign result = tda.total_seconds(...)

```python
result = tda.total_seconds()
```

### Step 4: Assign expected = tda_nano.total_seconds(...)

```python
expected = tda_nano.total_seconds()
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit, tda

# Workflow
as_nano = tda._ndarray.astype('m8[ns]')
tda_nano = TimedeltaArray._simple_new(as_nano, dtype=as_nano.dtype)
result = tda.total_seconds()
expected = tda_nano.total_seconds()
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*