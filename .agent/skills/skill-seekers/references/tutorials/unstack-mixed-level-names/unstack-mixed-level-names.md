# How To: Unstack Mixed Level Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unstack mixed level names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['a', 'a'], [1, 2], ['red', 'blue']]
```

### Step 2: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays(arrays, names=('x', 0, 'y'))
```

### Step 3: Assign ser = Series(...)

```python
ser = Series([1, 2], index=idx)
```

### Step 4: Assign result = ser.unstack(...)

```python
result = ser.unstack('x')
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1], [2]], columns=Index(['a'], name='x'), index=MultiIndex.from_tuples([(1, 'red'), (2, 'blue')], names=[0, 'y']))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'a'], [1, 2], ['red', 'blue']]
idx = MultiIndex.from_arrays(arrays, names=('x', 0, 'y'))
ser = Series([1, 2], index=idx)
result = ser.unstack('x')
expected = DataFrame([[1], [2]], columns=Index(['a'], name='x'), index=MultiIndex.from_tuples([(1, 'red'), (2, 'blue')], names=[0, 'y']))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_unstack.py:158 | Complexity: Intermediate | Last updated: 2026-06-02*