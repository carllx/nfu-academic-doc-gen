# How To: Where Doesnt Retain Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where doesnt retain freq

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.frequencies`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('20130101', periods=3, freq='D', name='idx')
```

### Step 2: Assign cond = value

```python
cond = [True, True, False]
```

### Step 3: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([dti[0], dti[1], dti[0]], freq=None, name='idx')
```

### Step 4: Assign result = dti.where(...)

```python
result = dti.where(cond, dti[::-1])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('20130101', periods=3, freq='D', name='idx')
cond = [True, True, False]
expected = DatetimeIndex([dti[0], dti[1], dti[0]], freq=None, name='idx')
result = dti.where(cond, dti[::-1])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*