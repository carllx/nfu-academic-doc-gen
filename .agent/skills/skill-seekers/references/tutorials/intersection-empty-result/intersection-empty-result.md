# How To: Intersection Empty Result

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection empty result

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

### Step 1: Assign index = monotonic_index(...)

```python
index = monotonic_index(0, 11, closed=closed)
```

### Step 2: Assign other = monotonic_index(...)

```python
other = monotonic_index(300, 314, closed=closed)
```

### Step 3: Assign expected = empty_index(...)

```python
expected = empty_index(dtype='int64', closed=closed)
```

### Step 4: Assign result = index.intersection(...)

```python
result = index.intersection(other, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign other = monotonic_index(...)

```python
other = monotonic_index(300, 314, dtype='float64', closed=closed)
```

### Step 7: Assign result = index.intersection(...)

```python
result = index.intersection(other, sort=sort)
```

### Step 8: Assign expected = value

```python
expected = other[:0]
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign other = monotonic_index(...)

```python
other = monotonic_index(300, 314, dtype='uint64', closed=closed)
```

### Step 11: Assign result = index.intersection(...)

```python
result = index.intersection(other, sort=sort)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, sort

# Workflow
index = monotonic_index(0, 11, closed=closed)
other = monotonic_index(300, 314, closed=closed)
expected = empty_index(dtype='int64', closed=closed)
result = index.intersection(other, sort=sort)
tm.assert_index_equal(result, expected)
other = monotonic_index(300, 314, dtype='float64', closed=closed)
result = index.intersection(other, sort=sort)
expected = other[:0]
tm.assert_index_equal(result, expected)
other = monotonic_index(300, 314, dtype='uint64', closed=closed)
result = index.intersection(other, sort=sort)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:104 | Complexity: Advanced | Last updated: 2026-06-02*