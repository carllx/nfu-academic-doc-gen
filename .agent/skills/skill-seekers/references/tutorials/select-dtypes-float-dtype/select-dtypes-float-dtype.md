# How To: Select Dtypes Float Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test select dtypes float dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: expected, float_dtypes
```

## Step-by-Step Guide

### Step 1: Assign dtype_dict = value

```python
dtype_dict = {'A': float, 'B': np.float64, 'C': np.float32}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(3), 'B': range(5, 8), 'C': range(10, 7, -1)})
```

### Step 3: Assign df = df.astype(...)

```python
df = df.astype(dtype_dict)
```

### Step 4: Assign result = df.select_dtypes(...)

```python
result = df.select_dtypes(include=float_dtypes)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: expected, float_dtypes

# Workflow
dtype_dict = {'A': float, 'B': np.float64, 'C': np.float32}
df = DataFrame({'A': range(3), 'B': range(5, 8), 'C': range(10, 7, -1)})
df = df.astype(dtype_dict)
result = df.select_dtypes(include=float_dtypes)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_select_dtypes.py:455 | Complexity: Intermediate | Last updated: 2026-06-02*