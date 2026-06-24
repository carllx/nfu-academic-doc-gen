# How To: Isna Lists

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isna lists

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = isna(...)

```python
result = isna([[False]])
```

### Step 2: Assign exp = np.array(...)

```python
exp = np.array([[False]])
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```

### Step 4: Assign result = isna(...)

```python
result = isna([[1], [2]])
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([[False], [False]])
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```

### Step 7: Assign result = isna(...)

```python
result = isna(['foo', 'bar'])
```

### Step 8: Assign exp = np.array(...)

```python
exp = np.array([False, False])
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```

### Step 10: Assign result = isna(...)

```python
result = isna(['foo', 'bar'])
```

### Step 11: Assign exp = np.array(...)

```python
exp = np.array([False, False])
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```

### Step 13: Assign result = isna(...)

```python
result = isna([np.nan, 'world'])
```

### Step 14: Assign exp = np.array(...)

```python
exp = np.array([True, False])
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```


## Complete Example

```python
# Workflow
result = isna([[False]])
exp = np.array([[False]])
tm.assert_numpy_array_equal(result, exp)
result = isna([[1], [2]])
exp = np.array([[False], [False]])
tm.assert_numpy_array_equal(result, exp)
result = isna(['foo', 'bar'])
exp = np.array([False, False])
tm.assert_numpy_array_equal(result, exp)
result = isna(['foo', 'bar'])
exp = np.array([False, False])
tm.assert_numpy_array_equal(result, exp)
result = isna([np.nan, 'world'])
exp = np.array([True, False])
tm.assert_numpy_array_equal(result, exp)
```

## Next Steps


---

*Source: test_missing.py:153 | Complexity: Advanced | Last updated: 2026-06-02*