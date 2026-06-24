# How To: Round Builtin

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round builtin

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
# Fixtures: any_float_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1.123, 2.123, 3.123], index=range(3), dtype=any_float_dtype)
```

### Step 2: Assign result = round(...)

```python
result = round(ser)
```

### Step 3: Assign expected_rounded0 = Series(...)

```python
expected_rounded0 = Series([1.0, 2.0, 3.0], index=range(3), dtype=any_float_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_rounded0)
```

### Step 5: Assign decimals = 2

```python
decimals = 2
```

### Step 6: Assign expected_rounded = Series(...)

```python
expected_rounded = Series([1.12, 2.12, 3.12], index=range(3), dtype=any_float_dtype)
```

### Step 7: Assign result = round(...)

```python
result = round(ser, decimals)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_rounded)
```


## Complete Example

```python
# Setup
# Fixtures: any_float_dtype

# Workflow
ser = Series([1.123, 2.123, 3.123], index=range(3), dtype=any_float_dtype)
result = round(ser)
expected_rounded0 = Series([1.0, 2.0, 3.0], index=range(3), dtype=any_float_dtype)
tm.assert_series_equal(result, expected_rounded0)
decimals = 2
expected_rounded = Series([1.12, 2.12, 3.12], index=range(3), dtype=any_float_dtype)
result = round(ser, decimals)
tm.assert_series_equal(result, expected_rounded)
```

## Next Steps


---

*Source: test_round.py:38 | Complexity: Advanced | Last updated: 2026-06-02*