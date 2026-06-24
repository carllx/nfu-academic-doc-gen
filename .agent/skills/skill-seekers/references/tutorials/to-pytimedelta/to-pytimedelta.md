# How To: To Pytimedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to pytimedelta

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
# Fixtures: tda
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

### Step 3: Assign result = tda.to_pytimedelta(...)

```python
result = tda.to_pytimedelta()
```

### Step 4: Assign expected = tda_nano.to_pytimedelta(...)

```python
expected = tda_nano.to_pytimedelta()
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tda

# Workflow
as_nano = tda._ndarray.astype('m8[ns]')
tda_nano = TimedeltaArray._simple_new(as_nano, dtype=as_nano.dtype)
result = tda.to_pytimedelta()
expected = tda_nano.to_pytimedelta()
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_timedeltas.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*