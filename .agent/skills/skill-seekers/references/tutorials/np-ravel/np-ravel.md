# How To: Np Ravel

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test np ravel

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([[0.11197053, 0.44361564, -0.92589452], [0.05883648, -0.00948922, -0.26469934]])
```

### Step 2: Assign result = np.ravel(...)

```python
result = np.ravel([DataFrame(batch.reshape(1, 3)) for batch in arr])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([0.11197053, 0.44361564, -0.92589452, 0.05883648, -0.00948922, -0.26469934])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = np.ravel(...)

```python
result = np.ravel(DataFrame(arr[0].reshape(1, 3), columns=['x1', 'x2', 'x3']))
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([0.11197053, 0.44361564, -0.92589452])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = np.ravel(...)

```python
result = np.ravel([DataFrame(batch.reshape(1, 3), columns=['x1', 'x2', 'x3']) for batch in arr])
```

### Step 9: Assign expected = np.array(...)

```python
expected = np.array([0.11197053, 0.44361564, -0.92589452, 0.05883648, -0.00948922, -0.26469934])
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.array([[0.11197053, 0.44361564, -0.92589452], [0.05883648, -0.00948922, -0.26469934]])
result = np.ravel([DataFrame(batch.reshape(1, 3)) for batch in arr])
expected = np.array([0.11197053, 0.44361564, -0.92589452, 0.05883648, -0.00948922, -0.26469934])
tm.assert_numpy_array_equal(result, expected)
result = np.ravel(DataFrame(arr[0].reshape(1, 3), columns=['x1', 'x2', 'x3']))
expected = np.array([0.11197053, 0.44361564, -0.92589452])
tm.assert_numpy_array_equal(result, expected)
result = np.ravel([DataFrame(batch.reshape(1, 3), columns=['x1', 'x2', 'x3']) for batch in arr])
expected = np.array([0.11197053, 0.44361564, -0.92589452, 0.05883648, -0.00948922, -0.26469934])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_npfuncs.py:47 | Complexity: Advanced | Last updated: 2026-06-02*