# How To: Pivot Table Dropna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pivot table dropna

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.reshape`
- `pandas.core.reshape.pivot`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'amount': {0: 60000, 1: 100000, 2: 50000, 3: 30000}, 'customer': {0: 'A', 1: 'A', 2: 'B', 3: 'C'}, 'month': {0: 201307, 1: 201309, 2: 201308, 3: 201310}, 'product': {0: 'a', 1: 'b', 2: 'c', 3: 'd'}, 'quantity': {0: 2000000, 1: 500000, 2: 1000000, 3: 1000000}})
```

### Step 2: Assign pv_col = df.pivot_table(...)

```python
pv_col = df.pivot_table('quantity', 'month', ['customer', 'product'], dropna=False)
```

### Step 3: Assign pv_ind = df.pivot_table(...)

```python
pv_ind = df.pivot_table('quantity', ['customer', 'product'], 'month', dropna=False)
```

### Step 4: Assign m = MultiIndex.from_tuples(...)

```python
m = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('A', 'c'), ('A', 'd'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('B', 'd'), ('C', 'a'), ('C', 'b'), ('C', 'c'), ('C', 'd')], names=['customer', 'product'])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pv_col.columns, m)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(pv_ind.index, m)
```


## Complete Example

```python
# Workflow
df = DataFrame({'amount': {0: 60000, 1: 100000, 2: 50000, 3: 30000}, 'customer': {0: 'A', 1: 'A', 2: 'B', 3: 'C'}, 'month': {0: 201307, 1: 201309, 2: 201308, 3: 201310}, 'product': {0: 'a', 1: 'b', 2: 'c', 3: 'd'}, 'quantity': {0: 2000000, 1: 500000, 2: 1000000, 3: 1000000}})
pv_col = df.pivot_table('quantity', 'month', ['customer', 'product'], dropna=False)
pv_ind = df.pivot_table('quantity', ['customer', 'product'], 'month', dropna=False)
m = MultiIndex.from_tuples([('A', 'a'), ('A', 'b'), ('A', 'c'), ('A', 'd'), ('B', 'a'), ('B', 'b'), ('B', 'c'), ('B', 'd'), ('C', 'a'), ('C', 'b'), ('C', 'c'), ('C', 'd')], names=['customer', 'product'])
tm.assert_index_equal(pv_col.columns, m)
tm.assert_index_equal(pv_ind.index, m)
```

## Next Steps


---

*Source: test_pivot.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*