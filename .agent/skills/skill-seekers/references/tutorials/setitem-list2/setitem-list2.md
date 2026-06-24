# How To: Setitem List2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem list2

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `decimal`
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(0, index=range(3), columns=['tt1', 'tt2'], dtype=int)
```

### Step 2: Assign unknown = value

```python
df.loc[1, ['tt1', 'tt2']] = [1, 2]
```

### Step 3: Assign result = value

```python
result = df.loc[df.index[1], ['tt1', 'tt2']]
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 2], df.columns, dtype=int, name=1)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign unknown, unknown = '0'

```python
df['tt1'] = df['tt2'] = '0'
```

### Step 7: Assign unknown = value

```python
df.loc[df.index[1], ['tt1', 'tt2']] = ['1', '2']
```

### Step 8: Assign result = value

```python
result = df.loc[df.index[1], ['tt1', 'tt2']]
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(['1', '2'], df.columns, name=1)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(0, index=range(3), columns=['tt1', 'tt2'], dtype=int)
df.loc[1, ['tt1', 'tt2']] = [1, 2]
result = df.loc[df.index[1], ['tt1', 'tt2']]
expected = Series([1, 2], df.columns, dtype=int, name=1)
tm.assert_series_equal(result, expected)
df['tt1'] = df['tt2'] = '0'
df.loc[df.index[1], ['tt1', 'tt2']] = ['1', '2']
result = df.loc[df.index[1], ['tt1', 'tt2']]
expected = Series(['1', '2'], df.columns, name=1)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:112 | Complexity: Advanced | Last updated: 2026-06-02*