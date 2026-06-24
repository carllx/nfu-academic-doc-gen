# How To: Compare With Non Equal Nulls

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare with non equal nulls

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

### Step 4: Assign unknown = value

```python
df2.loc[2, 'col3'] = np.nan
```

### Step 5: Assign result = df.compare(...)

```python
result = df.compare(df2)
```

### Step 6: Assign indices = pd.Index(...)

```python
indices = pd.Index([0, 2])
```

### Step 7: Assign columns = pd.MultiIndex.from_product(...)

```python
columns = pd.MultiIndex.from_product([['col1', 'col3'], ['self', 'other']])
```

### Step 8: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['a', 'c', np.nan, np.nan], [np.nan, np.nan, 3.0, np.nan]], index=indices, columns=columns)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
df2 = df.copy()
df2.loc[0, 'col1'] = 'c'
df2.loc[2, 'col3'] = np.nan
result = df.compare(df2)
indices = pd.Index([0, 2])
columns = pd.MultiIndex.from_product([['col1', 'col3'], ['self', 'other']])
expected = pd.DataFrame([['a', 'c', np.nan, np.nan], [np.nan, np.nan, 3.0, np.nan]], index=indices, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:113 | Complexity: Advanced | Last updated: 2026-06-02*