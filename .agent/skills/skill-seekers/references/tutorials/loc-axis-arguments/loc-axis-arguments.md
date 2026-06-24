# How To: Loc Axis Arguments

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc axis arguments

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

### Step 1: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
```

### Step 2: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
```

### Step 3: Assign df = DataFrame.sort_index.sort_index(...)

```python
df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns).sort_index().sort_index(axis=1)
```

### Step 4: Assign result = value

```python
result = df.loc(axis=0)['A1':'A3', :, ['C1', 'C3']]
```

### Step 5: Assign expected = value

```python
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if a in ('A1', 'A2', 'A3') and c in ('C1', 'C3')]]
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = df.loc(axis='index')[:, :, ['C1', 'C3']]
```

### Step 8: Assign expected = value

```python
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if c in ('C1', 'C3')]]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df.loc(axis=1)[:, 'foo']
```

### Step 11: Assign expected = value

```python
expected = df.loc[:, (slice(None), 'foo')]
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = df.loc(axis='columns')[:, 'foo']
```

### Step 14: Assign expected = value

```python
expected = df.loc[:, (slice(None), 'foo')]
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign msg = value

```python
msg = f'No axis named {i} for object type DataFrame'
```

### Step 17: df.loc(axis=i)[:, :, ['C1', 'C3']]

```python
df.loc(axis=i)[:, :, ['C1', 'C3']]
```


## Complete Example

```python
# Workflow
index = MultiIndex.from_product([_mklbl('A', 4), _mklbl('B', 2), _mklbl('C', 4), _mklbl('D', 2)])
columns = MultiIndex.from_tuples([('a', 'foo'), ('a', 'bar'), ('b', 'foo'), ('b', 'bah')], names=['lvl0', 'lvl1'])
df = DataFrame(np.arange(len(index) * len(columns), dtype='int64').reshape((len(index), len(columns))), index=index, columns=columns).sort_index().sort_index(axis=1)
result = df.loc(axis=0)['A1':'A3', :, ['C1', 'C3']]
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if a in ('A1', 'A2', 'A3') and c in ('C1', 'C3')]]
tm.assert_frame_equal(result, expected)
result = df.loc(axis='index')[:, :, ['C1', 'C3']]
expected = df.loc[[(a, b, c, d) for a, b, c, d in df.index.values if c in ('C1', 'C3')]]
tm.assert_frame_equal(result, expected)
result = df.loc(axis=1)[:, 'foo']
expected = df.loc[:, (slice(None), 'foo')]
tm.assert_frame_equal(result, expected)
result = df.loc(axis='columns')[:, 'foo']
expected = df.loc[:, (slice(None), 'foo')]
tm.assert_frame_equal(result, expected)
for i in [-1, 2, 'foo']:
    msg = f'No axis named {i} for object type DataFrame'
    with pytest.raises(ValueError, match=msg):
        df.loc(axis=i)[:, :, ['C1', 'C3']]
```

## Next Steps


---

*Source: test_slice.py:460 | Complexity: Advanced | Last updated: 2026-06-02*