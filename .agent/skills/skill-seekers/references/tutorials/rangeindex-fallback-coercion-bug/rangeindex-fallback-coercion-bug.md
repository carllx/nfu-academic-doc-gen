# How To: Rangeindex Fallback Coercion Bug

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rangeindex fallback coercion bug

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame(np.arange(100).reshape((10, 10)))
```

### Step 2: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame(np.arange(100).reshape((10, 10)))
```

### Step 3: Assign df = pd.concat(...)

```python
df = pd.concat({'df1': df1.stack(future_stack=True), 'df2': df2.stack(future_stack=True)}, axis=1)
```

### Step 4: Assign df.index.names = value

```python
df.index.names = ['fizz', 'buzz']
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'df2': np.arange(100), 'df1': np.arange(100)}, index=MultiIndex.from_product([range(10), range(10)], names=['fizz', 'buzz']))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected, check_like=True)
```

### Step 7: Assign result = df.index.get_level_values(...)

```python
result = df.index.get_level_values('fizz')
```

### Step 8: Assign expected = Index.repeat(...)

```python
expected = Index(np.arange(10, dtype=np.int64), name='fizz').repeat(10)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign result = df.index.get_level_values(...)

```python
result = df.index.get_level_values('buzz')
```

### Step 11: Assign expected = Index(...)

```python
expected = Index(np.tile(np.arange(10, dtype=np.int64), 10), name='buzz')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = pd.DataFrame(np.arange(100).reshape((10, 10)))
df2 = pd.DataFrame(np.arange(100).reshape((10, 10)))
df = pd.concat({'df1': df1.stack(future_stack=True), 'df2': df2.stack(future_stack=True)}, axis=1)
df.index.names = ['fizz', 'buzz']
expected = pd.DataFrame({'df2': np.arange(100), 'df1': np.arange(100)}, index=MultiIndex.from_product([range(10), range(10)], names=['fizz', 'buzz']))
tm.assert_frame_equal(df, expected, check_like=True)
result = df.index.get_level_values('fizz')
expected = Index(np.arange(10, dtype=np.int64), name='fizz').repeat(10)
tm.assert_index_equal(result, expected)
result = df.index.get_level_values('buzz')
expected = Index(np.tile(np.arange(10, dtype=np.int64), 10), name='buzz')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_integrity.py:243 | Complexity: Advanced | Last updated: 2026-06-02*