# How To: Compare Tuple

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare tuple

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_product(...)

```python
mi = MultiIndex.from_product([[1, 2]] * 2)
```

### Step 2: Assign all_false = np.array(...)

```python
all_false = np.array([False, False, False, False])
```

### Step 3: Assign result = value

```python
result = mi == mi[0]
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = mi != mi[0]
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```

### Step 8: Assign result = value

```python
result = mi < mi[0]
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, all_false)
```

### Step 10: Assign result = value

```python
result = mi <= mi[0]
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 12: Assign result = value

```python
result = mi > mi[0]
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```

### Step 14: Assign result = value

```python
result = mi >= mi[0]
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~all_false)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_product([[1, 2]] * 2)
all_false = np.array([False, False, False, False])
result = mi == mi[0]
expected = np.array([True, False, False, False])
tm.assert_numpy_array_equal(result, expected)
result = mi != mi[0]
tm.assert_numpy_array_equal(result, ~expected)
result = mi < mi[0]
tm.assert_numpy_array_equal(result, all_false)
result = mi <= mi[0]
tm.assert_numpy_array_equal(result, expected)
result = mi > mi[0]
tm.assert_numpy_array_equal(result, ~expected)
result = mi >= mi[0]
tm.assert_numpy_array_equal(result, ~all_false)
```

## Next Steps


---

*Source: test_equivalence.py:95 | Complexity: Advanced | Last updated: 2026-06-02*