# How To: Left Join Index Multi Match

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test left join index multi match

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame([['c', 0], ['b', 1], ['a', 2], ['b', 3]], columns=['tag', 'val'], index=[2, 0, 1, 3])
```

### Step 2: Assign right = DataFrame.set_index(...)

```python
right = DataFrame([['a', 'v'], ['c', 'w'], ['c', 'x'], ['d', 'y'], ['a', 'z'], ['c', 'r'], ['e', 'q'], ['c', 's']], columns=['tag', 'char']).set_index('tag')
```

### Step 3: Assign result = left.join(...)

```python
result = left.join(right, on='tag', how='left')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame([['c', 0, 'w'], ['c', 0, 'x'], ['c', 0, 'r'], ['c', 0, 's'], ['b', 1, np.nan], ['a', 2, 'v'], ['a', 2, 'z'], ['b', 3, np.nan]], columns=['tag', 'val', 'char'], index=[2, 2, 2, 2, 0, 1, 1, 3])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = left.join(...)

```python
result = left.join(right, on='tag', how='left', sort=True)
```

### Step 7: Assign expected2 = expected.sort_values(...)

```python
expected2 = expected.sort_values('tag', kind='mergesort')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected2)
```

### Step 9: Assign result = merge(...)

```python
result = merge(left, right.reset_index(), how='left', on='tag')
```

### Step 10: Assign expected.index = RangeIndex(...)

```python
expected.index = RangeIndex(len(expected))
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame([['c', 0], ['b', 1], ['a', 2], ['b', 3]], columns=['tag', 'val'], index=[2, 0, 1, 3])
right = DataFrame([['a', 'v'], ['c', 'w'], ['c', 'x'], ['d', 'y'], ['a', 'z'], ['c', 'r'], ['e', 'q'], ['c', 's']], columns=['tag', 'char']).set_index('tag')
result = left.join(right, on='tag', how='left')
expected = DataFrame([['c', 0, 'w'], ['c', 0, 'x'], ['c', 0, 'r'], ['c', 0, 's'], ['b', 1, np.nan], ['a', 2, 'v'], ['a', 2, 'z'], ['b', 3, np.nan]], columns=['tag', 'val', 'char'], index=[2, 2, 2, 2, 0, 1, 1, 3])
tm.assert_frame_equal(result, expected)
result = left.join(right, on='tag', how='left', sort=True)
expected2 = expected.sort_values('tag', kind='mergesort')
tm.assert_frame_equal(result, expected2)
result = merge(left, right.reset_index(), how='left', on='tag')
expected.index = RangeIndex(len(expected))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:344 | Complexity: Advanced | Last updated: 2026-06-02*