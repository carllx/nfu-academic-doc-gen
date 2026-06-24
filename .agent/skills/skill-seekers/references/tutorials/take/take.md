# How To: Take

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: closed
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_breaks(...)

```python
index = IntervalIndex.from_breaks(range(11), closed=closed)
```

### Step 2: Assign result = index.take(...)

```python
result = index.take(range(10))
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, index)
```

### Step 4: Assign result = index.take(...)

```python
result = index.take([0, 0, 1])
```

### Step 5: Assign expected = IntervalIndex.from_arrays(...)

```python
expected = IntervalIndex.from_arrays([0, 0, 1], [1, 1, 2], closed=closed)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed

# Workflow
index = IntervalIndex.from_breaks(range(11), closed=closed)
result = index.take(range(10))
tm.assert_index_equal(result, index)
result = index.take([0, 0, 1])
expected = IntervalIndex.from_arrays([0, 0, 1], [1, 1, 2], closed=closed)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*