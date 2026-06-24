# How To: Union

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union

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
assert result.equals(idx)
```

### Step 2: Assign piece2 = value

```python
piece2 = idx[3:]
```

### Step 3: Assign the_union = piece1.union(...)

```python
the_union = piece1.union(piece2, sort=sort)
```

### Step 4: Assign the_union = idx.union(...)

```python
the_union = idx.union(idx, sort=sort)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_union, idx)
```

### Step 6: Assign the_union = idx.union(...)

```python
the_union = idx.union(idx[:0], sort=sort)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_union, idx)
```

### Step 8: Assign tuples = value

```python
tuples = idx.values
```

### Step 9: Assign result = unknown.union(...)

```python
result = idx[:4].union(tuples[4:], sort=sort)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_union.sort_values(), idx.sort_values())
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(the_union, idx)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.sort_values(), idx.sort_values())
```

**Verification:**
```python
assert result.equals(idx)
```


## Complete Example

```python
# Setup
# Fixtures: idx, sort

# Workflow
piece1 = idx[:5][::-1]
piece2 = idx[3:]
the_union = piece1.union(piece2, sort=sort)
if sort in (None, False):
    tm.assert_index_equal(the_union.sort_values(), idx.sort_values())
else:
    tm.assert_index_equal(the_union, idx)
the_union = idx.union(idx, sort=sort)
tm.assert_index_equal(the_union, idx)
the_union = idx.union(idx[:0], sort=sort)
tm.assert_index_equal(the_union, idx)
tuples = idx.values
result = idx[:4].union(tuples[4:], sort=sort)
if sort is None:
    tm.assert_index_equal(result.sort_values(), idx.sort_values())
else:
    assert result.equals(idx)
```

## Next Steps


---

*Source: test_setops.py:240 | Complexity: Advanced | Last updated: 2026-06-02*