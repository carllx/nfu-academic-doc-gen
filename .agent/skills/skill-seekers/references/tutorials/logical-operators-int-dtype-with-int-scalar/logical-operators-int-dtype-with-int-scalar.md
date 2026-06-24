# How To: Logical Operators Int Dtype With Int Scalar

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test logical operators int dtype with int scalar

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign s_0123 = Series(...)

```python
s_0123 = Series(range(4), dtype='int64')
```

### Step 2: Assign res = value

```python
res = s_0123 & 0
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([0] * 4)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 5: Assign res = value

```python
res = s_0123 & 1
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([0, 1, 0, 1])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
s_0123 = Series(range(4), dtype='int64')
res = s_0123 & 0
expected = Series([0] * 4)
tm.assert_series_equal(res, expected)
res = s_0123 & 1
expected = Series([0, 1, 0, 1])
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_logical_ops.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*