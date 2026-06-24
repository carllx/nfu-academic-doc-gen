# How To: Expanding Func

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test expanding func

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func, static_comp, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign data = frame_or_series(...)

```python
data = frame_or_series(np.array(list(range(10)) + [np.nan] * 10))
```

**Verification:**
```python
assert isinstance(result, frame_or_series)
```

### Step 2: Assign msg = "The 'axis' keyword in (Series|DataFrame).expanding is deprecated"

```python
msg = "The 'axis' keyword in (Series|DataFrame).expanding is deprecated"
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(obj, func)()
```

**Verification:**
```python
assert isinstance(result, frame_or_series)
```

### Step 4: Assign msg = 'The behavior of DataFrame.sum with axis=None is deprecated'

```python
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
```

### Step 5: Assign warn = None

```python
warn = None
```

### Step 6: Assign obj = data.expanding(...)

```python
obj = data.expanding(min_periods=1, axis=0)
```

### Step 7: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 8: Assign expected = static_comp(...)

```python
expected = static_comp(data[:11])
```

### Step 9: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result[10], expected)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result.iloc[10], expected, check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: func, static_comp, frame_or_series

# Workflow
data = frame_or_series(np.array(list(range(10)) + [np.nan] * 10))
msg = "The 'axis' keyword in (Series|DataFrame).expanding is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    obj = data.expanding(min_periods=1, axis=0)
result = getattr(obj, func)()
assert isinstance(result, frame_or_series)
msg = 'The behavior of DataFrame.sum with axis=None is deprecated'
warn = None
if frame_or_series is DataFrame and static_comp is np.sum:
    warn = FutureWarning
with tm.assert_produces_warning(warn, match=msg, check_stacklevel=False):
    expected = static_comp(data[:11])
if frame_or_series is Series:
    tm.assert_almost_equal(result[10], expected)
else:
    tm.assert_series_equal(result.iloc[10], expected, check_names=False)
```

## Next Steps


---

*Source: test_expanding.py:329 | Complexity: Advanced | Last updated: 2026-06-02*