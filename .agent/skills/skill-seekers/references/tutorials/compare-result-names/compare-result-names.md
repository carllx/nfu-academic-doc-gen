# How To: Compare Result Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare result names

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]})
```

### Step 2: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'col1': ['c', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, np.nan]})
```

### Step 3: Assign result = df1.compare(...)

```python
result = df1.compare(df2, result_names=('left', 'right'))
```

### Step 4: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({('col1', 'left'): {0: 'a', 2: np.nan}, ('col1', 'right'): {0: 'c', 2: np.nan}, ('col3', 'left'): {0: np.nan, 2: 3.0}, ('col3', 'right'): {0: np.nan, 2: np.nan}})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, 3.0]})
df2 = pd.DataFrame({'col1': ['c', 'b', 'c'], 'col2': [1.0, 2.0, np.nan], 'col3': [1.0, 2.0, np.nan]})
result = df1.compare(df2, result_names=('left', 'right'))
expected = pd.DataFrame({('col1', 'left'): {0: 'a', 2: np.nan}, ('col1', 'right'): {0: 'c', 2: np.nan}, ('col3', 'left'): {0: np.nan, 2: 3.0}, ('col3', 'right'): {0: np.nan, 2: np.nan}})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*