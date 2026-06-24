# How To: Categorical Tuple Equality

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical tuple equality

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([(0, 0), (0, 1), (0, 0), (1, 0), (1, 1)])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([True, False, True, False, False])
```

### Step 3: Assign result = value

```python
result = ser == (0, 0)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = ser.astype('category') == (0, 0)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([(0, 0), (0, 1), (0, 0), (1, 0), (1, 1)])
expected = Series([True, False, True, False, False])
result = ser == (0, 0)
tm.assert_series_equal(result, expected)
result = ser.astype('category') == (0, 0)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_categorical.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*