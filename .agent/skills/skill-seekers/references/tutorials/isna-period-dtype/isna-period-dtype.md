# How To: Isna Period Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isna period dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([Period('2011-01', freq='M'), Period('NaT', freq='M')])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False, True])
```

### Step 3: Assign result = ser.isna(...)

```python
result = ser.isna()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.notna(...)

```python
result = ser.notna()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ~expected)
```


## Complete Example

```python
# Workflow
ser = Series([Period('2011-01', freq='M'), Period('NaT', freq='M')])
expected = Series([False, True])
result = ser.isna()
tm.assert_series_equal(result, expected)
result = ser.notna()
tm.assert_series_equal(result, ~expected)
```

## Next Steps


---

*Source: test_isna.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*