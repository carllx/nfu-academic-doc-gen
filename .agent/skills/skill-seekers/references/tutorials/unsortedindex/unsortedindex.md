# How To: Unsortedindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unsortedindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('z', 'a'), ('x', 'a'), ('y', 'b'), ('x', 'b'), ('y', 'a'), ('z', 'b')], names=['one', 'two'])
```

**Verification:**
```python
assert len(df.loc(axis=0)['z', :]) == 2
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame([[i, 10 * i] for i in range(6)], index=mi, columns=['one', 'two'])
```

### Step 3: Assign result = value

```python
result = df.loc(axis=0)['z', 'a']
```

### Step 4: Assign expected = value

```python
expected = df.iloc[0]
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 0'

```python
msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 0'
```

### Step 7: Call df.sort_index()

```python
df.sort_index(inplace=True)
```

**Verification:**
```python
assert len(df.loc(axis=0)['z', :]) == 2
```

### Step 8: df.loc(axis=0)['z', slice('a')]

```python
df.loc(axis=0)['z', slice('a')]
```

### Step 9: df.loc(axis=0)['q', :]

```python
df.loc(axis=0)['q', :]
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_tuples([('z', 'a'), ('x', 'a'), ('y', 'b'), ('x', 'b'), ('y', 'a'), ('z', 'b')], names=['one', 'two'])
df = DataFrame([[i, 10 * i] for i in range(6)], index=mi, columns=['one', 'two'])
result = df.loc(axis=0)['z', 'a']
expected = df.iloc[0]
tm.assert_series_equal(result, expected)
msg = 'MultiIndex slicing requires the index to be lexsorted: slicing on levels \\[1\\], lexsort depth 0'
with pytest.raises(UnsortedIndexError, match=msg):
    df.loc(axis=0)['z', slice('a')]
df.sort_index(inplace=True)
assert len(df.loc(axis=0)['z', :]) == 2
with pytest.raises(KeyError, match="'q'"):
    df.loc(axis=0)['q', :]
```

## Next Steps


---

*Source: test_sorting.py:112 | Complexity: Advanced | Last updated: 2026-06-02*