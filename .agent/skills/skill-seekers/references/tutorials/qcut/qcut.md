# How To: Qcut

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test qcut

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal(1000)
```

**Verification:**
```python
assert np.allclose(result, ex_bins[:-1], atol=0.01)
```

### Step 2: Assign unknown = qcut(...)

```python
labels, _ = qcut(arr, 4, retbins=True)
```

**Verification:**
```python
assert np.allclose(result, ex_bins[1:], atol=0.01)
```

### Step 3: Assign ex_bins = np.quantile(...)

```python
ex_bins = np.quantile(arr, [0, 0.25, 0.5, 0.75, 1.0])
```

### Step 4: Assign result = value

```python
result = labels.categories.left.values
```

**Verification:**
```python
assert np.allclose(result, ex_bins[:-1], atol=0.01)
```

### Step 5: Assign result = value

```python
result = labels.categories.right.values
```

**Verification:**
```python
assert np.allclose(result, ex_bins[1:], atol=0.01)
```

### Step 6: Assign ex_levels = cut(...)

```python
ex_levels = cut(arr, ex_bins, include_lowest=True)
```

### Step 7: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(labels, ex_levels)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal(1000)
labels, _ = qcut(arr, 4, retbins=True)
ex_bins = np.quantile(arr, [0, 0.25, 0.5, 0.75, 1.0])
result = labels.categories.left.values
assert np.allclose(result, ex_bins[:-1], atol=0.01)
result = labels.categories.right.values
assert np.allclose(result, ex_bins[1:], atol=0.01)
ex_levels = cut(arr, ex_bins, include_lowest=True)
tm.assert_categorical_equal(labels, ex_levels)
```

## Next Steps


---

*Source: test_qcut.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*