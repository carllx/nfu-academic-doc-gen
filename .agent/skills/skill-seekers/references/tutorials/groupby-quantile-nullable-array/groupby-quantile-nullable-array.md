# How To: Groupby Quantile Nullable Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby quantile nullable array

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values, q
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['x'] * 3 + ['y'] * 3, 'b': values})
```

### Step 2: Assign result = unknown.quantile(...)

```python
result = df.groupby('a')['b'].quantile(q)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series(true_quantiles * 2, index=idx, name='b', dtype='Float64')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign idx = pd.MultiIndex.from_product(...)

```python
idx = pd.MultiIndex.from_product((['x', 'y'], q), names=['a', None])
```

### Step 6: Assign true_quantiles = value

```python
true_quantiles = [0.0, 0.5, 1.0]
```

### Step 7: Assign idx = Index(...)

```python
idx = Index(['x', 'y'], name='a')
```

### Step 8: Assign true_quantiles = value

```python
true_quantiles = [0.5]
```


## Complete Example

```python
# Setup
# Fixtures: values, q

# Workflow
df = DataFrame({'a': ['x'] * 3 + ['y'] * 3, 'b': values})
result = df.groupby('a')['b'].quantile(q)
if isinstance(q, list):
    idx = pd.MultiIndex.from_product((['x', 'y'], q), names=['a', None])
    true_quantiles = [0.0, 0.5, 1.0]
else:
    idx = Index(['x', 'y'], name='a')
    true_quantiles = [0.5]
expected = pd.Series(true_quantiles * 2, index=idx, name='b', dtype='Float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:238 | Complexity: Advanced | Last updated: 2026-06-02*