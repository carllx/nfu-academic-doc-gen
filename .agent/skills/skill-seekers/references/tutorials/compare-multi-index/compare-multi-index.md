# How To: Compare Multi Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare multi index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: align_axis
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]})
```

### Step 2: Assign df.columns = pd.MultiIndex.from_arrays(...)

```python
df.columns = pd.MultiIndex.from_arrays([['a', 'a', 'b'], ['col1', 'col2', 'col3']])
```

### Step 3: Assign df.index = pd.MultiIndex.from_arrays(...)

```python
df.index = pd.MultiIndex.from_arrays([['x', 'x', 'y'], [0, 1, 2]])
```

### Step 4: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 5: Assign unknown = 'c'

```python
df2.iloc[0, 0] = 'c'
```

### Step 6: Assign unknown = 4.0

```python
df2.iloc[2, 2] = 4.0
```

### Step 7: Assign result = df.compare(...)

```python
result = df.compare(df2, align_axis=align_axis)
```

### Step 8: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(data=data, index=indices, columns=columns)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign indices = pd.MultiIndex.from_arrays(...)

```python
indices = pd.MultiIndex.from_arrays([['x', 'x', 'y', 'y'], [0, 0, 2, 2], ['self', 'other', 'self', 'other']])
```

### Step 11: Assign columns = pd.MultiIndex.from_arrays(...)

```python
columns = pd.MultiIndex.from_arrays([['a', 'b'], ['col1', 'col3']])
```

### Step 12: Assign data = value

```python
data = [['a', np.nan], ['c', np.nan], [np.nan, 3.0], [np.nan, 4.0]]
```

### Step 13: Assign indices = pd.MultiIndex.from_arrays(...)

```python
indices = pd.MultiIndex.from_arrays([['x', 'y'], [0, 2]])
```

### Step 14: Assign columns = pd.MultiIndex.from_arrays(...)

```python
columns = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], ['col1', 'col1', 'col3', 'col3'], ['self', 'other', 'self', 'other']])
```

### Step 15: Assign data = value

```python
data = [['a', 'c', np.nan, np.nan], [np.nan, np.nan, 3.0, 4.0]]
```


## Complete Example

```python
# Setup
# Fixtures: align_axis

# Workflow
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]})
df.columns = pd.MultiIndex.from_arrays([['a', 'a', 'b'], ['col1', 'col2', 'col3']])
df.index = pd.MultiIndex.from_arrays([['x', 'x', 'y'], [0, 1, 2]])
df2 = df.copy()
df2.iloc[0, 0] = 'c'
df2.iloc[2, 2] = 4.0
result = df.compare(df2, align_axis=align_axis)
if align_axis == 0:
    indices = pd.MultiIndex.from_arrays([['x', 'x', 'y', 'y'], [0, 0, 2, 2], ['self', 'other', 'self', 'other']])
    columns = pd.MultiIndex.from_arrays([['a', 'b'], ['col1', 'col3']])
    data = [['a', np.nan], ['c', np.nan], [np.nan, 3.0], [np.nan, 4.0]]
else:
    indices = pd.MultiIndex.from_arrays([['x', 'y'], [0, 2]])
    columns = pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], ['col1', 'col1', 'col3', 'col3'], ['self', 'other', 'self', 'other']])
    data = [['a', 'c', np.nan, np.nan], [np.nan, np.nan, 3.0, 4.0]]
expected = pd.DataFrame(data=data, index=indices, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:137 | Complexity: Advanced | Last updated: 2026-06-02*