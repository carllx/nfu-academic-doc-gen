# How To: Unstack Fill Frame Object

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack fill frame object

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape`


## Step-by-Step Guide

### Step 1: Assign data = Series(...)

```python
data = Series(['a', 'b', 'c', 'a'], dtype='object')
```

### Step 2: Assign data.index = MultiIndex.from_tuples(...)

```python
data.index = MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'b'), ('z', 'a')])
```

### Step 3: Assign result = data.unstack(...)

```python
result = data.unstack()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['a', np.nan, 'a'], 'b': ['b', 'c', np.nan]}, index=list('xyz'), dtype=object)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = data.unstack(...)

```python
result = data.unstack(fill_value='d')
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': ['a', 'd', 'a'], 'b': ['b', 'c', 'd']}, index=list('xyz'), dtype=object)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = Series(['a', 'b', 'c', 'a'], dtype='object')
data.index = MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'b'), ('z', 'a')])
result = data.unstack()
expected = DataFrame({'a': ['a', np.nan, 'a'], 'b': ['b', 'c', np.nan]}, index=list('xyz'), dtype=object)
tm.assert_frame_equal(result, expected)
result = data.unstack(fill_value='d')
expected = DataFrame({'a': ['a', 'd', 'a'], 'b': ['b', 'c', 'd']}, index=list('xyz'), dtype=object)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_stack_unstack.py:1357 | Complexity: Advanced | Last updated: 2026-06-02*