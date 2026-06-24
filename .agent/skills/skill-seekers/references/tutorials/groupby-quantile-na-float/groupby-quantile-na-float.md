# How To: Groupby Quantile Na Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby quantile NA float

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
# Fixtures: any_float_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 1], 'y': [0.2, np.nan]}, dtype=any_float_dtype)
```

### Step 2: Assign result = unknown.quantile(...)

```python
result = df.groupby('x')['y'].quantile(0.5)
```

### Step 3: Assign exp_index = Index(...)

```python
exp_index = Index([1.0], dtype=any_float_dtype, name='x')
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([0.2], dtype=expected_dtype, index=exp_index, name='y')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = unknown.quantile(...)

```python
result = df.groupby('x')['y'].quantile([0.5, 0.75])
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series([0.2] * 2, index=pd.MultiIndex.from_product((exp_index, [0.5, 0.75]), names=['x', None]), name='y', dtype=expected_dtype)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign expected_dtype = any_float_dtype

```python
expected_dtype = any_float_dtype
```

### Step 10: Assign expected_dtype = None

```python
expected_dtype = None
```


## Complete Example

```python
# Setup
# Fixtures: any_float_dtype

# Workflow
df = DataFrame({'x': [1, 1], 'y': [0.2, np.nan]}, dtype=any_float_dtype)
result = df.groupby('x')['y'].quantile(0.5)
exp_index = Index([1.0], dtype=any_float_dtype, name='x')
if any_float_dtype in ['Float32', 'Float64']:
    expected_dtype = any_float_dtype
else:
    expected_dtype = None
expected = pd.Series([0.2], dtype=expected_dtype, index=exp_index, name='y')
tm.assert_series_equal(result, expected)
result = df.groupby('x')['y'].quantile([0.5, 0.75])
expected = pd.Series([0.2] * 2, index=pd.MultiIndex.from_product((exp_index, [0.5, 0.75]), names=['x', None]), name='y', dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:268 | Complexity: Advanced | Last updated: 2026-06-02*