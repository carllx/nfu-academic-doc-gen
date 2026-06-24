# How To: Rank Dense Method

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank dense method

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: dtype, ser, exp
```

## Step-by-Step Guide

### Step 1: Assign s = Series.astype(...)

```python
s = Series(ser).astype(dtype)
```

### Step 2: Assign result = s.rank(...)

```python
result = s.rank(method='dense')
```

### Step 3: Assign expected = Series.astype(...)

```python
expected = Series(exp).astype(expected_dtype(dtype, 'dense'))
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign exp = value

```python
exp = exp[::-1]
```


## Complete Example

```python
# Setup
# Fixtures: dtype, ser, exp

# Workflow
if ser[0] < 0 and dtype.startswith('str'):
    exp = exp[::-1]
s = Series(ser).astype(dtype)
result = s.rank(method='dense')
expected = Series(exp).astype(expected_dtype(dtype, 'dense'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:372 | Complexity: Intermediate | Last updated: 2026-06-02*