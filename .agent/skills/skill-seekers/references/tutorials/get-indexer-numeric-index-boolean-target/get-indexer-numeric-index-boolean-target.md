# How To: Get Indexer Numeric Index Boolean Target

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer numeric index boolean target

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: method, idx_dtype
```

## Step-by-Step Guide

### Step 1: Assign other = Index(...)

```python
other = Index([True, False, True])
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(numeric_index, method)(other)
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([-1, -1, -1], dtype=np.intp)
```

### Step 4: Assign numeric_index = RangeIndex(...)

```python
numeric_index = RangeIndex(4)
```

### Step 5: Assign numeric_index = Index(...)

```python
numeric_index = Index(np.arange(4, dtype=idx_dtype))
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign missing = np.arange(...)

```python
missing = np.arange(3, dtype=np.intp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[0], expected)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result[1], missing)
```


## Complete Example

```python
# Setup
# Fixtures: method, idx_dtype

# Workflow
if idx_dtype == 'range':
    numeric_index = RangeIndex(4)
else:
    numeric_index = Index(np.arange(4, dtype=idx_dtype))
other = Index([True, False, True])
result = getattr(numeric_index, method)(other)
expected = np.array([-1, -1, -1], dtype=np.intp)
if method == 'get_indexer':
    tm.assert_numpy_array_equal(result, expected)
else:
    missing = np.arange(3, dtype=np.intp)
    tm.assert_numpy_array_equal(result[0], expected)
    tm.assert_numpy_array_equal(result[1], missing)
```

## Next Steps


---

*Source: test_indexing.py:216 | Complexity: Advanced | Last updated: 2026-06-02*