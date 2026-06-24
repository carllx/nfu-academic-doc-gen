# How To: Invert Mixed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invert mixed

## Prerequisites

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign shape = value

```python
shape = (10, 5)
```

### Step 2: Assign df = pd.concat(...)

```python
df = pd.concat([pd.DataFrame(np.zeros(shape, dtype='bool')), pd.DataFrame(np.zeros(shape, dtype=int))], axis=1, ignore_index=True)
```

### Step 3: Assign result = value

```python
result = ~df
```

### Step 4: Assign expected = pd.concat(...)

```python
expected = pd.concat([pd.DataFrame(np.ones(shape, dtype='bool')), pd.DataFrame(-np.ones(shape, dtype=int))], axis=1, ignore_index=True)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
shape = (10, 5)
df = pd.concat([pd.DataFrame(np.zeros(shape, dtype='bool')), pd.DataFrame(np.zeros(shape, dtype=int))], axis=1, ignore_index=True)
result = ~df
expected = pd.concat([pd.DataFrame(np.ones(shape, dtype='bool')), pd.DataFrame(-np.ones(shape, dtype=int))], axis=1, ignore_index=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_unary.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*