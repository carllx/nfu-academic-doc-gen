# How To: Quantile Interpolation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile interpolation

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
```

**Verification:**
```python
assert np.isnan(q['x']) and np.isnan(q['y'])
```

### Step 2: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=1, interpolation='nearest')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, 2, 3], index=[1, 2, 3], name=0.5)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign exp = np.percentile(...)

```python
exp = np.percentile(np.array([[1, 2, 3], [2, 3, 4]]), 0.5, axis=0, method='nearest')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype='int64')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1.0, 2.0, 3.0], 'B': [2.0, 3.0, 4.0]}, index=[1, 2, 3])
```

### Step 9: Assign result = df.quantile(...)

```python
result = df.quantile(0.5, axis=1, interpolation='nearest')
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([1.0, 2.0, 3.0], index=[1, 2, 3], name=0.5)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign exp = np.percentile(...)

```python
exp = np.percentile(np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0]]), 0.5, axis=0, method='nearest')
```

### Step 13: Assign expected = Series(...)

```python
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype='float64')
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Assign result = df.quantile(...)

```python
result = df.quantile([0.5, 0.75], axis=1, interpolation='lower')
```

### Step 16: Assign expected = DataFrame(...)

```python
expected = DataFrame({1: [1.0, 1.0], 2: [2.0, 2.0], 3: [3.0, 3.0]}, index=[0.5, 0.75])
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign df = DataFrame(...)

```python
df = DataFrame({'x': [], 'y': []})
```

### Step 19: Assign q = df.quantile(...)

```python
q = df.quantile(0.1, axis=0, interpolation='higher')
```

**Verification:**
```python
assert np.isnan(q['x']) and np.isnan(q['y'])
```

### Step 20: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=['a', 'b', 'c'])
```

### Step 21: Assign result = df.quantile(...)

```python
result = df.quantile([0.25, 0.5], interpolation='midpoint')
```

### Step 22: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.5, 1.5, 1.5], [2.0, 2.0, 2.0]], index=[0.25, 0.5], columns=['a', 'b', 'c'])
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation='nearest')
expected = Series([1, 2, 3], index=[1, 2, 3], name=0.5)
tm.assert_series_equal(result, expected)
exp = np.percentile(np.array([[1, 2, 3], [2, 3, 4]]), 0.5, axis=0, method='nearest')
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype='int64')
tm.assert_series_equal(result, expected)
df = DataFrame({'A': [1.0, 2.0, 3.0], 'B': [2.0, 3.0, 4.0]}, index=[1, 2, 3])
result = df.quantile(0.5, axis=1, interpolation='nearest')
expected = Series([1.0, 2.0, 3.0], index=[1, 2, 3], name=0.5)
tm.assert_series_equal(result, expected)
exp = np.percentile(np.array([[1.0, 2.0, 3.0], [2.0, 3.0, 4.0]]), 0.5, axis=0, method='nearest')
expected = Series(exp, index=[1, 2, 3], name=0.5, dtype='float64')
tm.assert_series_equal(result, expected)
result = df.quantile([0.5, 0.75], axis=1, interpolation='lower')
expected = DataFrame({1: [1.0, 1.0], 2: [2.0, 2.0], 3: [3.0, 3.0]}, index=[0.5, 0.75])
tm.assert_frame_equal(result, expected)
df = DataFrame({'x': [], 'y': []})
q = df.quantile(0.1, axis=0, interpolation='higher')
assert np.isnan(q['x']) and np.isnan(q['y'])
df = DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=['a', 'b', 'c'])
result = df.quantile([0.25, 0.5], interpolation='midpoint')
expected = DataFrame([[1.5, 1.5, 1.5], [2.0, 2.0, 2.0]], index=[0.25, 0.5], columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_quantile.py:239 | Complexity: Advanced | Last updated: 2026-06-02*