# How To: Groupby Example

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby example

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

### Step 1: Assign NUM_ROWS = 100

```python
NUM_ROWS = 100
```

### Step 2: Assign NUM_COLS = 10

```python
NUM_COLS = 10
```

### Step 3: Assign col_names = value

```python
col_names = ['A' + num for num in map(str, np.arange(NUM_COLS).tolist())]
```

### Step 4: Assign index_cols = value

```python
index_cols = col_names[:5]
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(5, size=(NUM_ROWS, NUM_COLS)), dtype=np.int64, columns=col_names)
```

### Step 6: Assign df = df.set_index.sort_index(...)

```python
df = df.set_index(index_cols).sort_index()
```

### Step 7: Assign grp = df.groupby(...)

```python
grp = df.groupby(level=index_cols[:4])
```

### Step 8: Assign unknown = value

```python
df['new_col'] = np.nan
```

### Step 9: Assign new_vals = np.arange(...)

```python
new_vals = np.arange(df2.shape[0])
```

### Step 10: Assign unknown = new_vals

```python
df.loc[name, 'new_col'] = new_vals
```


## Complete Example

```python
# Workflow
NUM_ROWS = 100
NUM_COLS = 10
col_names = ['A' + num for num in map(str, np.arange(NUM_COLS).tolist())]
index_cols = col_names[:5]
df = DataFrame(np.random.default_rng(2).integers(5, size=(NUM_ROWS, NUM_COLS)), dtype=np.int64, columns=col_names)
df = df.set_index(index_cols).sort_index()
grp = df.groupby(level=index_cols[:4])
df['new_col'] = np.nan
for name, df2 in grp:
    new_vals = np.arange(df2.shape[0])
    df.loc[name, 'new_col'] = new_vals
```

## Next Steps


---

*Source: test_setitem.py:259 | Complexity: Advanced | Last updated: 2026-06-02*