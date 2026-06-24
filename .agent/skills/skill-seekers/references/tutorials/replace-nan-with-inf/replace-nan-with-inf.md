# How To: Replace Nan With Inf

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace nan with inf

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([np.nan, 0, np.inf])
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
```

### Step 3: Assign ser = pd.Series(...)

```python
ser = pd.Series([np.nan, 0, 'foo', 'bar', np.inf, None, pd.NaT])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
```

### Step 5: Assign filled = ser.copy(...)

```python
filled = ser.copy()
```

### Step 6: Assign unknown = 0

```python
filled[4] = 0
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.replace(np.inf, 0), filled)
```


## Complete Example

```python
# Workflow
ser = pd.Series([np.nan, 0, np.inf])
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
ser = pd.Series([np.nan, 0, 'foo', 'bar', np.inf, None, pd.NaT])
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
filled = ser.copy()
filled[4] = 0
tm.assert_series_equal(ser.replace(np.inf, 0), filled)
```

## Next Steps


---

*Source: test_replace.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*