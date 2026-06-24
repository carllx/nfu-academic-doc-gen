# How To: Rank Max Pct

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank max pct

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
result = s.rank(method='max', pct=True)
```

### Step 3: Assign expected = Series.astype(...)

```python
expected = Series(exp).astype(expected_dtype(dtype, 'max', pct=True))
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
result = s.rank(method='max', pct=True)
expected = Series(exp).astype(expected_dtype(dtype, 'max', pct=True))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:503 | Complexity: Intermediate | Last updated: 2026-06-02*