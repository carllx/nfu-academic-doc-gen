# How To: Replace Listlike Value Listlike Target

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace listlike value listlike target

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(datetime_series.index)
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
```

### Step 3: Assign msg = 'Replacement lists must match in length\\. Expecting 3 got 2'

```python
msg = 'Replacement lists must match in length\\. Expecting 3 got 2'
```

### Step 4: Assign result = ser.replace(...)

```python
result = ser.replace([1, 2], [np.nan, 0])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ser)
```

### Step 6: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, 1, 2, 3, 4])
```

### Step 7: Assign result = ser.replace(...)

```python
result = ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, pd.Series([4, 3, 2, 1, 0]))
```

### Step 9: Call ser.replace()

```python
ser.replace([1, 2, 3], [np.nan, 0])
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
ser = pd.Series(datetime_series.index)
tm.assert_series_equal(ser.replace(np.nan, 0), ser.fillna(0))
msg = 'Replacement lists must match in length\\. Expecting 3 got 2'
with pytest.raises(ValueError, match=msg):
    ser.replace([1, 2, 3], [np.nan, 0])
result = ser.replace([1, 2], [np.nan, 0])
tm.assert_series_equal(result, ser)
ser = pd.Series([0, 1, 2, 3, 4])
result = ser.replace([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
tm.assert_series_equal(result, pd.Series([4, 3, 2, 1, 0]))
```

## Next Steps


---

*Source: test_replace.py:121 | Complexity: Advanced | Last updated: 2026-06-02*