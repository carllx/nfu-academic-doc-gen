# How To: Series Constructor With Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series constructor with dtype

## Prerequisites

**Required Modules:**
- `__future__`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.extension`
- `pandas.tests.extension.decimal.array`


## Step-by-Step Guide

### Step 1: Assign arr = DecimalArray(...)

```python
arr = DecimalArray([decimal.Decimal('10.0')])
```

### Step 2: Assign result = pd.Series(...)

```python
result = pd.Series(arr, dtype=DecimalDtype())
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(arr)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = pd.Series(...)

```python
result = pd.Series(arr, dtype='int64')
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series([10])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = DecimalArray([decimal.Decimal('10.0')])
result = pd.Series(arr, dtype=DecimalDtype())
expected = pd.Series(arr)
tm.assert_series_equal(result, expected)
result = pd.Series(arr, dtype='int64')
expected = pd.Series([10])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:332 | Complexity: Intermediate | Last updated: 2026-06-02*