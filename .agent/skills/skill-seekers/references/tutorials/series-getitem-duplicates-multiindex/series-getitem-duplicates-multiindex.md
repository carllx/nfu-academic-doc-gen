# How To: Series Getitem Duplicates Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series getitem duplicates multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.indexing`

**Setup Required:**
```python
# Fixtures: level0_value
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[[level0_value, 'B', 'C'], [0, 26, 27, 37, 57, 67, 75, 82]], codes=[[0, 0, 0, 1, 2, 2, 2, 2, 2, 2], [1, 3, 4, 6, 0, 2, 2, 3, 5, 7]], names=['tag', 'day'])
```

### Step 2: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((len(index), 1))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(arr, index=index, columns=['val'])
```

### Step 4: Assign result = value

```python
result = df.val[level0_value]
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(arr.ravel()[0:3], name='val', index=Index([26, 37, 57], name='day'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: df.val['X']

```python
df.val['X']
```

### Step 8: df.val['A']

```python
df.val['A']
```


## Complete Example

```python
# Setup
# Fixtures: level0_value

# Workflow
index = MultiIndex(levels=[[level0_value, 'B', 'C'], [0, 26, 27, 37, 57, 67, 75, 82]], codes=[[0, 0, 0, 1, 2, 2, 2, 2, 2, 2], [1, 3, 4, 6, 0, 2, 2, 3, 5, 7]], names=['tag', 'day'])
arr = np.random.default_rng(2).standard_normal((len(index), 1))
df = DataFrame(arr, index=index, columns=['val'])
if level0_value != 'A':
    with pytest.raises(KeyError, match="^'A'$"):
        df.val['A']
with pytest.raises(KeyError, match="^'X'$"):
    df.val['X']
result = df.val[level0_value]
expected = Series(arr.ravel()[0:3], name='val', index=Index([26, 37, 57], name='day'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_getitem.py:39 | Complexity: Advanced | Last updated: 2026-06-02*