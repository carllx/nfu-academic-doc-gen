# How To: Round Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test round nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, freq, unit
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([pd.NaT], dtype=f'M8[{unit}]')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(pd.NaT, dtype=f'M8[{unit}]')
```

### Step 3: Assign round_method = getattr(...)

```python
round_method = getattr(ser.dt, method)
```

### Step 4: Assign result = round_method(...)

```python
result = round_method(freq)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, freq, unit

# Workflow
ser = Series([pd.NaT], dtype=f'M8[{unit}]')
expected = Series(pd.NaT, dtype=f'M8[{unit}]')
round_method = getattr(ser.dt, method)
result = round_method(freq)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_round.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*