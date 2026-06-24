# How To: Fillna Limit

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna limit

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(np.nan, index=[0, 1, 2])
```

### Step 2: Assign result = ser.fillna(...)

```python
result = ser.fillna(999, limit=1)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([999, np.nan, np.nan], index=[0, 1, 2])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.fillna(...)

```python
result = ser.fillna(999, limit=2)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([999, 999, np.nan], index=[0, 1, 2])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(np.nan, index=[0, 1, 2])
result = ser.fillna(999, limit=1)
expected = Series([999, np.nan, np.nan], index=[0, 1, 2])
tm.assert_series_equal(result, expected)
result = ser.fillna(999, limit=2)
expected = Series([999, 999, np.nan], index=[0, 1, 2])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*