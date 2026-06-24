# How To: Round With Duplicate Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test round with duplicate columns

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random([3, 3]), columns=['A', 'B', 'C'], index=['first', 'second', 'third'])
```

### Step 2: Assign dfs = pd.concat(...)

```python
dfs = pd.concat((df, df), axis=1)
```

### Step 3: Assign rounded = dfs.round(...)

```python
rounded = dfs.round()
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rounded.index, dfs.index)
```

### Step 5: Assign decimals = Series(...)

```python
decimals = Series([1, 0, 2], index=['A', 'B', 'A'])
```

### Step 6: Assign msg = 'Index of decimals must be unique'

```python
msg = 'Index of decimals must be unique'
```

### Step 7: Call df.round()

```python
df.round(decimals)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).random([3, 3]), columns=['A', 'B', 'C'], index=['first', 'second', 'third'])
dfs = pd.concat((df, df), axis=1)
rounded = dfs.round()
tm.assert_index_equal(rounded.index, dfs.index)
decimals = Series([1, 0, 2], index=['A', 'B', 'A'])
msg = 'Index of decimals must be unique'
with pytest.raises(ValueError, match=msg):
    df.round(decimals)
```

## Next Steps


---

*Source: test_round.py:169 | Complexity: Intermediate | Last updated: 2026-06-02*