# How To: Setops Preserve Object Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setops preserve object dtype

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([1, 2, 3], dtype=object)
```

### Step 2: Assign result = idx.intersection(...)

```python
result = idx.intersection(idx[1:])
```

### Step 3: Assign expected = value

```python
expected = idx[1:]
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = idx.intersection(...)

```python
result = idx.intersection(idx[1:][::-1])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = idx._union(...)

```python
result = idx._union(idx[1:], sort=None)
```

### Step 8: Assign expected = idx

```python
expected = idx
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected.values)
```

### Step 10: Assign result = idx.union(...)

```python
result = idx.union(idx[1:], sort=None)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign result = idx._union(...)

```python
result = idx._union(idx[1:][::-1], sort=None)
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected.values)
```

### Step 14: Assign result = idx.union(...)

```python
result = idx.union(idx[1:][::-1], sort=None)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = Index([1, 2, 3], dtype=object)
result = idx.intersection(idx[1:])
expected = idx[1:]
tm.assert_index_equal(result, expected)
result = idx.intersection(idx[1:][::-1])
tm.assert_index_equal(result, expected)
result = idx._union(idx[1:], sort=None)
expected = idx
tm.assert_numpy_array_equal(result, expected.values)
result = idx.union(idx[1:], sort=None)
tm.assert_index_equal(result, expected)
result = idx._union(idx[1:][::-1], sort=None)
tm.assert_numpy_array_equal(result, expected.values)
result = idx.union(idx[1:][::-1], sort=None)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:36 | Complexity: Advanced | Last updated: 2026-06-02*