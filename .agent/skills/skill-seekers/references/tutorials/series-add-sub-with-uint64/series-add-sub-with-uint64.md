# How To: Series Add Sub With Uint64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series add sub with UInt64

## Prerequisites

**Required Modules:**
- `__future__`
- `collections`
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign series1 = Series(...)

```python
series1 = Series([1, 2, 3])
```

### Step 2: Assign series2 = Series(...)

```python
series2 = Series([2, 1, 3], dtype='UInt64')
```

### Step 3: Assign result = value

```python
result = series1 + series2
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([3, 3, 6], dtype='Float64')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = series1 - series2
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([-1, 1, 0], dtype='Float64')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
series1 = Series([1, 2, 3])
series2 = Series([2, 1, 3], dtype='UInt64')
result = series1 + series2
expected = Series([3, 3, 6], dtype='Float64')
tm.assert_series_equal(result, expected)
result = series1 - series2
expected = Series([-1, 1, 0], dtype='Float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:1556 | Complexity: Advanced | Last updated: 2026-06-02*