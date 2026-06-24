# How To: Transpose Uint64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transpose uint64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': np.arange(3), 'B': [2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10]}, dtype=np.uint64)
```

### Step 2: Assign result = value

```python
result = df.T
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame(df.values.T)
```

### Step 4: Assign expected.index = value

```python
expected.index = ['A', 'B']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': np.arange(3), 'B': [2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10]}, dtype=np.uint64)
result = df.T
expected = DataFrame(df.values.T)
expected.index = ['A', 'B']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_transpose.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*