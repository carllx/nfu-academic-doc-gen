# How To: Searchsorted Datetime64 List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test searchsorted datetime64 list

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('20120101', periods=10, freq='2D'))
```

### Step 2: Assign vals = value

```python
vals = [Timestamp('20120102'), Timestamp('20120104')]
```

### Step 3: Assign res = ser.searchsorted(...)

```python
res = ser.searchsorted(vals)
```

### Step 4: Assign exp = np.array(...)

```python
exp = np.array([1, 2], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series(date_range('20120101', periods=10, freq='2D'))
vals = [Timestamp('20120102'), Timestamp('20120104')]
res = ser.searchsorted(vals)
exp = np.array([1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(res, exp)
```

## Next Steps


---

*Source: test_searchsorted.py:57 | Complexity: Intermediate | Last updated: 2026-06-02*