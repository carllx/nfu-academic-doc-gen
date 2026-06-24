# How To: Concat Series Axis1 With Reindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series axis1 with reindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: sort
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(3), index=['c', 'a', 'b'], name='A')
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series(np.random.default_rng(2).standard_normal(4), index=['d', 'a', 'b', 'c'], name='B')
```

### Step 3: Assign result = concat(...)

```python
result = concat([s, s2], axis=1, sort=sort)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': s, 'B': s2}, index=['c', 'a', 'b', 'd'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```


## Complete Example

```python
# Setup
# Fixtures: sort

# Workflow
s = Series(np.random.default_rng(2).standard_normal(3), index=['c', 'a', 'b'], name='A')
s2 = Series(np.random.default_rng(2).standard_normal(4), index=['d', 'a', 'b', 'c'], name='B')
result = concat([s, s2], axis=1, sort=sort)
expected = DataFrame({'A': s, 'B': s2}, index=['c', 'a', 'b', 'd'])
if sort:
    expected = expected.sort_index()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_series.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*