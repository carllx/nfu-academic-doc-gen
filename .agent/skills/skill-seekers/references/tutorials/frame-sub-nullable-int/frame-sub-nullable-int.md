# How To: Frame Sub Nullable Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame sub nullable int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`

**Setup Required:**
```python
# Fixtures: any_int_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign series1 = Series(...)

```python
series1 = Series([1, 2, None], dtype=any_int_ea_dtype)
```

### Step 2: Assign series2 = Series(...)

```python
series2 = Series([1, 2, 3], dtype=any_int_ea_dtype)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([0, 0, None], dtype=any_int_ea_dtype)
```

### Step 4: Assign result = value

```python
result = series1.to_frame() - series2.to_frame()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_int_ea_dtype

# Workflow
series1 = Series([1, 2, None], dtype=any_int_ea_dtype)
series2 = Series([1, 2, 3], dtype=any_int_ea_dtype)
expected = DataFrame([0, 0, None], dtype=any_int_ea_dtype)
result = series1.to_frame() - series2.to_frame()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:2070 | Complexity: Intermediate | Last updated: 2026-06-02*