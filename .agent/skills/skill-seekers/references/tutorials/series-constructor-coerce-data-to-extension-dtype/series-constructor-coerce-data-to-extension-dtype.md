# How To: Series Constructor Coerce Data To Extension Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series constructor coerce data to extension dtype

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

### Step 1: Assign dtype = DecimalDtype(...)

```python
dtype = DecimalDtype()
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, 1, 2], dtype=dtype)
```

### Step 3: Assign arr = DecimalArray(...)

```python
arr = DecimalArray([decimal.Decimal(0), decimal.Decimal(1), decimal.Decimal(2)], dtype=dtype)
```

### Step 4: Assign exp = pd.Series(...)

```python
exp = pd.Series(arr)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, exp)
```


## Complete Example

```python
# Workflow
dtype = DecimalDtype()
ser = pd.Series([0, 1, 2], dtype=dtype)
arr = DecimalArray([decimal.Decimal(0), decimal.Decimal(1), decimal.Decimal(2)], dtype=dtype)
exp = pd.Series(arr)
tm.assert_series_equal(ser, exp)
```

## Next Steps


---

*Source: test_decimal.py:320 | Complexity: Intermediate | Last updated: 2026-06-02*