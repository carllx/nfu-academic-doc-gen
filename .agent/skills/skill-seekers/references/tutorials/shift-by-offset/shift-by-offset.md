# How To: Shift By Offset

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift by offset

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_frame, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = tm.get_obj(...)

```python
obj = tm.get_obj(datetime_frame, frame_or_series)
```

**Verification:**
```python
assert len(shifted) == len(obj)
```

### Step 2: Assign offset = offsets.BDay(...)

```python
offset = offsets.BDay()
```

### Step 3: Assign shifted = obj.shift(...)

```python
shifted = obj.shift(5, freq=offset)
```

**Verification:**
```python
assert len(shifted) == len(obj)
```

### Step 4: Assign unshifted = shifted.shift(...)

```python
unshifted = shifted.shift(-5, freq=offset)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(unshifted, obj)
```

### Step 6: Assign shifted2 = obj.shift(...)

```python
shifted2 = obj.shift(5, freq='B')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(shifted, shifted2)
```

### Step 8: Assign unshifted = obj.shift(...)

```python
unshifted = obj.shift(0, freq=offset)
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(unshifted, obj)
```

### Step 10: Assign d = value

```python
d = obj.index[0]
```

### Step 11: Assign shifted_d = value

```python
shifted_d = d + offset * 5
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(obj.xs(d), shifted.xs(shifted_d), check_names=False)
```

### Step 13: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(obj.at[d], shifted.at[shifted_d])
```


## Complete Example

```python
# Setup
# Fixtures: datetime_frame, frame_or_series

# Workflow
obj = tm.get_obj(datetime_frame, frame_or_series)
offset = offsets.BDay()
shifted = obj.shift(5, freq=offset)
assert len(shifted) == len(obj)
unshifted = shifted.shift(-5, freq=offset)
tm.assert_equal(unshifted, obj)
shifted2 = obj.shift(5, freq='B')
tm.assert_equal(shifted, shifted2)
unshifted = obj.shift(0, freq=offset)
tm.assert_equal(unshifted, obj)
d = obj.index[0]
shifted_d = d + offset * 5
if frame_or_series is DataFrame:
    tm.assert_series_equal(obj.xs(d), shifted.xs(shifted_d), check_names=False)
else:
    tm.assert_almost_equal(obj.at[d], shifted.at[shifted_d])
```

## Next Steps


---

*Source: test_shift.py:219 | Complexity: Advanced | Last updated: 2026-06-02*