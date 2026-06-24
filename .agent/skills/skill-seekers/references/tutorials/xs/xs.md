# How To: Xs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: float_frame, datetime_frame, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign float_frame_orig = float_frame.copy(...)

```python
float_frame_orig = float_frame.copy()
```

**Verification:**
```python
assert np.isnan(float_frame[item][idx])
```

### Step 2: Assign idx = value

```python
idx = float_frame.index[5]
```

**Verification:**
```python
assert value == float_frame[item][idx]
```

### Step 3: Assign xs = float_frame.xs(...)

```python
xs = float_frame.xs(idx)
```

**Verification:**
```python
assert xs.dtype == np.object_
```

### Step 4: Assign test_data = value

```python
test_data = {'A': {'1': 1, '2': 2}, 'B': {'1': '1', '2': '2', '3': '3'}}
```

**Verification:**
```python
assert xs['A'] == 1
```

### Step 5: Assign frame = DataFrame(...)

```python
frame = DataFrame(test_data)
```

**Verification:**
```python
assert xs['B'] == '1'
```

### Step 6: Assign xs = frame.xs(...)

```python
xs = frame.xs('1')
```

**Verification:**
```python
assert not (expected == 5).all()
```

### Step 7: Assign series = float_frame.xs(...)

```python
series = float_frame.xs('A', axis=1)
```

**Verification:**
```python
assert (expected == 5).all()
```

### Step 8: Assign expected = value

```python
expected = float_frame['A']
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(series, expected)
```

### Step 10: Assign series = float_frame.xs(...)

```python
series = float_frame.xs('A', axis=1)
```

### Step 11: Call datetime_frame.xs()

```python
datetime_frame.xs(datetime_frame.index[0] - BDay())
```

### Step 12: Assign unknown = 5

```python
series[:] = 5
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(float_frame['A'], float_frame_orig['A'])
```

**Verification:**
```python
assert not (expected == 5).all()
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, datetime_frame, using_copy_on_write, warn_copy_on_write

# Workflow
float_frame_orig = float_frame.copy()
idx = float_frame.index[5]
xs = float_frame.xs(idx)
for item, value in xs.items():
    if np.isnan(value):
        assert np.isnan(float_frame[item][idx])
    else:
        assert value == float_frame[item][idx]
test_data = {'A': {'1': 1, '2': 2}, 'B': {'1': '1', '2': '2', '3': '3'}}
frame = DataFrame(test_data)
xs = frame.xs('1')
assert xs.dtype == np.object_
assert xs['A'] == 1
assert xs['B'] == '1'
with pytest.raises(KeyError, match=re.escape("Timestamp('1999-12-31 00:00:00')")):
    datetime_frame.xs(datetime_frame.index[0] - BDay())
series = float_frame.xs('A', axis=1)
expected = float_frame['A']
tm.assert_series_equal(series, expected)
series = float_frame.xs('A', axis=1)
with tm.assert_cow_warning(warn_copy_on_write):
    series[:] = 5
if using_copy_on_write:
    tm.assert_series_equal(float_frame['A'], float_frame_orig['A'])
    assert not (expected == 5).all()
else:
    assert (expected == 5).all()
```

## Next Steps


---

*Source: test_xs.py:39 | Complexity: Advanced | Last updated: 2026-06-02*