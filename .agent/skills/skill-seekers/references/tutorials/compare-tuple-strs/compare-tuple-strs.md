# How To: Compare Tuple Strs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare tuple strs

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('a', 'b'), ('b', 'c'), ('c', 'a')])
```

### Step 2: Assign result = value

```python
result = mi == ('c', 'a')
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([False, False, True])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = mi == ('c',)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([False, False, False])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('a', 'b'), ('b', 'c'), ('c', 'a')])
result = mi == ('c', 'a')
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)
result = mi == ('c',)
expected = np.array([False, False, False])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_equivalence.py:121 | Complexity: Intermediate | Last updated: 2026-06-02*