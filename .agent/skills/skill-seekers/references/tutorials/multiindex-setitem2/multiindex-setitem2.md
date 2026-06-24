# How To: Multiindex Setitem2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex setitem2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df_orig = DataFrame.from_dict(...)

```python
df_orig = DataFrame.from_dict({'price': {('DE', 'Coal', 'Stock'): 2, ('DE', 'Gas', 'Stock'): 4, ('DE', 'Elec', 'Demand'): 1, ('FR', 'Gas', 'Stock'): 5, ('FR', 'Solar', 'SupIm'): 0, ('FR', 'Wind', 'SupIm'): 0}})
```

### Step 2: Assign df_orig.index = MultiIndex.from_tuples(...)

```python
df_orig.index = MultiIndex.from_tuples(df_orig.index, names=['Sit', 'Com', 'Type'])
```

### Step 3: Assign expected = df_orig.copy(...)

```python
expected = df_orig.copy()
```

### Step 4: Assign idx = value

```python
idx = pd.IndexSlice
```

### Step 5: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign df = df_orig.copy(...)

```python
df = df_orig.copy()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df_orig = DataFrame.from_dict({'price': {('DE', 'Coal', 'Stock'): 2, ('DE', 'Gas', 'Stock'): 4, ('DE', 'Elec', 'Demand'): 1, ('FR', 'Gas', 'Stock'): 5, ('FR', 'Solar', 'SupIm'): 0, ('FR', 'Wind', 'SupIm'): 0}})
df_orig.index = MultiIndex.from_tuples(df_orig.index, names=['Sit', 'Com', 'Type'])
expected = df_orig.copy()
expected.iloc[[0, 1, 3]] *= 2
idx = pd.IndexSlice
df = df_orig.copy()
df.loc[idx[:, :, 'Stock'], :] *= 2
tm.assert_frame_equal(df, expected)
df = df_orig.copy()
df.loc[idx[:, :, 'Stock'], 'price'] *= 2
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_setitem.py:157 | Complexity: Advanced | Last updated: 2026-06-02*