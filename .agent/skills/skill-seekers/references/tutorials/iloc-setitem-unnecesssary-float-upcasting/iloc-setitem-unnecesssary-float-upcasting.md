# How To: Iloc Setitem Unnecesssary Float Upcasting

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc setitem unnecesssary float upcasting

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({0: np.array([1, 3], dtype=np.float32), 1: np.array([2, 4], dtype=np.float32), 2: ['a', 'b']})
```

### Step 2: Assign orig = df.copy(...)

```python
orig = df.copy()
```

### Step 3: Assign values = unknown.values.reshape(...)

```python
values = df[0].values.reshape(2, 1)
```

### Step 4: Assign unknown = values

```python
df.iloc[:, 0:1] = values
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, orig)
```


## Complete Example

```python
# Workflow
df = DataFrame({0: np.array([1, 3], dtype=np.float32), 1: np.array([2, 4], dtype=np.float32), 2: ['a', 'b']})
orig = df.copy()
values = df[0].values.reshape(2, 1)
df.iloc[:, 0:1] = values
tm.assert_frame_equal(df, orig)
```

## Next Steps


---

*Source: test_coercion.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*