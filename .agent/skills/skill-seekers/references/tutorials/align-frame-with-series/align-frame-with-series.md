# How To: Align Frame With Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align frame with series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign idx = value

```python
idx = float_frame.index
```

**Verification:**
```python
assert isinstance(right, Series)
```

### Step 2: Assign s = Series(...)

```python
s = Series(range(len(idx)), index=idx)
```

### Step 3: Assign unknown = float_frame.align(...)

```python
left, right = float_frame.align(s, axis=0)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(left.index, float_frame.index)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(right.index, float_frame.index)
```

**Verification:**
```python
assert isinstance(right, Series)
```

### Step 6: Assign msg = "The 'broadcast_axis' keyword in DataFrame.align is deprecated"

```python
msg = "The 'broadcast_axis' keyword in DataFrame.align is deprecated"
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(left.index, float_frame.index)
```

### Step 8: Assign expected = value

```python
expected = {c: s for c in float_frame.columns}
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected, index=float_frame.index, columns=float_frame.columns)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(right, expected)
```

### Step 11: Assign unknown = float_frame.align(...)

```python
left, right = float_frame.align(s, broadcast_axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
idx = float_frame.index
s = Series(range(len(idx)), index=idx)
left, right = float_frame.align(s, axis=0)
tm.assert_index_equal(left.index, float_frame.index)
tm.assert_index_equal(right.index, float_frame.index)
assert isinstance(right, Series)
msg = "The 'broadcast_axis' keyword in DataFrame.align is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    left, right = float_frame.align(s, broadcast_axis=1)
tm.assert_index_equal(left.index, float_frame.index)
expected = {c: s for c in float_frame.columns}
expected = DataFrame(expected, index=float_frame.index, columns=float_frame.columns)
tm.assert_frame_equal(right, expected)
```

## Next Steps


---

*Source: test_align.py:127 | Complexity: Advanced | Last updated: 2026-06-02*