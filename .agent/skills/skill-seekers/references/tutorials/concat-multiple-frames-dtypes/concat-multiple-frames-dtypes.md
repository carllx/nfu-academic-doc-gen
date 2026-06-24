# How To: Concat Multiple Frames Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat multiple frames dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame(data=np.ones((10, 2)), columns=['foo', 'bar'], dtype=np.float64)
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(data=np.ones((10, 2)), dtype=np.float32)
```

### Step 3: Assign results = value

```python
results = concat((df1, df2), axis=1).dtypes
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([np.dtype('float64')] * 2 + [np.dtype('float32')] * 2, index=['foo', 'bar', 0, 1])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(results, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame(data=np.ones((10, 2)), columns=['foo', 'bar'], dtype=np.float64)
df2 = DataFrame(data=np.ones((10, 2)), dtype=np.float32)
results = concat((df1, df2), axis=1).dtypes
expected = Series([np.dtype('float64')] * 2 + [np.dtype('float32')] * 2, index=['foo', 'bar', 0, 1])
tm.assert_series_equal(results, expected)
```

## Next Steps


---

*Source: test_dataframe.py:15 | Complexity: Intermediate | Last updated: 2026-06-02*