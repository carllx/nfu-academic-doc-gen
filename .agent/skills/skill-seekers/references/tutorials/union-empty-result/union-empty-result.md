# How To: Union Empty Result

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union empty result

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed, sort
```

## Step-by-Step Guide

### Step 1: Assign index = empty_index(...)

```python
index = empty_index(dtype='int64', closed=closed)
```

### Step 2: Assign result = index.union(...)

```python
result = index.union(index, sort=sort)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```

### Step 4: Assign other = empty_index(...)

```python
other = empty_index(dtype='float64', closed=closed)
```

### Step 5: Assign result = index.union(...)

```python
result = index.union(other, sort=sort)
```

### Step 6: Assign expected = other

```python
expected = other
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign other = index.union(...)

```python
other = index.union(index, sort=sort)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign other = empty_index(...)

```python
other = empty_index(dtype='uint64', closed=closed)
```

### Step 11: Assign result = index.union(...)

```python
result = index.union(other, sort=sort)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 13: Assign result = other.union(...)

```python
result = other.union(index, sort=sort)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, sort

# Workflow
index = empty_index(dtype='int64', closed=closed)
result = index.union(index, sort=sort)
tm.assert_index_equal(result, index)
other = empty_index(dtype='float64', closed=closed)
result = index.union(other, sort=sort)
expected = other
tm.assert_index_equal(result, expected)
other = index.union(index, sort=sort)
tm.assert_index_equal(result, expected)
other = empty_index(dtype='uint64', closed=closed)
result = index.union(other, sort=sort)
tm.assert_index_equal(result, expected)
result = other.union(index, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:42 | Complexity: Advanced | Last updated: 2026-06-02*