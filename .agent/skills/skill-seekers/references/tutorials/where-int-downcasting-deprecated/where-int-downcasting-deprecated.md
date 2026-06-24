# How To: Where Int Downcasting Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where int downcasting deprecated

## Prerequisites

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas._testing._hypothesis`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.astype.reshape(...)

```python
arr = np.arange(6).astype(np.int16).reshape(3, 2)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr)
```

### Step 3: Assign mask = np.zeros(...)

```python
mask = np.zeros(arr.shape, dtype=bool)
```

### Step 4: Assign unknown = True

```python
mask[:, 0] = True
```

### Step 5: Assign res = df.where(...)

```python
res = df.where(mask, 2 ** 17)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: arr[:, 0], 1: np.array([2 ** 17] * 3, dtype=np.int32)})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(6).astype(np.int16).reshape(3, 2)
df = DataFrame(arr)
mask = np.zeros(arr.shape, dtype=bool)
mask[:, 0] = True
res = df.where(mask, 2 ** 17)
expected = DataFrame({0: arr[:, 0], 1: np.array([2 ** 17] * 3, dtype=np.int32)})
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_where.py:814 | Complexity: Intermediate | Last updated: 2026-06-02*