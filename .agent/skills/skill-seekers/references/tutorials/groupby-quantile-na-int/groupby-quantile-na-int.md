# How To: Groupby Quantile Na Int

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby quantile NA int

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
# Fixtures: any_int_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [1, 1], 'y': [2, 5]}, dtype=any_int_ea_dtype)
```

### Step 2: Assign result = unknown.quantile(...)

```python
result = df.groupby('x')['y'].quantile(0.5)
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([3.5], dtype='Float64', index=Index([1], name='x', dtype=any_int_ea_dtype), name='y')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```

### Step 5: Assign result = df.groupby.quantile(...)

```python
result = df.groupby('x').quantile(0.5)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'y': 3.5}, dtype='Float64', index=Index([1], name='x', dtype=any_int_ea_dtype))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_int_ea_dtype

# Workflow
df = DataFrame({'x': [1, 1], 'y': [2, 5]}, dtype=any_int_ea_dtype)
result = df.groupby('x')['y'].quantile(0.5)
expected = pd.Series([3.5], dtype='Float64', index=Index([1], name='x', dtype=any_int_ea_dtype), name='y')
tm.assert_series_equal(expected, result)
result = df.groupby('x').quantile(0.5)
expected = DataFrame({'y': 3.5}, dtype='Float64', index=Index([1], name='x', dtype=any_int_ea_dtype))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:292 | Complexity: Intermediate | Last updated: 2026-06-02*