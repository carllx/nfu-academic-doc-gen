# How To: All Numeric Unary Operators

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test all numeric unary operators

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype, source, neg_target, abs_target
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_numeric_ea_dtype

```python
dtype = any_numeric_ea_dtype
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(source, dtype=dtype)
```

### Step 3: Assign unknown = value

```python
neg_result, pos_result, abs_result = (-ser, +ser, abs(ser))
```

### Step 4: Assign abs_target = Series(...)

```python
abs_target = Series(abs_target, dtype=dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(neg_result, neg_target)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(pos_result, ser)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(abs_result, abs_target)
```

### Step 8: Assign neg_target = value

```python
neg_target = -Series(source, dtype=dtype)
```

### Step 9: Assign neg_target = Series(...)

```python
neg_target = Series(neg_target, dtype=dtype)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype, source, neg_target, abs_target

# Workflow
dtype = any_numeric_ea_dtype
ser = Series(source, dtype=dtype)
neg_result, pos_result, abs_result = (-ser, +ser, abs(ser))
if dtype.startswith('U'):
    neg_target = -Series(source, dtype=dtype)
else:
    neg_target = Series(neg_target, dtype=dtype)
abs_target = Series(abs_target, dtype=dtype)
tm.assert_series_equal(neg_result, neg_target)
tm.assert_series_equal(pos_result, ser)
tm.assert_series_equal(abs_result, abs_target)
```

## Next Steps


---

*Source: test_unary.py:25 | Complexity: Advanced | Last updated: 2026-06-02*