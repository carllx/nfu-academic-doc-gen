# How To: Merge Asof Index Behavior

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge asof index behavior

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: kwargs
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([1, 5, 10], name='test')
```

### Step 2: Assign left = pd.DataFrame(...)

```python
left = pd.DataFrame({'left': ['a', 'b', 'c'], 'left_time': [1, 4, 10]}, index=index)
```

### Step 3: Assign right = pd.DataFrame(...)

```python
right = pd.DataFrame({'right': [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
```

### Step 4: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, **kwargs)
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'left': ['a', 'b', 'c'], 'left_time': [1, 4, 10], 'right': [1, 3, 7]}, index=index)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: kwargs

# Workflow
index = Index([1, 5, 10], name='test')
left = pd.DataFrame({'left': ['a', 'b', 'c'], 'left_time': [1, 4, 10]}, index=index)
right = pd.DataFrame({'right': [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
result = merge_asof(left, right, **kwargs)
expected = pd.DataFrame({'left': ['a', 'b', 'c'], 'left_time': [1, 4, 10], 'right': [1, 3, 7]}, index=index)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3428 | Complexity: Intermediate | Last updated: 2026-06-02*