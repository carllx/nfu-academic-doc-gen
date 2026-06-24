# How To: Intersection Non Overlapping Gcd

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection non overlapping gcd

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
# Fixtures: sort, names
```

## Step-by-Step Guide

### Step 1: Assign index = RangeIndex(...)

```python
index = RangeIndex(1, 10, 2, name=names[0])
```

### Step 2: Assign other = RangeIndex(...)

```python
other = RangeIndex(0, 10, 4, name=names[1])
```

### Step 3: Assign result = index.intersection(...)

```python
result = index.intersection(other, sort=sort)
```

### Step 4: Assign expected = RangeIndex(...)

```python
expected = RangeIndex(0, 0, 1, name=names[2])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort, names

# Workflow
index = RangeIndex(1, 10, 2, name=names[0])
other = RangeIndex(0, 10, 4, name=names[1])
result = index.intersection(other, sort=sort)
expected = RangeIndex(0, 0, 1, name=names[2])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*