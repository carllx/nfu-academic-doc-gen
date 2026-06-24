# How To: Quantile Array No Sort

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile array no sort

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
df = DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
```

### Step 2: Assign key = np.array(...)

```python
key = np.array([1, 0, 1], dtype=np.int64)
```

### Step 3: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(key, sort=False).quantile([0.25, 0.5, 0.75])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0.5, 1.0, 1.5, 1.0, 1.0, 1.0], 'B': [3.5, 4.0, 4.5, 4.0, 4.0, 4.0]}, index=pd.MultiIndex.from_product([[1, 0], [0.25, 0.5, 0.75]]))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(key, sort=False).quantile([0.75, 0.25])
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1.5, 0.5, 1.0, 1.0], 'B': [4.5, 3.5, 4.0, 4.0]}, index=pd.MultiIndex.from_product([[1, 0], [0.75, 0.25]]))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
key = np.array([1, 0, 1], dtype=np.int64)
result = df.groupby(key, sort=False).quantile([0.25, 0.5, 0.75])
expected = DataFrame({'A': [0.5, 1.0, 1.5, 1.0, 1.0, 1.0], 'B': [3.5, 4.0, 4.5, 4.0, 4.0, 4.0]}, index=pd.MultiIndex.from_product([[1, 0], [0.25, 0.5, 0.75]]))
tm.assert_frame_equal(result, expected)
result = df.groupby(key, sort=False).quantile([0.75, 0.25])
expected = DataFrame({'A': [1.5, 0.5, 1.0, 1.0], 'B': [4.5, 3.5, 4.0, 4.0]}, index=pd.MultiIndex.from_product([[1, 0], [0.75, 0.25]]))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:111 | Complexity: Advanced | Last updated: 2026-06-02*