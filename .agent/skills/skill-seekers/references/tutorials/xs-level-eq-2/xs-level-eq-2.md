# How To: Xs Level Eq 2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test xs level eq 2

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((3, 5))
```

### Step 2: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[['a', 'p', 'x'], ['b', 'q', 'y'], ['c', 'r', 'z']], codes=[[2, 0, 1], [2, 0, 1], [2, 0, 1]])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr, index=index)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(arr[1:2], index=[['a'], ['b']])
```

### Step 5: Assign result = df.xs(...)

```python
result = df.xs('c', level=2)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((3, 5))
index = MultiIndex(levels=[['a', 'p', 'x'], ['b', 'q', 'y'], ['c', 'r', 'z']], codes=[[2, 0, 1], [2, 0, 1], [2, 0, 1]])
df = DataFrame(arr, index=index)
expected = DataFrame(arr[1:2], index=[['a'], ['b']])
result = df.xs('c', level=2)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_xs.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*