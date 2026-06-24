# How To: Union Non Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union non numeric

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
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(np.arange(5, dtype=dtype), dtype=dtype)
```

**Verification:**
```python
assert index.dtype == dtype
```

### Step 2: Assign other = Index(...)

```python
other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
```

### Step 3: Assign result = index.union(...)

```python
result = index.union(other)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(np.concatenate((index, other)))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = other.union(...)

```python
result = other.union(index)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index(np.concatenate((other, index)))
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
index = Index(np.arange(5, dtype=dtype), dtype=dtype)
assert index.dtype == dtype
other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
result = index.union(other)
expected = Index(np.concatenate((index, other)))
tm.assert_index_equal(result, expected)
result = other.union(index)
expected = Index(np.concatenate((other, index)))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:25 | Complexity: Advanced | Last updated: 2026-06-02*