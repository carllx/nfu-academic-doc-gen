# How To: Intersection Monotonic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test intersection monotonic

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
# Fixtures: index2, keeps_name, sort
```

## Step-by-Step Guide

### Step 1: Assign index1 = Index(...)

```python
index1 = Index([5, 3, 2, 4, 1], name='index')
```

### Step 2: Assign expected = Index(...)

```python
expected = Index([5, 3, 4])
```

### Step 3: Assign result = index1.intersection(...)

```python
result = index1.intersection(index2, sort=sort)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign expected.name = 'index'

```python
expected.name = 'index'
```

### Step 6: Assign expected = expected.sort_values(...)

```python
expected = expected.sort_values()
```


## Complete Example

```python
# Setup
# Fixtures: index2, keeps_name, sort

# Workflow
index1 = Index([5, 3, 2, 4, 1], name='index')
expected = Index([5, 3, 4])
if keeps_name:
    expected.name = 'index'
result = index1.intersection(index2, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*