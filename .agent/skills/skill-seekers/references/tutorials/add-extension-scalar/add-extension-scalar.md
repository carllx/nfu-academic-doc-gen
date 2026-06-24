# How To: Add Extension Scalar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test add extension scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`

**Setup Required:**
```python
# Fixtures: other, box_with_array, op
```

## Step-by-Step Guide

### Step 1: Assign arr = Series(...)

```python
arr = Series(['a', 'b', 'c'])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([op(x, other) for x in arr])
```

### Step 3: Assign arr = tm.box_expected(...)

```python
arr = tm.box_expected(arr, box_with_array)
```

### Step 4: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, box_with_array)
```

### Step 5: Assign result = op(...)

```python
result = op(arr, other)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: other, box_with_array, op

# Workflow
arr = Series(['a', 'b', 'c'])
expected = Series([op(x, other) for x in arr])
arr = tm.box_expected(arr, box_with_array)
expected = tm.box_expected(expected, box_with_array)
result = op(arr, other)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_object.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*