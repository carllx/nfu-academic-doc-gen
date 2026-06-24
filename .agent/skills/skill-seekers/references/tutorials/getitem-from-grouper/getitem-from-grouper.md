# How To: Getitem From Grouper

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test getitem from grouper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 2], 'b': 3, 'c': 4, 'd': 5})
```

### Step 2: Assign gb = value

```python
gb = df.groupby(['a', 'b'])[['a', 'c']]
```

### Step 3: Assign idx = MultiIndex.from_tuples(...)

```python
idx = MultiIndex.from_tuples([(1, 3), (2, 3)], names=['a', 'b'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [2, 2], 'c': [8, 4]}, index=idx)
```

### Step 5: Assign result = func(...)

```python
result = func(gb)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
df = DataFrame({'a': [1, 1, 2], 'b': 3, 'c': 4, 'd': 5})
gb = df.groupby(['a', 'b'])[['a', 'c']]
idx = MultiIndex.from_tuples([(1, 3), (2, 3)], names=['a', 'b'])
expected = DataFrame({'a': [2, 2], 'c': [8, 4]}, index=idx)
result = func(gb)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:138 | Complexity: Intermediate | Last updated: 2026-06-02*