# How To: Compare Various Formats

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare various formats

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
# Fixtures: keep_shape, keep_equal
```

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

### Step 4: Assign unknown = 4.0

```python
df2.loc[2, 'col3'] = 4.0
```

### Step 5: Assign result = df.compare(...)

```python
result = df.compare(df2, keep_shape=keep_shape, keep_equal=keep_equal)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign indices = pd.Index(...)

```python
indices = pd.Index([0, 1, 2])
```

### Step 8: Assign columns = pd.MultiIndex.from_product(...)

```python
columns = pd.MultiIndex.from_product([['col1', 'col2', 'col3'], ['self', 'other']])
```

### Step 9: Assign indices = pd.Index(...)

```python
indices = pd.Index([0, 2])
```

### Step 10: Assign columns = pd.MultiIndex.from_product(...)

```python
columns = pd.MultiIndex.from_product([['col1', 'col3'], ['self', 'other']])
```

### Step 11: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['a', 'c', 1.0, 1.0], ['c', 'c', 3.0, 4.0]], index=indices, columns=columns)
```

### Step 12: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['a', 'c', 1.0, 1.0, 1.0, 1.0], ['b', 'b', 2.0, 2.0, 2.0, 2.0], ['c', 'c', np.nan, np.nan, 3.0, 4.0]], index=indices, columns=columns)
```

### Step 13: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([['a', 'c', np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan, 3.0, 4.0]], index=indices, columns=columns)
```


## Complete Example

```python
# Setup
# Fixtures: keep_shape, keep_equal

# Workflow
df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]}, columns=['col1', 'col2', 'col3'])
df2 = df.copy()
df2.loc[0, 'col1'] = 'c'
df2.loc[2, 'col3'] = 4.0
result = df.compare(df2, keep_shape=keep_shape, keep_equal=keep_equal)
if keep_shape:
    indices = pd.Index([0, 1, 2])
    columns = pd.MultiIndex.from_product([['col1', 'col2', 'col3'], ['self', 'other']])
    if keep_equal:
        expected = pd.DataFrame([['a', 'c', 1.0, 1.0, 1.0, 1.0], ['b', 'b', 2.0, 2.0, 2.0, 2.0], ['c', 'c', np.nan, np.nan, 3.0, 4.0]], index=indices, columns=columns)
    else:
        expected = pd.DataFrame([['a', 'c', np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan, np.nan, 3.0, 4.0]], index=indices, columns=columns)
else:
    indices = pd.Index([0, 2])
    columns = pd.MultiIndex.from_product([['col1', 'col3'], ['self', 'other']])
    expected = pd.DataFrame([['a', 'c', 1.0, 1.0], ['c', 'c', 3.0, 4.0]], index=indices, columns=columns)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:51 | Complexity: Advanced | Last updated: 2026-06-02*