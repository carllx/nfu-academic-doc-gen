# How To: Compare With Equal Nulls

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare with equal nulls

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
```

### Step 2: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 3: Assign unknown = 'c'

```python
df2.loc[0, 'col1'] = 'c'
```

### Step 4: Assign result = df.compare(...)

```python
result = df.compare(df2)
```

### Step 5: Assign indices = pd.Index(...)

```python
indices = pd.Index([0])
```

### Step 6: Assign columns = pd.MultiIndex.from_product(...)

```python
columns = pd.MultiIndex.from_product([['col1'], ['self', 'other']])
```

### Step 7: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['a', 'c']], index=indices, columns=columns)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
df2 = df.copy()
df2.loc[0, 'col1'] = 'c'
result = df.compare(df2)
indices = pd.Index([0])
columns = pd.MultiIndex.from_product([['col1'], ['self', 'other']])
expected = pd.DataFrame([['a', 'c']], index=indices, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:96 | Complexity: Advanced | Last updated: 2026-06-02*