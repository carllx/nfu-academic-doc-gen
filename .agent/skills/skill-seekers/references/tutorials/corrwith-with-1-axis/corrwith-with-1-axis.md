# How To: Corrwith With 1 Axis

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test corrwith with 1 axis

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, 2], 'b': [3, 7, 4]})
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('a')
```

### Step 3: Assign msg = 'DataFrameGroupBy.corrwith with axis=1 is deprecated'

```python
msg = 'DataFrameGroupBy.corrwith with axis=1 is deprecated'
```

### Step 4: Assign index = Index(...)

```python
index = Index(data=[(1, 0), (1, 1), (1, 2), (2, 2), (2, 0), (2, 1)], name=('a', None))
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.nan] * 6, index=index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = gb.corrwith(...)

```python
result = gb.corrwith(df, axis=1)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, 2], 'b': [3, 7, 4]})
gb = df.groupby('a')
msg = 'DataFrameGroupBy.corrwith with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = gb.corrwith(df, axis=1)
index = Index(data=[(1, 0), (1, 1), (1, 2), (2, 2), (2, 0), (2, 1)], name=('a', None))
expected = Series([np.nan] * 6, index=index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_corrwith.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*