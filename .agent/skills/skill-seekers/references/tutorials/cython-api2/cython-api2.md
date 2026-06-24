# How To: Cython Api2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython api2

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Required Fixtures:**
- `api_client` fixture


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, np.nan], [1, np.nan, 9], [3, 4, 9]], columns=['A', 'B', 'C'])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, np.nan], [np.nan, 9], [4, 9]], columns=['B', 'C'])
```

### Step 3: Assign result = df.groupby.cumsum(...)

```python
result = df.groupby('A').cumsum()
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.groupby.cumsum(...)

```python
result = df.groupby('A', as_index=False).cumsum()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign msg = 'DataFrameGroupBy.cumsum with axis=1 is deprecated'

```python
msg = 'DataFrameGroupBy.cumsum with axis=1 is deprecated'
```

### Step 8: Assign expected = df.cumsum(...)

```python
expected = df.cumsum(axis=1)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign msg = 'DataFrameGroupBy.cumprod with axis=1 is deprecated'

```python
msg = 'DataFrameGroupBy.cumprod with axis=1 is deprecated'
```

### Step 11: Assign expected = df.cumprod(...)

```python
expected = df.cumprod(axis=1)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = df.groupby.cumsum(...)

```python
result = df.groupby('A').cumsum(axis=1)
```

### Step 14: Assign result = df.groupby.cumprod(...)

```python
result = df.groupby('A').cumprod(axis=1)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, np.nan], [1, np.nan, 9], [3, 4, 9]], columns=['A', 'B', 'C'])
expected = DataFrame([[2, np.nan], [np.nan, 9], [4, 9]], columns=['B', 'C'])
result = df.groupby('A').cumsum()
tm.assert_frame_equal(result, expected)
result = df.groupby('A', as_index=False).cumsum()
tm.assert_frame_equal(result, expected)
msg = 'DataFrameGroupBy.cumsum with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('A').cumsum(axis=1)
expected = df.cumsum(axis=1)
tm.assert_frame_equal(result, expected)
msg = 'DataFrameGroupBy.cumprod with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.groupby('A').cumprod(axis=1)
expected = df.cumprod(axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:295 | Complexity: Advanced | Last updated: 2026-06-02*