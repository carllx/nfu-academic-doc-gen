# How To: Diff Dt64

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff dt64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('20130102', periods=5))
```

### Step 2: Assign result = ser.diff(...)

```python
result = ser.diff()
```

### Step 3: Assign expected = value

```python
expected = ser - ser.shift(1)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = result - result.shift(1)
```

### Step 6: Assign expected = expected.diff(...)

```python
expected = expected.diff()
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(date_range('20130102', periods=5))
result = ser.diff()
expected = ser - ser.shift(1)
tm.assert_series_equal(result, expected)
result = result - result.shift(1)
expected = expected.diff()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*