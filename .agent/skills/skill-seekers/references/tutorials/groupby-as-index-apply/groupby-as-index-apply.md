# How To: Groupby As Index Apply

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby as index apply

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'item_id': ['b', 'b', 'a', 'c', 'a', 'b'], 'user_id': [1, 2, 1, 1, 3, 1], 'time': range(6)})
```

### Step 2: Assign g_as = df.groupby(...)

```python
g_as = df.groupby('user_id', as_index=True)
```

### Step 3: Assign g_not_as = df.groupby(...)

```python
g_not_as = df.groupby('user_id', as_index=False)
```

### Step 4: Assign res_as = value

```python
res_as = g_as.head(2).index
```

### Step 5: Assign res_not_as = value

```python
res_not_as = g_not_as.head(2).index
```

### Step 6: Assign exp = Index(...)

```python
exp = Index([0, 1, 2, 4])
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_as, exp)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_not_as, exp)
```

### Step 9: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 10: Assign exp_not_as_apply = MultiIndex.from_tuples(...)

```python
exp_not_as_apply = MultiIndex.from_tuples([(0, 0), (0, 2), (1, 1), (2, 4)])
```

### Step 11: Assign tp = value

```python
tp = [(1, 0), (1, 2), (2, 1), (3, 4)]
```

### Step 12: Assign exp_as_apply = MultiIndex.from_tuples(...)

```python
exp_as_apply = MultiIndex.from_tuples(tp, names=['user_id', None])
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_as_apply, exp_as_apply)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_not_as_apply, exp_not_as_apply)
```

### Step 15: Assign ind = Index(...)

```python
ind = Index(list('abcde'))
```

### Step 16: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [2, 3], [1, 4], [1, 5], [2, 6]], index=ind)
```

### Step 17: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, ind)
```

### Step 19: Assign res_as_apply = value

```python
res_as_apply = g_as.apply(lambda x: x.head(2)).index
```

### Step 20: Assign res_not_as_apply = value

```python
res_not_as_apply = g_not_as.apply(lambda x: x.head(2)).index
```

### Step 21: Assign res = value

```python
res = df.groupby(0, as_index=False, group_keys=False).apply(lambda x: x).index
```


## Complete Example

```python
# Workflow
df = DataFrame({'item_id': ['b', 'b', 'a', 'c', 'a', 'b'], 'user_id': [1, 2, 1, 1, 3, 1], 'time': range(6)})
g_as = df.groupby('user_id', as_index=True)
g_not_as = df.groupby('user_id', as_index=False)
res_as = g_as.head(2).index
res_not_as = g_not_as.head(2).index
exp = Index([0, 1, 2, 4])
tm.assert_index_equal(res_as, exp)
tm.assert_index_equal(res_not_as, exp)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res_as_apply = g_as.apply(lambda x: x.head(2)).index
with tm.assert_produces_warning(FutureWarning, match=msg):
    res_not_as_apply = g_not_as.apply(lambda x: x.head(2)).index
exp_not_as_apply = MultiIndex.from_tuples([(0, 0), (0, 2), (1, 1), (2, 4)])
tp = [(1, 0), (1, 2), (2, 1), (3, 4)]
exp_as_apply = MultiIndex.from_tuples(tp, names=['user_id', None])
tm.assert_index_equal(res_as_apply, exp_as_apply)
tm.assert_index_equal(res_not_as_apply, exp_not_as_apply)
ind = Index(list('abcde'))
df = DataFrame([[1, 2], [2, 3], [1, 4], [1, 5], [2, 6]], index=ind)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = df.groupby(0, as_index=False, group_keys=False).apply(lambda x: x).index
tm.assert_index_equal(res, ind)
```

## Next Steps


---

*Source: test_apply.py:324 | Complexity: Advanced | Last updated: 2026-06-02*