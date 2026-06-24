# How To: Quantile Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile array

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
df = DataFrame({'A': [0, 1, 2, 3, 4]})
```

### Step 2: Assign key = np.array(...)

```python
key = np.array([0, 0, 1, 1, 1], dtype=np.int64)
```

### Step 3: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(key).quantile([0.25])
```

### Step 4: Assign index = pd.MultiIndex.from_product(...)

```python
index = pd.MultiIndex.from_product([[0, 1], [0.25]])
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0.25, 2.5]}, index=index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 2, 3], 'B': [4, 5, 6, 7]})
```

### Step 8: Assign index = pd.MultiIndex.from_product(...)

```python
index = pd.MultiIndex.from_product([[0, 1], [0.25, 0.75]])
```

### Step 9: Assign key = np.array(...)

```python
key = np.array([0, 0, 1, 1], dtype=np.int64)
```

### Step 10: Assign result = df.groupby.quantile(...)

```python
result = df.groupby(key).quantile([0.25, 0.75])
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0.25, 0.75, 2.25, 2.75], 'B': [4.25, 4.75, 6.25, 6.75]}, index=index)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [0, 1, 2, 3, 4]})
key = np.array([0, 0, 1, 1, 1], dtype=np.int64)
result = df.groupby(key).quantile([0.25])
index = pd.MultiIndex.from_product([[0, 1], [0.25]])
expected = DataFrame({'A': [0.25, 2.5]}, index=index)
tm.assert_frame_equal(result, expected)
df = DataFrame({'A': [0, 1, 2, 3], 'B': [4, 5, 6, 7]})
index = pd.MultiIndex.from_product([[0, 1], [0.25, 0.75]])
key = np.array([0, 0, 1, 1], dtype=np.int64)
result = df.groupby(key).quantile([0.25, 0.75])
expected = DataFrame({'A': [0.25, 0.75, 2.25, 2.75], 'B': [4.25, 4.75, 6.25, 6.75]}, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:73 | Complexity: Advanced | Last updated: 2026-06-02*