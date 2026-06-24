# How To: Frame Mixed Depth Get

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test frame mixed depth get

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`


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

### Step 5: Assign result = value

```python
result = df['a']
```

### Step 6: Assign expected = unknown.rename(...)

```python
expected = df['a', '', ''].rename('a')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df['routine1', 'result1']
```

### Step 9: Assign expected = value

```python
expected = df['routine1', 'result1', '']
```

### Step 10: Assign expected = expected.rename(...)

```python
expected = expected.rename(('routine1', 'result1'))
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [['a', 'top', 'top', 'routine1', 'routine1', 'routine2'], ['', 'OD', 'OD', 'result1', 'result2', 'result1'], ['', 'wx', 'wy', '', '', '']]
tuples = sorted(zip(*arrays))
index = MultiIndex.from_tuples(tuples)
df = DataFrame(np.random.default_rng(2).standard_normal((4, 6)), columns=index)
result = df['a']
expected = df['a', '', ''].rename('a')
tm.assert_series_equal(result, expected)
result = df['routine1', 'result1']
expected = df['routine1', 'result1', '']
expected = expected.rename(('routine1', 'result1'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:198 | Complexity: Advanced | Last updated: 2026-06-02*