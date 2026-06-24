# How To: Series Groupby Value Counts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series groupby value counts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: seed_nans, num_rows, max_int, keys, bins, isort, normalize, name, sort, ascending, dropna
```

## Step-by-Step Guide

### Step 1: Assign df = seed_df(...)

```python
df = seed_df(seed_nans, num_rows, max_int)
```

### Step 2: Assign kwargs = value

```python
kwargs = {'normalize': normalize, 'sort': sort, 'ascending': ascending, 'dropna': dropna, 'bins': bins}
```

### Step 3: Assign gr = df.groupby(...)

```python
gr = df.groupby(keys, sort=isort)
```

### Step 4: Assign left = unknown.value_counts(...)

```python
left = gr['3rd'].value_counts(**kwargs)
```

### Step 5: Assign gr = df.groupby(...)

```python
gr = df.groupby(keys, sort=isort)
```

### Step 6: Assign right = unknown.apply(...)

```python
right = gr['3rd'].apply(Series.value_counts, **kwargs)
```

### Step 7: Assign right.index.names = value

```python
right.index.names = right.index.names[:-1] + ['3rd']
```

### Step 8: Assign right = right.rename(...)

```python
right = right.rename(name)
```

### Step 9: Assign unknown = map(...)

```python
left, right = map(rebuild_index, (left, right))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(left.sort_index(), right.sort_index())
```

### Step 11: Assign arr = list(...)

```python
arr = list(map(df.index.get_level_values, range(df.index.nlevels)))
```

### Step 12: Assign df.index = MultiIndex.from_arrays(...)

```python
df.index = MultiIndex.from_arrays(arr, names=df.index.names)
```


## Complete Example

```python
# Setup
# Fixtures: seed_nans, num_rows, max_int, keys, bins, isort, normalize, name, sort, ascending, dropna

# Workflow
df = seed_df(seed_nans, num_rows, max_int)

def rebuild_index(df):
    arr = list(map(df.index.get_level_values, range(df.index.nlevels)))
    df.index = MultiIndex.from_arrays(arr, names=df.index.names)
    return df
kwargs = {'normalize': normalize, 'sort': sort, 'ascending': ascending, 'dropna': dropna, 'bins': bins}
gr = df.groupby(keys, sort=isort)
left = gr['3rd'].value_counts(**kwargs)
gr = df.groupby(keys, sort=isort)
right = gr['3rd'].apply(Series.value_counts, **kwargs)
right.index.names = right.index.names[:-1] + ['3rd']
right = right.rename(name)
left, right = map(rebuild_index, (left, right))
tm.assert_series_equal(left.sort_index(), right.sort_index())
```

## Next Steps


---

*Source: test_value_counts.py:80 | Complexity: Advanced | Last updated: 2026-06-02*