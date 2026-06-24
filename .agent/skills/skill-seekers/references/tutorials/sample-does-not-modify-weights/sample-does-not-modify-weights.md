# How To: Sample Does Not Modify Weights

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sample does not modify weights

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign result = np.array(...)

```python
result = np.array([np.nan, 1, np.nan])
```

### Step 2: Assign expected = result.copy(...)

```python
expected = result.copy()
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([1, 2, 3])
```

### Step 4: Call ser.sample()

```python
ser.sample(weights=result)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'values': [1, 1, 1], 'weights': [1, np.nan, np.nan]})
```

### Step 7: Assign expected = unknown.copy(...)

```python
expected = df['weights'].copy()
```

### Step 8: Call df.sample()

```python
df.sample(frac=1.0, replace=True, weights='weights')
```

### Step 9: Assign result = value

```python
result = df['weights']
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
result = np.array([np.nan, 1, np.nan])
expected = result.copy()
ser = Series([1, 2, 3])
ser.sample(weights=result)
tm.assert_numpy_array_equal(result, expected)
df = DataFrame({'values': [1, 1, 1], 'weights': [1, np.nan, np.nan]})
expected = df['weights'].copy()
df.sample(frac=1.0, replace=True, weights='weights')
result = df['weights']
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_sample.py:347 | Complexity: Advanced | Last updated: 2026-06-02*