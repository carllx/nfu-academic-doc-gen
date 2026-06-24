# How To: Combine Scalar

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine scalar

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([i * 10 for i in range(5)])
```

### Step 2: Assign result = ser.combine(...)

```python
result = ser.combine(3, lambda x, y: x + y)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([i * 10 + 3 for i in range(5)])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.combine(...)

```python
result = ser.combine(22, lambda x, y: min(x, y))
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([min(i * 10, 22) for i in range(5)])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([i * 10 for i in range(5)])
result = ser.combine(3, lambda x, y: x + y)
expected = Series([i * 10 + 3 for i in range(5)])
tm.assert_series_equal(result, expected)
result = ser.combine(22, lambda x, y: min(x, y))
expected = Series([min(i * 10, 22) for i in range(5)])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_combine.py:6 | Complexity: Intermediate | Last updated: 2026-06-02*