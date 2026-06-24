# How To: Intersection Uint64 Outside Int64 Range

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection uint64 outside int64 range

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`

**Setup Required:**
```python
# Fixtures: index_large
```

## Step-by-Step Guide

### Step 1: Assign other = Index(...)

```python
other = Index([2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10, 2 ** 63 + 15, 2 ** 63 + 20])
```

### Step 2: Assign result = index_large.intersection(...)

```python
result = index_large.intersection(other)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(np.sort(np.intersect1d(index_large.values, other.values)))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = other.intersection(...)

```python
result = other.intersection(index_large)
```

### Step 6: Assign expected = Index(...)

```python
expected = Index(np.sort(np.asarray(np.intersect1d(index_large.values, other.values))))
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: index_large

# Workflow
other = Index([2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10, 2 ** 63 + 15, 2 ** 63 + 20])
result = index_large.intersection(other)
expected = Index(np.sort(np.intersect1d(index_large.values, other.values)))
tm.assert_index_equal(result, expected)
result = other.intersection(index_large)
expected = Index(np.sort(np.asarray(np.intersect1d(index_large.values, other.values))))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*