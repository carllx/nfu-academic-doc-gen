# How To: Return Type Doesnt Depend On Monotonicity

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test return type doesnt depend on monotonicity

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(start='2015-5-13 23:59:00', freq='min', periods=3)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(3), index=dti)
```

### Step 3: Assign ser2 = Series(...)

```python
ser2 = Series(range(3), index=[dti[1], dti[0], dti[2]])
```

### Step 4: Assign key = '2015-5-14 00'

```python
key = '2015-5-14 00'
```

### Step 5: Assign result = value

```python
result = ser.loc[key]
```

### Step 6: Assign expected = value

```python
expected = ser.iloc[1:]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = ser.iloc[::-1].loc[key]
```

### Step 9: Assign expected = value

```python
expected = ser.iloc[::-1][:-1]
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result2 = value

```python
result2 = ser2.loc[key]
```

### Step 12: Assign expected2 = value

```python
expected2 = ser2.iloc[::2]
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected2)
```


## Complete Example

```python
# Workflow
dti = date_range(start='2015-5-13 23:59:00', freq='min', periods=3)
ser = Series(range(3), index=dti)
ser2 = Series(range(3), index=[dti[1], dti[0], dti[2]])
key = '2015-5-14 00'
result = ser.loc[key]
expected = ser.iloc[1:]
tm.assert_series_equal(result, expected)
result = ser.iloc[::-1].loc[key]
expected = ser.iloc[::-1][:-1]
tm.assert_series_equal(result, expected)
result2 = ser2.loc[key]
expected2 = ser2.iloc[::2]
tm.assert_series_equal(result2, expected2)
```

## Next Steps


---

*Source: test_partial_slicing.py:42 | Complexity: Advanced | Last updated: 2026-06-02*