# How To: Mixed Depth Drop

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed depth drop

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['a', 'top', 'top', 'routine1', 'routine1', 'routine2'], ['', 'OD', 'OD', 'result1', 'result2', 'result1'], ['', 'wx', 'wy', '', '', '']]
```

### Step 2: Assign tuples = sorted(...)

```python
tuples = sorted(zip(*arrays))
```

### Step 3: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((4, 6)), columns=index)
```

### Step 5: Assign result = df.drop(...)

```python
result = df.drop('a', axis=1)
```

### Step 6: Assign expected = df.drop(...)

```python
expected = df.drop([('a', '', '')], axis=1)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 8: Assign result = df.drop(...)

```python
result = df.drop(['top'], axis=1)
```

### Step 9: Assign expected = df.drop(...)

```python
expected = df.drop([('top', 'OD', 'wx')], axis=1)
```

### Step 10: Assign expected = expected.drop(...)

```python
expected = expected.drop([('top', 'OD', 'wy')], axis=1)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 12: Assign result = df.drop(...)

```python
result = df.drop(('top', 'OD', 'wx'), axis=1)
```

### Step 13: Assign expected = df.drop(...)

```python
expected = df.drop([('top', 'OD', 'wx')], axis=1)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```

### Step 15: Assign expected = df.drop(...)

```python
expected = df.drop([('top', 'OD', 'wy')], axis=1)
```

### Step 16: Assign expected = df.drop(...)

```python
expected = df.drop('top', axis=1)
```

### Step 17: Assign result = df.drop(...)

```python
result = df.drop('result1', level=1, axis=1)
```

### Step 18: Assign expected = df.drop(...)

```python
expected = df.drop([('routine1', 'result1', ''), ('routine2', 'result1', '')], axis=1)
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(expected, result)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'top', 'top', 'routine1', 'routine1', 'routine2'], ['', 'OD', 'OD', 'result1', 'result2', 'result1'], ['', 'wx', 'wy', '', '', '']]
tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.default_rng(2).standard_normal((4, 6)), columns=index)
result = df.drop('a', axis=1)
expected = df.drop([('a', '', '')], axis=1)
tm.assert_frame_equal(expected, result)
result = df.drop(['top'], axis=1)
expected = df.drop([('top', 'OD', 'wx')], axis=1)
expected = expected.drop([('top', 'OD', 'wy')], axis=1)
tm.assert_frame_equal(expected, result)
result = df.drop(('top', 'OD', 'wx'), axis=1)
expected = df.drop([('top', 'OD', 'wx')], axis=1)
tm.assert_frame_equal(expected, result)
expected = df.drop([('top', 'OD', 'wy')], axis=1)
expected = df.drop('top', axis=1)
result = df.drop('result1', level=1, axis=1)
expected = df.drop([('routine1', 'result1', ''), ('routine2', 'result1', '')], axis=1)
tm.assert_frame_equal(expected, result)
```

## Next Steps


---

*Source: test_drop.py:296 | Complexity: Advanced | Last updated: 2026-06-02*