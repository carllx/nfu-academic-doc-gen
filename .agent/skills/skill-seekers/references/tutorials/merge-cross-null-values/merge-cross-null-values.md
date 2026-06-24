# How To: Merge Cross Null Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge cross null values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'a': [1, nulls_fixture]})
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'b': ['a', 'b'], 'c': [1.0, 2.0]})
```

### Step 3: Assign result = merge(...)

```python
result = merge(left, right, how='cross')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 1, nulls_fixture, nulls_fixture], 'b': ['a', 'b', 'a', 'b'], 'c': [1.0, 2.0, 1.0, 2.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
left = DataFrame({'a': [1, nulls_fixture]})
right = DataFrame({'b': ['a', 'b'], 'c': [1.0, 2.0]})
result = merge(left, right, how='cross')
expected = DataFrame({'a': [1, 1, nulls_fixture, nulls_fixture], 'b': ['a', 'b', 'a', 'b'], 'c': [1.0, 2.0, 1.0, 2.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_cross.py:77 | Complexity: Intermediate | Last updated: 2026-06-02*