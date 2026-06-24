# How To: Cumsum

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cumsum

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = f'm8[{unit}]'
```

### Step 2: Assign arr = TimedeltaArray._from_sequence(...)

```python
arr = TimedeltaArray._from_sequence(['1D', '2D'], dtype=dtype)
```

### Step 3: Assign result = arr._accumulate(...)

```python
result = arr._accumulate('cumsum')
```

### Step 4: Assign expected = TimedeltaArray._from_sequence(...)

```python
expected = TimedeltaArray._from_sequence(['1D', '3D'], dtype=dtype)
```

### Step 5: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
dtype = f'm8[{unit}]'
arr = TimedeltaArray._from_sequence(['1D', '2D'], dtype=dtype)
result = arr._accumulate('cumsum')
expected = TimedeltaArray._from_sequence(['1D', '3D'], dtype=dtype)
tm.assert_timedelta_array_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*