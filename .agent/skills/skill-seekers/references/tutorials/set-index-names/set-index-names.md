# How To: Set Index Names

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index names

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.ones((10, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(10)]))
```

**Verification:**
```python
assert df.set_index(df.index).index.names == ['name']
```

### Step 2: Assign df.index.name = 'name'

```python
df.index.name = 'name'
```

**Verification:**
```python
assert df.set_index(df.index).index.names == ['A', 'B']
```

### Step 3: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays(df[['A', 'B']].T.values, names=['A', 'B'])
```

**Verification:**
```python
assert isinstance(df.set_index(df.index).index, MultiIndex)
```

### Step 4: Assign mi2 = MultiIndex.from_arrays(...)

```python
mi2 = MultiIndex.from_arrays(df[['A', 'B', 'A', 'B']].T.values, names=['A', 'B', 'C', 'D'])
```

**Verification:**
```python
assert isinstance(df.set_index([df.index, idx2]).index, MultiIndex)
```

### Step 5: Assign df = df.set_index(...)

```python
df = df.set_index(['A', 'B'])
```

**Verification:**
```python
assert df.set_index(df.index).index.names == ['A', 'B']
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.set_index(df.index).index, mi)
```

### Step 7: Assign idx2 = df.index.rename(...)

```python
idx2 = df.index.rename(['C', 'D'])
```

**Verification:**
```python
assert isinstance(df.set_index([df.index, idx2]).index, MultiIndex)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.set_index([df.index, idx2]).index, mi2)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.ones((10, 4)), columns=Index(list('ABCD')), index=Index([f'i-{i}' for i in range(10)]))
df.index.name = 'name'
assert df.set_index(df.index).index.names == ['name']
mi = MultiIndex.from_arrays(df[['A', 'B']].T.values, names=['A', 'B'])
mi2 = MultiIndex.from_arrays(df[['A', 'B', 'A', 'B']].T.values, names=['A', 'B', 'C', 'D'])
df = df.set_index(['A', 'B'])
assert df.set_index(df.index).index.names == ['A', 'B']
assert isinstance(df.set_index(df.index).index, MultiIndex)
tm.assert_index_equal(df.set_index(df.index).index, mi)
idx2 = df.index.rename(['C', 'D'])
assert isinstance(df.set_index([df.index, idx2]).index, MultiIndex)
tm.assert_index_equal(df.set_index([df.index, idx2]).index, mi2)
```

## Next Steps


---

*Source: test_set_index.py:158 | Complexity: Advanced | Last updated: 2026-06-02*