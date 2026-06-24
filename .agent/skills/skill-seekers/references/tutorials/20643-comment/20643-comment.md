# How To: 20643 Comment

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 20643 comment

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `os`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign orig = Series(...)

```python
orig = Series([0, 1, 2], index=['a', 'b', 'c'])
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([np.nan, 1, 2], index=['a', 'b', 'c'])
```

### Step 3: Assign ser = orig.copy(...)

```python
ser = orig.copy()
```

### Step 4: Assign unknown = None

```python
ser.iat[0] = None
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 6: Assign ser = orig.copy(...)

```python
ser = orig.copy()
```

### Step 7: Assign unknown = None

```python
ser.iloc[0] = None
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```


## Complete Example

```python
# Workflow
orig = Series([0, 1, 2], index=['a', 'b', 'c'])
expected = Series([np.nan, 1, 2], index=['a', 'b', 'c'])
ser = orig.copy()
ser.iat[0] = None
tm.assert_series_equal(ser, expected)
ser = orig.copy()
ser.iloc[0] = None
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_setitem.py:1613 | Complexity: Advanced | Last updated: 2026-06-02*