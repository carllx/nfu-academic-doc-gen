# How To: To Numpy String

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy string

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: box, dtype
```

## Step-by-Step Guide

### Step 1: Assign con = value

```python
con = pd.Series if box else pd.array
```

### Step 2: Assign arr = con(...)

```python
arr = con([0.0, 1.0, None], dtype='Float64')
```

### Step 3: Assign result = arr.to_numpy(...)

```python
result = arr.to_numpy(dtype='str')
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([0.0, 1.0, pd.NA], dtype=f'{tm.ENDIAN}U32')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box, dtype

# Workflow
con = pd.Series if box else pd.array
arr = con([0.0, 1.0, None], dtype='Float64')
result = arr.to_numpy(dtype='str')
expected = np.array([0.0, 1.0, pd.NA], dtype=f'{tm.ENDIAN}U32')
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numpy.py:113 | Complexity: Intermediate | Last updated: 2026-06-02*