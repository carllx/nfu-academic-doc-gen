# How To: Mutate Groups

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mutate groups

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'cat1': ['a'] * 8 + ['b'] * 6, 'cat2': ['c'] * 2 + ['d'] * 2 + ['e'] * 2 + ['f'] * 2 + ['c'] * 2 + ['d'] * 2 + ['e'] * 2, 'cat3': [f'g{x}' for x in range(1, 15)], 'val': np.random.default_rng(2).integers(100, size=14)})
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(grpby_copy, grpby_no_copy)
```

### Step 4: Assign x = x.copy(...)

```python
x = x.copy()
```

### Step 5: Assign unknown = x.val.rank(...)

```python
x['rank'] = x.val.rank(method='min')
```

### Step 6: Assign unknown = x.val.rank(...)

```python
x['rank'] = x.val.rank(method='min')
```

### Step 7: Assign grpby_copy = df.groupby.apply(...)

```python
grpby_copy = df.groupby('cat1').apply(f_copy)
```

### Step 8: Assign grpby_no_copy = df.groupby.apply(...)

```python
grpby_no_copy = df.groupby('cat1').apply(f_no_copy)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'cat1': ['a'] * 8 + ['b'] * 6, 'cat2': ['c'] * 2 + ['d'] * 2 + ['e'] * 2 + ['f'] * 2 + ['c'] * 2 + ['d'] * 2 + ['e'] * 2, 'cat3': [f'g{x}' for x in range(1, 15)], 'val': np.random.default_rng(2).integers(100, size=14)})

def f_copy(x):
    x = x.copy()
    x['rank'] = x.val.rank(method='min')
    return x.groupby('cat2')['rank'].min()

def f_no_copy(x):
    x['rank'] = x.val.rank(method='min')
    return x.groupby('cat2')['rank'].min()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grpby_copy = df.groupby('cat1').apply(f_copy)
with tm.assert_produces_warning(FutureWarning, match=msg):
    grpby_no_copy = df.groupby('cat1').apply(f_no_copy)
tm.assert_series_equal(grpby_copy, grpby_no_copy)
```

## Next Steps


---

*Source: test_apply_mutate.py:29 | Complexity: Advanced | Last updated: 2026-06-02*