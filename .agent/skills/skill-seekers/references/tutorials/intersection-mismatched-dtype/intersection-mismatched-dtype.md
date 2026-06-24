# How To: Intersection Mismatched Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test intersection mismatched dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `hypothesis`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign index = RangeIndex(...)

```python
index = RangeIndex(start=0, stop=20, step=2, name='foo')
```

### Step 2: Assign index = Index(...)

```python
index = Index(index, dtype=dtype)
```

### Step 3: Assign flt = index.astype(...)

```python
flt = index.astype(np.float64)
```

### Step 4: Assign result = index.intersection(...)

```python
result = index.intersection(flt)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index, exact=True)
```

### Step 6: Assign result = flt.intersection(...)

```python
result = flt.intersection(index)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, flt, exact=True)
```

### Step 8: Assign result = index.intersection(...)

```python
result = index.intersection(flt[1:])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, flt[1:], exact=True)
```

### Step 10: Assign result = unknown.intersection(...)

```python
result = flt[1:].intersection(index)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, flt[1:], exact=True)
```

### Step 12: Assign result = index.intersection(...)

```python
result = index.intersection(flt[:0])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, flt[:0], exact=True)
```

### Step 14: Assign result = unknown.intersection(...)

```python
result = flt[:0].intersection(index)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, flt[:0], exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
index = RangeIndex(start=0, stop=20, step=2, name='foo')
index = Index(index, dtype=dtype)
flt = index.astype(np.float64)
result = index.intersection(flt)
tm.assert_index_equal(result, index, exact=True)
result = flt.intersection(index)
tm.assert_index_equal(result, flt, exact=True)
result = index.intersection(flt[1:])
tm.assert_index_equal(result, flt[1:], exact=True)
result = flt[1:].intersection(index)
tm.assert_index_equal(result, flt[1:], exact=True)
result = index.intersection(flt[:0])
tm.assert_index_equal(result, flt[:0], exact=True)
result = flt[:0].intersection(index)
tm.assert_index_equal(result, flt[:0], exact=True)
```

## Next Steps


---

*Source: test_setops.py:23 | Complexity: Advanced | Last updated: 2026-06-02*