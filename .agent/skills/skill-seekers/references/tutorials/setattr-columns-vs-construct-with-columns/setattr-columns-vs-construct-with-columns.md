# How To: Setattr Columns Vs Construct With Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setattr columns vs construct with columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((3, 2))
```

### Step 2: Assign idx = list(...)

```python
idx = list(range(2))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=['A', 'A'])
```

### Step 4: Assign df.columns = idx

```python
df.columns = idx
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(arr, columns=idx)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((3, 2))
idx = list(range(2))
df = DataFrame(arr, columns=['A', 'A'])
df.columns = idx
expected = DataFrame(arr, columns=idx)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*