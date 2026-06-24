# How To: Truncate Out Of Bounds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate out of bounds

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign shape = value

```python
shape = [2000] + [1] * (frame_or_series._AXIS_LEN - 1)
```

### Step 2: Assign small = construct(...)

```python
small = construct(frame_or_series, shape, dtype='int8', value=1)
```

### Step 3: Call tm.assert_equal()

```python
tm.assert_equal(small.truncate(), small)
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(small.truncate(before=0, after=3000.0), small)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(small.truncate(before=-1, after=2000.0), small)
```

### Step 6: Assign shape = value

```python
shape = [2000000] + [1] * (frame_or_series._AXIS_LEN - 1)
```

### Step 7: Assign big = construct(...)

```python
big = construct(frame_or_series, shape, dtype='int8', value=1)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(big.truncate(), big)
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(big.truncate(before=0, after=3000000.0), big)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(big.truncate(before=-1, after=2000000.0), big)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
shape = [2000] + [1] * (frame_or_series._AXIS_LEN - 1)
small = construct(frame_or_series, shape, dtype='int8', value=1)
tm.assert_equal(small.truncate(), small)
tm.assert_equal(small.truncate(before=0, after=3000.0), small)
tm.assert_equal(small.truncate(before=-1, after=2000.0), small)
shape = [2000000] + [1] * (frame_or_series._AXIS_LEN - 1)
big = construct(frame_or_series, shape, dtype='int8', value=1)
tm.assert_equal(big.truncate(), big)
tm.assert_equal(big.truncate(before=0, after=3000000.0), big)
tm.assert_equal(big.truncate(before=-1, after=2000000.0), big)
```

## Next Steps


---

*Source: test_generic.py:280 | Complexity: Advanced | Last updated: 2026-06-02*