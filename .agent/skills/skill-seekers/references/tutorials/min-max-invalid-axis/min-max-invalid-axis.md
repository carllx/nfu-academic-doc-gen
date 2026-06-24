# How To: Min Max Invalid Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min max invalid axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: left_right_dtypes
```

## Step-by-Step Guide

### Step 1: Assign unknown = left_right_dtypes

```python
left, right = left_right_dtypes
```

### Step 2: Assign left = left.copy(...)

```python
left = left.copy(deep=True)
```

### Step 3: Assign right = right.copy(...)

```python
right = right.copy(deep=True)
```

### Step 4: Assign arr = IntervalArray.from_arrays(...)

```python
arr = IntervalArray.from_arrays(left, right)
```

### Step 5: Assign msg = '`axis` must be fewer than the number of dimensions'

```python
msg = '`axis` must be fewer than the number of dimensions'
```

### Step 6: Assign msg = "'>=' not supported between"

```python
msg = "'>=' not supported between"
```

### Step 7: Call arr.min()

```python
arr.min(axis='foo')
```

### Step 8: Call arr.max()

```python
arr.max(axis='foo')
```

### Step 9: Call arr.min()

```python
arr.min(axis=axis)
```

### Step 10: Call arr.max()

```python
arr.max(axis=axis)
```


## Complete Example

```python
# Setup
# Fixtures: left_right_dtypes

# Workflow
left, right = left_right_dtypes
left = left.copy(deep=True)
right = right.copy(deep=True)
arr = IntervalArray.from_arrays(left, right)
msg = '`axis` must be fewer than the number of dimensions'
for axis in [-2, 1]:
    with pytest.raises(ValueError, match=msg):
        arr.min(axis=axis)
    with pytest.raises(ValueError, match=msg):
        arr.max(axis=axis)
msg = "'>=' not supported between"
with pytest.raises(TypeError, match=msg):
    arr.min(axis='foo')
with pytest.raises(TypeError, match=msg):
    arr.max(axis='foo')
```

## Next Steps


---

*Source: test_interval.py:170 | Complexity: Advanced | Last updated: 2026-06-02*