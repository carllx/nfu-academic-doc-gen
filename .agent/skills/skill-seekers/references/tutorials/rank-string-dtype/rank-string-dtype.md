# How To: Rank String Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rank string dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: string_dtype_no_object
```

## Step-by-Step Guide

### Step 1: Assign obj = Series(...)

```python
obj = Series(['foo', 'foo', None, 'foo'], dtype=string_dtype_no_object)
```

### Step 2: Assign result = obj.rank(...)

```python
result = obj.rank(method='first')
```

### Step 3: Assign exp_dtype = value

```python
exp_dtype = 'Float64' if string_dtype_no_object == 'string[pyarrow]' else 'float64'
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 2, None, 3], dtype=exp_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign exp_dtype = 'float64'

```python
exp_dtype = 'float64'
```


## Complete Example

```python
# Setup
# Fixtures: string_dtype_no_object

# Workflow
obj = Series(['foo', 'foo', None, 'foo'], dtype=string_dtype_no_object)
result = obj.rank(method='first')
exp_dtype = 'Float64' if string_dtype_no_object == 'string[pyarrow]' else 'float64'
if string_dtype_no_object.storage == 'python':
    exp_dtype = 'float64'
expected = Series([1, 2, None, 3], dtype=exp_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:496 | Complexity: Intermediate | Last updated: 2026-06-02*