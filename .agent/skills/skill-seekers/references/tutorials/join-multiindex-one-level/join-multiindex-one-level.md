# How To: Join Multiindex One Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join multiindex one level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: join_type
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame(data={'c': 3}, index=MultiIndex.from_tuples([(1, 2)], names=('a', 'b')))
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame(data={'d': 4}, index=MultiIndex.from_tuples([(2,)], names=('b',)))
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, how=join_type)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': [3], 'd': [4]}, index=MultiIndex.from_tuples([(2, 1)], names=['b', 'a']))
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'c': [3], 'd': [4]}, index=MultiIndex.from_tuples([(1, 2)], names=['a', 'b']))
```


## Complete Example

```python
# Setup
# Fixtures: join_type

# Workflow
left = DataFrame(data={'c': 3}, index=MultiIndex.from_tuples([(1, 2)], names=('a', 'b')))
right = DataFrame(data={'d': 4}, index=MultiIndex.from_tuples([(2,)], names=('b',)))
result = left.join(right, how=join_type)
if join_type == 'right':
    expected = DataFrame({'c': [3], 'd': [4]}, index=MultiIndex.from_tuples([(2, 1)], names=['b', 'a']))
else:
    expected = DataFrame({'c': [3], 'd': [4]}, index=MultiIndex.from_tuples([(1, 2)], names=['a', 'b']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:948 | Complexity: Intermediate | Last updated: 2026-06-02*