# How To: Comparison With Tuple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test comparison with tuple

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(np.array(['foo', (0, 1), 3, (0, 1)], dtype=object))
```

### Step 2: Assign result = value

```python
result = cat == 'foo'
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False], dtype=bool)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = cat == (0, 1)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([False, True, False, True], dtype=bool)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = cat != (0, 1)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, ~expected)
```


## Complete Example

```python
# Workflow
cat = Categorical(np.array(['foo', (0, 1), 3, (0, 1)], dtype=object))
result = cat == 'foo'
expected = np.array([True, False, False, False], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
result = cat == (0, 1)
expected = np.array([False, True, False, True], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
result = cat != (0, 1)
tm.assert_numpy_array_equal(result, ~expected)
```

## Next Steps


---

*Source: test_operators.py:198 | Complexity: Advanced | Last updated: 2026-06-02*