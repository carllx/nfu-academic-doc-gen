# How To: Getitem Partial Column Select

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem partial column select

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex(...)

```python
idx = MultiIndex(codes=[[0, 0, 0], [0, 1, 1], [1, 0, 1]], levels=[['a', 'b'], ['x', 'y'], ['p', 'q']])
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((3, 2)), index=idx)
```

### Step 3: Assign result = value

```python
result = df.loc[('a', 'y'), :]
```

### Step 4: Assign expected = value

```python
expected = df.loc['a', 'y']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = value

```python
result = df.loc[('a', 'y'), [1, 0]]
```

### Step 7: Assign expected = value

```python
expected = df.loc['a', 'y'][[1, 0]]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: df.loc[('a', 'foo'), :]

```python
df.loc[('a', 'foo'), :]
```


## Complete Example

```python
# Workflow
idx = MultiIndex(codes=[[0, 0, 0], [0, 1, 1], [1, 0, 1]], levels=[['a', 'b'], ['x', 'y'], ['p', 'q']])
df = DataFrame(np.random.default_rng(2).random((3, 2)), index=idx)
result = df.loc[('a', 'y'), :]
expected = df.loc['a', 'y']
tm.assert_frame_equal(result, expected)
result = df.loc[('a', 'y'), [1, 0]]
expected = df.loc['a', 'y'][[1, 0]]
tm.assert_frame_equal(result, expected)
with pytest.raises(KeyError, match="\\('a', 'foo'\\)"):
    df.loc[('a', 'foo'), :]
```

## Next Steps


---

*Source: test_partial.py:103 | Complexity: Advanced | Last updated: 2026-06-02*