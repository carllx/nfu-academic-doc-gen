# How To: Comparison Dt64 Ndarray

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparison dt64 ndarray

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Timestamp(...)

```python
ts = Timestamp('2021-01-01')
```

### Step 2: Assign ts2 = Timestamp(...)

```python
ts2 = Timestamp('2019-04-05')
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([[ts.asm8, ts2.asm8]], dtype='M8[ns]')
```

### Step 4: Assign result = value

```python
result = ts == arr
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([[True, False]], dtype=bool)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = arr == ts
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = ts != arr
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```

### Step 11: Assign result = value

```python
result = arr != ts
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```

### Step 13: Assign result = value

```python
result = ts2 < arr
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 15: Assign result = value

```python
result = arr < ts2
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([[False, False]], dtype=bool))
```

### Step 17: Assign result = value

```python
result = ts2 <= arr
```

### Step 18: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))
```

### Step 19: Assign result = value

```python
result = arr <= ts2
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```

### Step 21: Assign result = value

```python
result = ts >= arr
```

### Step 22: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))
```

### Step 23: Assign result = value

```python
result = arr >= ts
```

### Step 24: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, np.array([[True, False]], dtype=bool))
```


## Complete Example

```python
# Workflow
ts = Timestamp('2021-01-01')
ts2 = Timestamp('2019-04-05')
arr = np.array([[ts.asm8, ts2.asm8]], dtype='M8[ns]')
result = ts == arr
expected = np.array([[True, False]], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
result = arr == ts
tm.assert_numpy_array_equal(result, expected)
result = ts != arr
tm.assert_numpy_array_equal(result, ~expected)
result = arr != ts
tm.assert_numpy_array_equal(result, ~expected)
result = ts2 < arr
tm.assert_numpy_array_equal(result, expected)
result = arr < ts2
tm.assert_numpy_array_equal(result, np.array([[False, False]], dtype=bool))
result = ts2 <= arr
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))
result = arr <= ts2
tm.assert_numpy_array_equal(result, ~expected)
result = ts >= arr
tm.assert_numpy_array_equal(result, np.array([[True, True]], dtype=bool))
result = arr >= ts
tm.assert_numpy_array_equal(result, np.array([[True, False]], dtype=bool))
```

## Next Steps


---

*Source: test_comparisons.py:22 | Complexity: Advanced | Last updated: 2026-06-02*