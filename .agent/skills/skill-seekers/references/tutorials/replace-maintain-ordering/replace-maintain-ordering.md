# How To: Replace Maintain Ordering

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace maintain ordering

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = pd.CategoricalDtype(...)

```python
dtype = pd.CategoricalDtype([0, 1, 2], ordered=True)
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, 1, 2], dtype=dtype)
```

### Step 3: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

### Step 4: Assign expected_dtype = pd.CategoricalDtype(...)

```python
expected_dtype = pd.CategoricalDtype([1, 2], ordered=True)
```

### Step 5: Assign expected = pd.Series(...)

```python
expected = pd.Series([2, 1, 2], dtype=expected_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result, check_category_order=True)
```

### Step 7: Assign result = ser.replace(...)

```python
result = ser.replace(0, 2)
```


## Complete Example

```python
# Workflow
dtype = pd.CategoricalDtype([0, 1, 2], ordered=True)
ser = pd.Series([0, 1, 2], dtype=dtype)
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.replace(0, 2)
expected_dtype = pd.CategoricalDtype([1, 2], ordered=True)
expected = pd.Series([2, 1, 2], dtype=expected_dtype)
tm.assert_series_equal(expected, result, check_category_order=True)
```

## Next Steps


---

*Source: test_replace.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*