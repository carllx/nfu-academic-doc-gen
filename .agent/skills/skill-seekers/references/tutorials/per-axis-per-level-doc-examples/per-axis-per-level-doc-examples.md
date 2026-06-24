# How To: Per Axis Per Level Doc Examples

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test per axis per level doc examples

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign idx = value

```python
idx = pd.IndexSlice
```

### Step 2: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
```

### Step 3: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns)
```

### Step 5: Assign result = value

```python
result = df.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]
```

### Step 6: Assign expected = value

```python
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if a in ('A1', 'A2', 'A3') and c in ('C1', 'C3')]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df.loc[idx['A1':'A3', :, ['C1', 'C3']], :]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc[(slice(None), slice(None), ['C1', 'C3']), :]
```

### Step 11: Assign expected = value

```python
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if c in ('C1', 'C3')]]
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = df.loc[idx[:, :, ['C1', 'C3']], :]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 1'

```python
msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 1'
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.loc['A1', (slice(None), 'foo')], df.loc['A1'].iloc[:, [0, 2]])
```

### Step 17: Assign df = df.sort_index(...)

```python
df = df.sort_index(axis=1)
```

### Step 18: df.loc['A1', (slice(None), 'foo')]

```python
df.loc['A1', (slice(None), 'foo')]
```

### Step 19: df.loc[(slice(None), slice(None), ['C1', 'C3']), (slice(None), 'foo')]

```python
df.loc[(slice(None), slice(None), ['C1', 'C3']), (slice(None), 'foo')]
```

### Step 20: Assign unknown = value

```python
df.loc(axis=0)[:, :, ['C1', 'C3']] = -10
```

### Step 21: df.loc['A1', ('a', slice('foo'))]

```python
df.loc['A1', ('a', slice('foo'))]
```


## Complete Example

```python
# Workflow
idx = pd.IndexSlice
index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns)
result = df.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if a in ('A1', 'A2', 'A3') and c in ('C1', 'C3')]]
tm.assert_frame_equal(result, expected)
result = df.loc[idx['A1':'A3', :, ['C1', 'C3']], :]
tm.assert_frame_equal(result, expected)
result = df.loc[(slice(None), slice(None), ['C1', 'C3']), :]
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if c in ('C1', 'C3')]]
tm.assert_frame_equal(result, expected)
result = df.loc[idx[:, :, ['C1', 'C3']], :]
tm.assert_frame_equal(result, expected)
msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 1'
with pytest.raises(UnsortedIndexError, match=msg):
    df.loc['A1', ('a', slice('foo'))]
tm.assert_frame_equal(df.loc['A1', (slice(None), 'foo')], df.loc['A1'].iloc[:, [0, 2]])
df = df.sort_index(axis=1)
df.loc['A1', (slice(None), 'foo')]
df.loc[(slice(None), slice(None), ['C1', 'C3']), (slice(None), 'foo')]
df.loc(axis=0)[:, :, ['C1', 'C3']] = -10
```

## Next Steps


---

*Source: test_slice.py:385 | Complexity: Advanced | Last updated: 2026-06-02*