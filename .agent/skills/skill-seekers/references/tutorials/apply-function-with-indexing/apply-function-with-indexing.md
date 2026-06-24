# How To: Apply Function With Indexing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply function with indexing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'col1': ['A', 'A', 'A', 'B', 'B', 'B'], 'col2': [1, 2, 3, 4, 5, 6]})
```

### Step 2: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([1, 2, 0, 4, 5, 0], index=pd.MultiIndex.from_tuples([(0, 0), (0, 1), (0, 2), (1, 3), (1, 4), (1, 5)]), name='col2')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign unknown = 0

```python
x.loc[x.index[-1], 'col2'] = 0
```

### Step 6: Assign result = df.groupby.apply(...)

```python
result = df.groupby(['col1'], as_index=False).apply(fn)
```


## Complete Example

```python
# Setup
# Fixtures: warn_copy_on_write

# Workflow
df = pd.DataFrame({'col1': ['A', 'A', 'A', 'B', 'B', 'B'], 'col2': [1, 2, 3, 4, 5, 6]})

def fn(x):
    x.loc[x.index[-1], 'col2'] = 0
    return x.col2
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg, raise_on_extra_warnings=not warn_copy_on_write):
    result = df.groupby(['col1'], as_index=False).apply(fn)
expected = pd.Series([1, 2, 0, 4, 5, 0], index=pd.MultiIndex.from_tuples([(0, 0), (0, 1), (0, 2), (1, 3), (1, 4), (1, 5)]), name='col2')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_apply_mutate.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*