# How To: Crosstab Margins

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test crosstab margins

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.random.default_rng.integers(...)

```python
a = np.random.default_rng(2).integers(0, 7, size=100)
```

**Verification:**
```python
assert result.index.names == ('a',)
```

### Step 2: Assign b = np.random.default_rng.integers(...)

```python
b = np.random.default_rng(2).integers(0, 3, size=100)
```

**Verification:**
```python
assert result.columns.names == ['b', 'c']
```

### Step 3: Assign c = np.random.default_rng.integers(...)

```python
c = np.random.default_rng(2).integers(0, 5, size=100)
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'a': a, 'b': b, 'c': c})
```

### Step 5: Assign result = crosstab(...)

```python
result = crosstab(a, [b, c], rownames=['a'], colnames=('b', 'c'), margins=True)
```

**Verification:**
```python
assert result.index.names == ('a',)
```

### Step 6: Assign all_cols = value

```python
all_cols = result['All', '']
```

### Step 7: Assign exp_cols = df.groupby.size.astype(...)

```python
exp_cols = df.groupby(['a']).size().astype('i8')
```

### Step 8: Assign exp_margin = Series(...)

```python
exp_margin = Series([len(df)], index=Index(['All'], name='a'))
```

### Step 9: Assign exp_cols = pd.concat(...)

```python
exp_cols = pd.concat([exp_cols, exp_margin])
```

### Step 10: Assign exp_cols.name = value

```python
exp_cols.name = ('All', '')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(all_cols, exp_cols)
```

### Step 12: Assign all_rows = value

```python
all_rows = result.loc['All']
```

### Step 13: Assign exp_rows = df.groupby.size.astype(...)

```python
exp_rows = df.groupby(['b', 'c']).size().astype('i8')
```

### Step 14: Assign exp_rows = pd.concat(...)

```python
exp_rows = pd.concat([exp_rows, Series([len(df)], index=[('All', '')])])
```

### Step 15: Assign exp_rows.name = 'All'

```python
exp_rows.name = 'All'
```

### Step 16: Assign exp_rows = exp_rows.reindex(...)

```python
exp_rows = exp_rows.reindex(all_rows.index)
```

### Step 17: Assign exp_rows = exp_rows.fillna.astype(...)

```python
exp_rows = exp_rows.fillna(0).astype(np.int64)
```

### Step 18: Call tm.assert_series_equal()

```python
tm.assert_series_equal(all_rows, exp_rows)
```


## Complete Example

```python
# Workflow
a = np.random.default_rng(2).integers(0, 7, size=100)
b = np.random.default_rng(2).integers(0, 3, size=100)
c = np.random.default_rng(2).integers(0, 5, size=100)
df = DataFrame({'a': a, 'b': b, 'c': c})
result = crosstab(a, [b, c], rownames=['a'], colnames=('b', 'c'), margins=True)
assert result.index.names == ('a',)
assert result.columns.names == ['b', 'c']
all_cols = result['All', '']
exp_cols = df.groupby(['a']).size().astype('i8')
exp_margin = Series([len(df)], index=Index(['All'], name='a'))
exp_cols = pd.concat([exp_cols, exp_margin])
exp_cols.name = ('All', '')
tm.assert_series_equal(all_cols, exp_cols)
all_rows = result.loc['All']
exp_rows = df.groupby(['b', 'c']).size().astype('i8')
exp_rows = pd.concat([exp_rows, Series([len(df)], index=[('All', '')])])
exp_rows.name = 'All'
exp_rows = exp_rows.reindex(all_rows.index)
exp_rows = exp_rows.fillna(0).astype(np.int64)
tm.assert_series_equal(all_rows, exp_rows)
```

## Next Steps


---

*Source: test_crosstab.py:128 | Complexity: Advanced | Last updated: 2026-06-02*