# How To: Isin Read Only

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin read only

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3])
```

### Step 2: Call arr.setflags()

```python
arr.setflags(write=False)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([1, 2, 3])
```

### Step 4: Assign result = df.isin(...)

```python
result = df.isin(arr)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([True, True, True])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3])
arr.setflags(write=False)
df = DataFrame([1, 2, 3])
result = df.isin(arr)
expected = DataFrame([True, True, True])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:212 | Complexity: Intermediate | Last updated: 2026-06-02*