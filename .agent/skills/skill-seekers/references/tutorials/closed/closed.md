# How To: Closed

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test closed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: regular, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex.as_unit(...)

```python
dti = DatetimeIndex([Timestamp('20130101 09:00:01'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:04'), Timestamp('20130101 09:00:06')]).as_unit(unit)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1] * 5}, index=dti)
```

### Step 3: Assign msg = "closed must be 'right', 'left', 'both' or 'neither'"

```python
msg = "closed must be 'right', 'left', 'both' or 'neither'"
```

### Step 4: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 5: Assign unknown = value

```python
expected['A'] = [1.0, 2, 2, 2, 1]
```

### Step 6: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s', closed='right').sum()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s').sum()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 11: Assign unknown = value

```python
expected['A'] = [1.0, 2, 3, 3, 2]
```

### Step 12: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s', closed='both').sum()
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 15: Assign unknown = value

```python
expected['A'] = [np.nan, 1.0, 2, 2, 1]
```

### Step 16: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s', closed='left').sum()
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 19: Assign unknown = value

```python
expected['A'] = [np.nan, 1.0, 1, 1, np.nan]
```

### Step 20: Assign result = df.rolling.sum(...)

```python
result = df.rolling('2s', closed='neither').sum()
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 22: Call regular.rolling()

```python
regular.rolling(window='2s', closed='blabla')
```


## Complete Example

```python
# Setup
# Fixtures: regular, unit

# Workflow
dti = DatetimeIndex([Timestamp('20130101 09:00:01'), Timestamp('20130101 09:00:02'), Timestamp('20130101 09:00:03'), Timestamp('20130101 09:00:04'), Timestamp('20130101 09:00:06')]).as_unit(unit)
df = DataFrame({'A': [1] * 5}, index=dti)
msg = "closed must be 'right', 'left', 'both' or 'neither'"
with pytest.raises(ValueError, match=msg):
    regular.rolling(window='2s', closed='blabla')
expected = df.copy()
expected['A'] = [1.0, 2, 2, 2, 1]
result = df.rolling('2s', closed='right').sum()
tm.assert_frame_equal(result, expected)
result = df.rolling('2s').sum()
tm.assert_frame_equal(result, expected)
expected = df.copy()
expected['A'] = [1.0, 2, 3, 3, 2]
result = df.rolling('2s', closed='both').sum()
tm.assert_frame_equal(result, expected)
expected = df.copy()
expected['A'] = [np.nan, 1.0, 2, 2, 1]
result = df.rolling('2s', closed='left').sum()
tm.assert_frame_equal(result, expected)
expected = df.copy()
expected['A'] = [np.nan, 1.0, 1, 1, np.nan]
result = df.rolling('2s', closed='neither').sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timeseries_window.py:255 | Complexity: Advanced | Last updated: 2026-06-02*