# How To: Where Downcast To Td64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where downcast to td64

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3])
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False])
```

### Step 3: Assign td = pd.Timedelta(...)

```python
td = pd.Timedelta(days=1)
```

### Step 4: Assign msg = "Downcasting behavior in Series and DataFrame methods 'where'"

```python
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([td, td, td], dtype='m8[ns]')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 7: Assign expected2 = expected.astype(...)

```python
expected2 = expected.astype(object)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, expected2)
```

### Step 9: Assign res = ser.where(...)

```python
res = ser.where(mask, td)
```

### Step 10: Assign res2 = ser.where(...)

```python
res2 = ser.where(mask, td)
```


## Complete Example

```python
# Workflow
ser = Series([1, 2, 3])
mask = np.array([False, False, False])
td = pd.Timedelta(days=1)
msg = "Downcasting behavior in Series and DataFrame methods 'where'"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = ser.where(mask, td)
expected = Series([td, td, td], dtype='m8[ns]')
tm.assert_series_equal(res, expected)
with pd.option_context('future.no_silent_downcasting', True):
    with tm.assert_produces_warning(None, match=msg):
        res2 = ser.where(mask, td)
expected2 = expected.astype(object)
tm.assert_series_equal(res2, expected2)
```

## Next Steps


---

*Source: test_where.py:999 | Complexity: Advanced | Last updated: 2026-06-02*