# How To: Empty Frame Groupby Dtypes Consistency

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test empty frame groupby dtypes consistency

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: d
```

## Step-by-Step Guide

### Step 1: Assign group_keys = value

```python
group_keys = ['a', 'b', 'c']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1], 'b': [2], 'c': [3], 'd': [d]})
```

### Step 3: Assign g = unknown.groupby(...)

```python
g = df[df.a == 2].groupby(group_keys)
```

### Step 4: Assign result = value

```python
result = g.first().index
```

### Step 5: Assign expected = MultiIndex(...)

```python
expected = MultiIndex(levels=[[1], [2], [3]], codes=[[], [], []], names=['a', 'b', 'c'])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: d

# Workflow
group_keys = ['a', 'b', 'c']
df = DataFrame({'a': [1], 'b': [2], 'c': [3], 'd': [d]})
g = df[df.a == 2].groupby(group_keys)
result = g.first().index
expected = MultiIndex(levels=[[1], [2], [3]], codes=[[], [], []], names=['a', 'b', 'c'])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_multilevel.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*