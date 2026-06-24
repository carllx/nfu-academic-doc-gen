# How To: Intersection

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: idx, sort
```

## Step-by-Step Guide

### Step 1: Assign piece1 = value

```python
piece1 = idx[:5][::-1]
```

**Verification:**
```python
assert empty.equals(expected)
```

### Step 2: Assign piece2 = value

```python
piece2 = idx[3:]
```

**Verification:**
```python
assert result.equals(idx)
```

### Step 3: Assign the_int = piece1.intersection(...)

```python
the_int = piece1.intersection(piece2, sort=sort)
```

### Step 4: Assign the_int = idx.intersection(...)

```python
the_int = idx.intersection(idx, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_int, idx)
```

### Step 6: Assign empty = unknown.intersection(...)

```python
empty = idx[:2].intersection(idx[2:], sort=sort)
```

### Step 7: Assign expected = value

```python
expected = idx[:0]
```

**Verification:**
```python
assert empty.equals(expected)
```

### Step 8: Assign tuples = value

```python
tuples = idx.values
```

### Step 9: Assign result = idx.intersection(...)

```python
result = idx.intersection(tuples)
```

**Verification:**
```python
assert result.equals(idx)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_int, idx[3:5])
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_int.sort_values(), idx[3:5])
```


## Complete Example

```python
# Setup
# Fixtures: idx, sort

# Workflow
piece1 = idx[:5][::-1]
piece2 = idx[3:]
the_int = piece1.intersection(piece2, sort=sort)
if sort in (None, True):
    tm.assert_index_equal(the_int, idx[3:5])
else:
    tm.assert_index_equal(the_int.sort_values(), idx[3:5])
the_int = idx.intersection(idx, sort=sort)
tm.assert_index_equal(the_int, idx)
empty = idx[:2].intersection(idx[2:], sort=sort)
expected = idx[:0]
assert empty.equals(expected)
tuples = idx.values
result = idx.intersection(tuples)
assert result.equals(idx)
```

## Next Steps


---

*Source: test_setops.py:285 | Complexity: Advanced | Last updated: 2026-06-02*