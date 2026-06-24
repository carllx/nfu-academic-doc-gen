# How To: Nlargest Misc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nlargest misc

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([3.0, np.nan, 1, 2, 5])
```

### Step 2: Assign result = ser.nlargest(...)

```python
result = ser.nlargest()
```

### Step 3: Assign expected = value

```python
expected = ser.iloc[[4, 0, 3, 2, 1]]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.nsmallest(...)

```python
result = ser.nsmallest()
```

### Step 6: Assign expected = value

```python
expected = ser.iloc[[2, 3, 0, 4, 1]]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign msg = 'keep must be either "first", "last"'

```python
msg = 'keep must be either "first", "last"'
```

### Step 9: Assign ser = Series(...)

```python
ser = Series([1] * 5, index=[1, 2, 3, 4, 5])
```

### Step 10: Assign expected_first = Series(...)

```python
expected_first = Series([1] * 3, index=[1, 2, 3])
```

### Step 11: Assign expected_last = Series(...)

```python
expected_last = Series([1] * 3, index=[5, 4, 3])
```

### Step 12: Assign result = ser.nsmallest(...)

```python
result = ser.nsmallest(3)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_first)
```

### Step 14: Assign result = ser.nsmallest(...)

```python
result = ser.nsmallest(3, keep='last')
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_last)
```

### Step 16: Assign result = ser.nlargest(...)

```python
result = ser.nlargest(3)
```

### Step 17: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_first)
```

### Step 18: Assign result = ser.nlargest(...)

```python
result = ser.nlargest(3, keep='last')
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_last)
```

### Step 20: Call ser.nsmallest()

```python
ser.nsmallest(keep='invalid')
```

### Step 21: Call ser.nlargest()

```python
ser.nlargest(keep='invalid')
```


## Complete Example

```python
# Workflow
ser = Series([3.0, np.nan, 1, 2, 5])
result = ser.nlargest()
expected = ser.iloc[[4, 0, 3, 2, 1]]
tm.assert_series_equal(result, expected)
result = ser.nsmallest()
expected = ser.iloc[[2, 3, 0, 4, 1]]
tm.assert_series_equal(result, expected)
msg = 'keep must be either "first", "last"'
with pytest.raises(ValueError, match=msg):
    ser.nsmallest(keep='invalid')
with pytest.raises(ValueError, match=msg):
    ser.nlargest(keep='invalid')
ser = Series([1] * 5, index=[1, 2, 3, 4, 5])
expected_first = Series([1] * 3, index=[1, 2, 3])
expected_last = Series([1] * 3, index=[5, 4, 3])
result = ser.nsmallest(3)
tm.assert_series_equal(result, expected_first)
result = ser.nsmallest(3, keep='last')
tm.assert_series_equal(result, expected_last)
result = ser.nlargest(3)
tm.assert_series_equal(result, expected_first)
result = ser.nlargest(3, keep='last')
tm.assert_series_equal(result, expected_last)
```

## Next Steps


---

*Source: test_nlargest.py:127 | Complexity: Advanced | Last updated: 2026-06-02*