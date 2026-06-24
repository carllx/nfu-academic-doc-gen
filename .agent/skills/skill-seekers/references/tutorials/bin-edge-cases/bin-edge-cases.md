# How To: Bin Edge Cases

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bin edge cases

## Prerequisites

**Required Modules:**
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([337, 404, 739, 806, 1007, 1811, 2012])
```

**Verification:**
```python
assert_(x >= left)
```

### Step 2: Assign unknown = np.histogram(...)

```python
hist, edges = np.histogram(arr, bins=8296, range=(2, 2280))
```

**Verification:**
```python
assert_(x < right)
```

### Step 3: Assign mask = value

```python
mask = hist > 0
```

### Step 4: Assign left_edges = value

```python
left_edges = edges[:-1][mask]
```

### Step 5: Assign right_edges = value

```python
right_edges = edges[1:][mask]
```

### Step 6: Call assert_()

```python
assert_(x >= left)
```

### Step 7: Call assert_()

```python
assert_(x < right)
```


## Complete Example

```python
# Workflow
arr = np.array([337, 404, 739, 806, 1007, 1811, 2012])
hist, edges = np.histogram(arr, bins=8296, range=(2, 2280))
mask = hist > 0
left_edges = edges[:-1][mask]
right_edges = edges[1:][mask]
for x, left, right in zip(arr, left_edges, right_edges):
    assert_(x >= left)
    assert_(x < right)
```

## Next Steps


---

*Source: test_histograms.py:238 | Complexity: Intermediate | Last updated: 2026-06-02*