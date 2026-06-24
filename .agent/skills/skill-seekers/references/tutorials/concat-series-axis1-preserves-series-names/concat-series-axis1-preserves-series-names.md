# How To: Concat Series Axis1 Preserves Series Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series axis1 preserves series names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.random.default_rng(2).standard_normal(5), name='A')
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series(np.random.default_rng(2).standard_normal(5), name='B')
```

### Step 3: Assign result = concat(...)

```python
result = concat([s, s2], axis=1)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': s, 'B': s2})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign s2.name = None

```python
s2.name = None
```

### Step 7: Assign result = concat(...)

```python
result = concat([s, s2], axis=1)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, Index(['A', 0], dtype='object'))
```


## Complete Example

```python
# Workflow
s = Series(np.random.default_rng(2).standard_normal(5), name='A')
s2 = Series(np.random.default_rng(2).standard_normal(5), name='B')
result = concat([s, s2], axis=1)
expected = DataFrame({'A': s, 'B': s2})
tm.assert_frame_equal(result, expected)
s2.name = None
result = concat([s, s2], axis=1)
tm.assert_index_equal(result.columns, Index(['A', 0], dtype='object'))
```

## Next Steps


---

*Source: test_series.py:67 | Complexity: Advanced | Last updated: 2026-06-02*