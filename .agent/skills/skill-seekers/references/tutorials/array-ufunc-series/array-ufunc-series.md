# How To: Array Ufunc Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array ufunc series

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

### Step 1: Assign a = to_decimal(...)

```python
a = to_decimal([1, 2, 3])
```

### Step 2: Assign s = pd.Series(...)

```python
s = pd.Series(a)
```

### Step 3: Assign result = np.exp(...)

```python
result = np.exp(s)
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(to_decimal(np.exp(a._data)))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = to_decimal([1, 2, 3])
s = pd.Series(a)
result = np.exp(s)
expected = pd.Series(to_decimal(np.exp(a._data)))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_decimal.py:462 | Complexity: Intermediate | Last updated: 2026-06-02*