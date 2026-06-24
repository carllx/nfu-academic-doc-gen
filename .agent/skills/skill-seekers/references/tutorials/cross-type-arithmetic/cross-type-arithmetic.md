# How To: Cross Type Arithmetic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cross type arithmetic

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'A': pd.array([1, 2, np.nan], dtype='Float64'), 'B': pd.array([1, np.nan, 3], dtype='Float32'), 'C': np.array([1, 2, 3], dtype='float64')})
```

### Step 2: Assign result = value

```python
result = df.A + df.C
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([2, 4, np.nan], dtype='Float64')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = (df.A + df.C) * 3 == 12
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series([False, True, None], dtype='boolean')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.A + df.B
```

### Step 9: Assign expected = pd.Series(...)

```python
expected = pd.Series([2, np.nan, np.nan], dtype='Float64')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'A': pd.array([1, 2, np.nan], dtype='Float64'), 'B': pd.array([1, np.nan, 3], dtype='Float32'), 'C': np.array([1, 2, 3], dtype='float64')})
result = df.A + df.C
expected = pd.Series([2, 4, np.nan], dtype='Float64')
tm.assert_series_equal(result, expected)
result = (df.A + df.C) * 3 == 12
expected = pd.Series([False, True, None], dtype='boolean')
tm.assert_series_equal(result, expected)
result = df.A + df.B
expected = pd.Series([2, np.nan, np.nan], dtype='Float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:187 | Complexity: Advanced | Last updated: 2026-06-02*