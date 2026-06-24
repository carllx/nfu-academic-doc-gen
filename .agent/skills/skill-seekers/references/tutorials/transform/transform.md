# How To: Transform

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign data = Series(...)

```python
data = Series(np.arange(9) // 3, index=np.arange(9))
```

**Verification:**
```python
assert transformed[7] == 12
```

### Step 2: Assign index = np.arange(...)

```python
index = np.arange(9)
```

### Step 3: Call np.random.default_rng.shuffle()

```python
np.random.default_rng(2).shuffle(index)
```

### Step 4: Assign data = data.reindex(...)

```python
data = data.reindex(index)
```

### Step 5: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(lambda x: x // 3)
```

### Step 6: Assign transformed = grouped.transform(...)

```python
transformed = grouped.transform(lambda x: x * x.sum())
```

**Verification:**
```python
assert transformed[7] == 12
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(6, dtype='int64').reshape(3, 2), columns=['a', 'b'], index=[0, 2, 1])
```

### Step 8: Assign key = value

```python
key = [0, 0, 1]
```

### Step 9: Assign expected = df.sort_index.groupby.transform.groupby.mean(...)

```python
expected = df.sort_index().groupby(key).transform(lambda x: x - x.mean()).groupby(key).mean()
```

### Step 10: Assign result = df.groupby.transform.groupby.mean(...)

```python
result = df.groupby(key).transform(lambda x: x - x.mean()).groupby(key).mean()
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign people = DataFrame(...)

```python
people = DataFrame(np.random.default_rng(2).standard_normal((5, 5)), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
```

### Step 13: Assign key = value

```python
key = ['one', 'two', 'one', 'two', 'one']
```

### Step 14: Assign result = people.groupby.transform.groupby.mean(...)

```python
result = people.groupby(key).transform(demean).groupby(key).mean()
```

### Step 15: Assign expected = people.groupby.apply.groupby.mean(...)

```python
expected = people.groupby(key, group_keys=False).apply(demean).groupby(key).mean()
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((50, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=50, freq='B'))
```

### Step 18: Assign g = df.groupby(...)

```python
g = df.groupby(pd.Grouper(freq='ME'))
```

### Step 19: Call g.transform()

```python
g.transform(lambda x: x - 1)
```

### Step 20: Assign df = DataFrame(...)

```python
df = DataFrame({'a': range(5, 10), 'b': range(5)})
```

### Step 21: Assign msg = 'using DataFrameGroupBy.max'

```python
msg = 'using DataFrameGroupBy.max'
```

### Step 22: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': range(5)})
```

### Step 23: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 24: Assign result = df.groupby.transform(...)

```python
result = df.groupby('a').transform(max)
```


## Complete Example

```python
# Workflow
data = Series(np.arange(9) // 3, index=np.arange(9))
index = np.arange(9)
np.random.default_rng(2).shuffle(index)
data = data.reindex(index)
grouped = data.groupby(lambda x: x // 3)
transformed = grouped.transform(lambda x: x * x.sum())
assert transformed[7] == 12
df = DataFrame(np.arange(6, dtype='int64').reshape(3, 2), columns=['a', 'b'], index=[0, 2, 1])
key = [0, 0, 1]
expected = df.sort_index().groupby(key).transform(lambda x: x - x.mean()).groupby(key).mean()
result = df.groupby(key).transform(lambda x: x - x.mean()).groupby(key).mean()
tm.assert_frame_equal(result, expected)

def demean(arr):
    return arr - arr.mean(axis=0)
people = DataFrame(np.random.default_rng(2).standard_normal((5, 5)), columns=['a', 'b', 'c', 'd', 'e'], index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
key = ['one', 'two', 'one', 'two', 'one']
result = people.groupby(key).transform(demean).groupby(key).mean()
expected = people.groupby(key, group_keys=False).apply(demean).groupby(key).mean()
tm.assert_frame_equal(result, expected)
df = DataFrame(np.random.default_rng(2).standard_normal((50, 4)), columns=Index(list('ABCD'), dtype=object), index=date_range('2000-01-01', periods=50, freq='B'))
g = df.groupby(pd.Grouper(freq='ME'))
g.transform(lambda x: x - 1)
df = DataFrame({'a': range(5, 10), 'b': range(5)})
msg = 'using DataFrameGroupBy.max'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('a').transform(max)
expected = DataFrame({'b': range(5)})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:28 | Complexity: Advanced | Last updated: 2026-06-02*