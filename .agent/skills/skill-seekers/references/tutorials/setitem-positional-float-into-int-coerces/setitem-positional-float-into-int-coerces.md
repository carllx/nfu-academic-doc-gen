# How To: Setitem Positional Float Into Int Coerces

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem positional float into int coerces

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

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], index=['a', 'b', 'c'])
```

### Step 2: Assign warn_msg = 'Series.__setitem__ treating keys as positions is deprecated'

```python
warn_msg = 'Series.__setitem__ treating keys as positions is deprecated'
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1.5, 2, 3], index=['a', 'b', 'c'])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 5: Assign unknown = 1.5

```python
ser[0] = 1.5
```


## Complete Example

```python
# Workflow
ser = Series([1, 2, 3], index=['a', 'b', 'c'])
warn_msg = 'Series.__setitem__ treating keys as positions is deprecated'
with tm.assert_produces_warning(FutureWarning, match=warn_msg):
    ser[0] = 1.5
expected = Series([1.5, 2, 3], index=['a', 'b', 'c'])
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_setitem.py:1735 | Complexity: Intermediate | Last updated: 2026-06-02*