# How To: Groupsort Indexer

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupsort indexer

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pandas._libs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.integers.astype(...)

```python
a = np.random.default_rng(2).integers(0, 1000, 100).astype(np.intp)
```

### Step 2: Assign b = np.random.default_rng.integers.astype(...)

```python
b = np.random.default_rng(2).integers(0, 1000, 100).astype(np.intp)
```

### Step 3: Assign result = value

```python
result = libalgos.groupsort_indexer(a, 1000)[0]
```

### Step 4: Assign expected = np.argsort(...)

```python
expected = np.argsort(a, kind='mergesort')
```

### Step 5: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.intp)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign key = value

```python
key = a * 1000 + b
```

### Step 8: Assign result = value

```python
result = libalgos.groupsort_indexer(key, 1000000)[0]
```

### Step 9: Assign expected = np.lexsort(...)

```python
expected = np.lexsort((b, a))
```

### Step 10: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.intp)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
a = np.random.default_rng(2).integers(0, 1000, 100).astype(np.intp)
b = np.random.default_rng(2).integers(0, 1000, 100).astype(np.intp)
result = libalgos.groupsort_indexer(a, 1000)[0]
expected = np.argsort(a, kind='mergesort')
expected = expected.astype(np.intp)
tm.assert_numpy_array_equal(result, expected)
key = a * 1000 + b
result = libalgos.groupsort_indexer(key, 1000000)[0]
expected = np.lexsort((b, a))
expected = expected.astype(np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_libalgos.py:33 | Complexity: Advanced | Last updated: 2026-06-02*