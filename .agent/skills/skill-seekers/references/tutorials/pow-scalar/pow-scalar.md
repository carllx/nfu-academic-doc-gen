# How To: Pow Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pow scalar

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([-1, 0, 1, None, 2], dtype='Int64')
```

### Step 2: Assign result = value

```python
result = a ** 0
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array([1, 1, 1, 1, 1], dtype='Int64')
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = a ** 1
```

### Step 6: Assign expected = pd.array(...)

```python
expected = pd.array([-1, 0, 1, None, 2], dtype='Int64')
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = a ** pd.NA
```

### Step 9: Assign expected = pd.array(...)

```python
expected = pd.array([None, None, 1, None, None], dtype='Int64')
```

### Step 10: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = a ** np.nan
```

### Step 12: Assign expected = FloatingArray(...)

```python
expected = FloatingArray(np.array([np.nan, np.nan, 1, np.nan, np.nan], dtype='float64'), np.array([False, False, False, True, False]))
```

### Step 13: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 14: Assign a = value

```python
a = a[1:]
```

### Step 15: Assign result = value

```python
result = 0 ** a
```

### Step 16: Assign expected = pd.array(...)

```python
expected = pd.array([1, 0, None, 0], dtype='Int64')
```

### Step 17: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 18: Assign result = value

```python
result = 1 ** a
```

### Step 19: Assign expected = pd.array(...)

```python
expected = pd.array([1, 1, 1, 1], dtype='Int64')
```

### Step 20: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 21: Assign result = value

```python
result = pd.NA ** a
```

### Step 22: Assign expected = pd.array(...)

```python
expected = pd.array([1, None, None, None], dtype='Int64')
```

### Step 23: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 24: Assign result = value

```python
result = np.nan ** a
```

### Step 25: Assign expected = FloatingArray(...)

```python
expected = FloatingArray(np.array([1, np.nan, np.nan, np.nan], dtype='float64'), np.array([False, False, True, False]))
```

### Step 26: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = pd.array([-1, 0, 1, None, 2], dtype='Int64')
result = a ** 0
expected = pd.array([1, 1, 1, 1, 1], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = a ** 1
expected = pd.array([-1, 0, 1, None, 2], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = a ** pd.NA
expected = pd.array([None, None, 1, None, None], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = a ** np.nan
expected = FloatingArray(np.array([np.nan, np.nan, 1, np.nan, np.nan], dtype='float64'), np.array([False, False, False, True, False]))
tm.assert_extension_array_equal(result, expected)
a = a[1:]
result = 0 ** a
expected = pd.array([1, 0, None, 0], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = 1 ** a
expected = pd.array([1, 1, 1, 1], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = pd.NA ** a
expected = pd.array([1, None, None, None], dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = np.nan ** a
expected = FloatingArray(np.array([1, np.nan, np.nan, np.nan], dtype='float64'), np.array([False, False, True, False]))
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:102 | Complexity: Advanced | Last updated: 2026-06-02*