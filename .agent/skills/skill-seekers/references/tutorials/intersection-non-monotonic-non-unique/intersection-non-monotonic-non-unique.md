# How To: Intersection Non Monotonic Non Unique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test intersection non monotonic non unique

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: index2, expected_arr, sort
```

## Step-by-Step Guide

### Step 1: Assign index1 = Index(...)

```python
index1 = Index(['A', 'B', 'A', 'C'])
```

### Step 2: Assign expected = Index(...)

```python
expected = Index(expected_arr)
```

### Step 3: Assign result = index1.intersection(...)

```python
result = index1.intersection(index2, sort=sort)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign expected = expected.sort_values(...)

```python
expected = expected.sort_values()
```


## Complete Example

```python
# Setup
# Fixtures: index2, expected_arr, sort

# Workflow
index1 = Index(['A', 'B', 'A', 'C'])
expected = Index(expected_arr)
result = index1.intersection(index2, sort=sort)
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*