# How To: Base Constructor With Period Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test base constructor with period dtype

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign dtype = PeriodDtype(...)

```python
dtype = PeriodDtype('D')
```

### Step 2: Assign values = value

```python
values = ['2011-01-01', '2012-03-04', '2014-05-01']
```

### Step 3: Assign result = Index(...)

```python
result = Index(values, dtype=dtype)
```

### Step 4: Assign expected = PeriodIndex(...)

```python
expected = PeriodIndex(values, dtype=dtype)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dtype = PeriodDtype('D')
values = ['2011-01-01', '2012-03-04', '2014-05-01']
result = Index(values, dtype=dtype)
expected = PeriodIndex(values, dtype=dtype)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*