# How To: Expanding Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test expanding axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: axis_frame
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((10, 20)))
```

### Step 2: Assign axis = df._get_axis_number(...)

```python
axis = df._get_axis_number(axis_frame)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign msg = "The 'axis' keyword in DataFrame.expanding is deprecated"

```python
msg = "The 'axis' keyword in DataFrame.expanding is deprecated"
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({i: [np.nan] * 2 + [float(j) for j in range(3, 11)] for i in range(20)})
```

### Step 6: Assign msg = 'Support for axis=1 in DataFrame.expanding is deprecated'

```python
msg = 'Support for axis=1 in DataFrame.expanding is deprecated'
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[np.nan] * 2 + [float(i) for i in range(3, 21)]] * 10)
```

### Step 8: Assign result = df.expanding.sum(...)

```python
result = df.expanding(3, axis=axis_frame).sum()
```


## Complete Example

```python
# Setup
# Fixtures: axis_frame

# Workflow
df = DataFrame(np.ones((10, 20)))
axis = df._get_axis_number(axis_frame)
if axis == 0:
    msg = "The 'axis' keyword in DataFrame.expanding is deprecated"
    expected = DataFrame({i: [np.nan] * 2 + [float(j) for j in range(3, 11)] for i in range(20)})
else:
    msg = 'Support for axis=1 in DataFrame.expanding is deprecated'
    expected = DataFrame([[np.nan] * 2 + [float(i) for i in range(3, 21)]] * 10)
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.expanding(3, axis=axis_frame).sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:82 | Complexity: Advanced | Last updated: 2026-06-02*