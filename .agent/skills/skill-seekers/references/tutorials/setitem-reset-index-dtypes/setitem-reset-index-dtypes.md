# How To: Setitem Reset Index Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem reset index dtypes

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame.astype(...)

```python
df = DataFrame(columns=['a', 'b', 'c']).astype({'a': 'datetime64[ns]', 'b': np.int64, 'c': np.float64})
```

### Step 2: Assign df1 = df.set_index(...)

```python
df1 = df.set_index(['a'])
```

### Step 3: Assign unknown = value

```python
df1['d'] = []
```

### Step 4: Assign result = df1.reset_index(...)

```python
result = df1.reset_index()
```

### Step 5: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame(columns=['a', 'b', 'c', 'd'], index=range(0)).astype({'a': 'datetime64[ns]', 'b': np.int64, 'c': np.float64, 'd': np.float64})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign df2 = df.set_index(...)

```python
df2 = df.set_index(['a', 'b'])
```

### Step 8: Assign unknown = value

```python
df2['d'] = []
```

### Step 9: Assign result = df2.reset_index(...)

```python
result = df2.reset_index()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(columns=['a', 'b', 'c']).astype({'a': 'datetime64[ns]', 'b': np.int64, 'c': np.float64})
df1 = df.set_index(['a'])
df1['d'] = []
result = df1.reset_index()
expected = DataFrame(columns=['a', 'b', 'c', 'd'], index=range(0)).astype({'a': 'datetime64[ns]', 'b': np.int64, 'c': np.float64, 'd': np.float64})
tm.assert_frame_equal(result, expected)
df2 = df.set_index(['a', 'b'])
df2['d'] = []
result = df2.reset_index()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:72 | Complexity: Advanced | Last updated: 2026-06-02*