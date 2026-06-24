# How To: Join Non Int Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join non int index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
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
other = Index(2 ** 63 + np.array([1, 5, 7, 10, 20], dtype='uint64'), dtype=object)
```

### Step 2: Assign outer = index_large.join(...)

```python
outer = index_large.join(other, how='outer')
```

### Step 3: Assign outer2 = other.join(...)

```python
outer2 = other.join(index_large, how='outer')
```

### Step 4: Assign expected = Index(...)

```python
expected = Index(2 ** 63 + np.array([0, 1, 5, 7, 10, 15, 20, 25], dtype='uint64'))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, outer2)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(outer, expected)
```

### Step 7: Assign inner = index_large.join(...)

```python
inner = index_large.join(other, how='inner')
```

### Step 8: Assign inner2 = other.join(...)

```python
inner2 = other.join(index_large, how='inner')
```

### Step 9: Assign expected = Index(...)

```python
expected = Index(2 ** 63 + np.array([10, 20], dtype='uint64'))
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, inner2)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(inner, expected)
```

### Step 12: Assign left = index_large.join(...)

```python
left = index_large.join(other, how='left')
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(left, index_large.astype(object))
```

### Step 14: Assign left2 = other.join(...)

```python
left2 = other.join(index_large, how='left')
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(left2, other)
```

### Step 16: Assign right = index_large.join(...)

```python
right = index_large.join(other, how='right')
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(right, other)
```

### Step 18: Assign right2 = other.join(...)

```python
right2 = other.join(index_large, how='right')
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(right2, index_large.astype(object))
```


## Complete Example

```python
# Setup
# Fixtures: index_large

# Workflow
other = Index(2 ** 63 + np.array([1, 5, 7, 10, 20], dtype='uint64'), dtype=object)
outer = index_large.join(other, how='outer')
outer2 = other.join(index_large, how='outer')
expected = Index(2 ** 63 + np.array([0, 1, 5, 7, 10, 15, 20, 25], dtype='uint64'))
tm.assert_index_equal(outer, outer2)
tm.assert_index_equal(outer, expected)
inner = index_large.join(other, how='inner')
inner2 = other.join(index_large, how='inner')
expected = Index(2 ** 63 + np.array([10, 20], dtype='uint64'))
tm.assert_index_equal(inner, inner2)
tm.assert_index_equal(inner, expected)
left = index_large.join(other, how='left')
tm.assert_index_equal(left, index_large.astype(object))
left2 = other.join(index_large, how='left')
tm.assert_index_equal(left2, other)
right = index_large.join(other, how='right')
tm.assert_index_equal(right, other)
right2 = other.join(index_large, how='right')
tm.assert_index_equal(right2, index_large.astype(object))
```

## Next Steps


---

*Source: test_join.py:315 | Complexity: Advanced | Last updated: 2026-06-02*