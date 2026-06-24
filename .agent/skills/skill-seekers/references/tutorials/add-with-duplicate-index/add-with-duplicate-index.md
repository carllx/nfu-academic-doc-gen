# How To: Add With Duplicate Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add with duplicate index

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.computation`
- `pandas.core.computation.check`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series([1, 2], index=[1, 1])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series([10, 10], index=[1, 2])
```

### Step 3: Assign result = value

```python
result = s1 + s2
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([11, 12, np.nan], index=[1, 1, 2])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
s1 = Series([1, 2], index=[1, 1])
s2 = Series([10, 10], index=[1, 2])
result = s1 + s2
expected = Series([11, 12, np.nan], index=[1, 1, 2])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:220 | Complexity: Intermediate | Last updated: 2026-06-02*