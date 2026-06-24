# How To: Subclassed Wide To Long

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subclassed wide to long

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign x = np.random.default_rng.standard_normal(...)

```python
x = np.random.default_rng(2).standard_normal(3)
```

### Step 2: Assign df = tm.SubclassedDataFrame(...)

```python
df = tm.SubclassedDataFrame({'A1970': {0: 'a', 1: 'b', 2: 'c'}, 'A1980': {0: 'd', 1: 'e', 2: 'f'}, 'B1970': {0: 2.5, 1: 1.2, 2: 0.7}, 'B1980': {0: 3.2, 1: 1.3, 2: 0.1}, 'X': dict(zip(range(3), x))})
```

### Step 3: Assign unknown = value

```python
df['id'] = df.index
```

### Step 4: Assign exp_data = value

```python
exp_data = {'X': x.tolist() + x.tolist(), 'A': ['a', 'b', 'c', 'd', 'e', 'f'], 'B': [2.5, 1.2, 0.7, 3.2, 1.3, 0.1], 'year': [1970, 1970, 1970, 1980, 1980, 1980], 'id': [0, 1, 2, 0, 1, 2]}
```

### Step 5: Assign expected = tm.SubclassedDataFrame(...)

```python
expected = tm.SubclassedDataFrame(exp_data)
```

### Step 6: Assign expected = value

```python
expected = expected.set_index(['id', 'year'])[['X', 'A', 'B']]
```

### Step 7: Assign long_frame = pd.wide_to_long(...)

```python
long_frame = pd.wide_to_long(df, ['A', 'B'], i='id', j='year')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(long_frame, expected)
```


## Complete Example

```python
# Workflow
x = np.random.default_rng(2).standard_normal(3)
df = tm.SubclassedDataFrame({'A1970': {0: 'a', 1: 'b', 2: 'c'}, 'A1980': {0: 'd', 1: 'e', 2: 'f'}, 'B1970': {0: 2.5, 1: 1.2, 2: 0.7}, 'B1980': {0: 3.2, 1: 1.3, 2: 0.1}, 'X': dict(zip(range(3), x))})
df['id'] = df.index
exp_data = {'X': x.tolist() + x.tolist(), 'A': ['a', 'b', 'c', 'd', 'e', 'f'], 'B': [2.5, 1.2, 0.7, 3.2, 1.3, 0.1], 'year': [1970, 1970, 1970, 1980, 1980, 1980], 'id': [0, 1, 2, 0, 1, 2]}
expected = tm.SubclassedDataFrame(exp_data)
expected = expected.set_index(['id', 'year'])[['X', 'A', 'B']]
long_frame = pd.wide_to_long(df, ['A', 'B'], i='id', j='year')
tm.assert_frame_equal(long_frame, expected)
```

## Next Steps


---

*Source: test_subclass.py:510 | Complexity: Advanced | Last updated: 2026-06-02*