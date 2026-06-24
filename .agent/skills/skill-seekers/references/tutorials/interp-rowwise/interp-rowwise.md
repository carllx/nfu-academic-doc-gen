# How To: Interp Rowwise

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp rowwise

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({0: [1, 2, np.nan, 4], 1: [2, 3, 4, np.nan], 2: [np.nan, 4, 5, 6], 3: [4, np.nan, 6, 7], 4: [1, 2, 3, 4]})
```

### Step 2: Assign result = df.interpolate(...)

```python
result = df.interpolate(axis=1)
```

### Step 3: Assign expected = df.copy(...)

```python
expected = df.copy()
```

### Step 4: Assign unknown = 5

```python
expected.loc[3, 1] = 5
```

### Step 5: Assign unknown = 3

```python
expected.loc[0, 2] = 3
```

### Step 6: Assign unknown = 3

```python
expected.loc[1, 3] = 3
```

### Step 7: Assign unknown = unknown.astype(...)

```python
expected[4] = expected[4].astype(np.float64)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.interpolate(...)

```python
result = df.interpolate(axis=1, method='values')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = df.interpolate(...)

```python
result = df.interpolate(axis=0)
```

### Step 12: Assign expected = df.interpolate(...)

```python
expected = df.interpolate()
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({0: [1, 2, np.nan, 4], 1: [2, 3, 4, np.nan], 2: [np.nan, 4, 5, 6], 3: [4, np.nan, 6, 7], 4: [1, 2, 3, 4]})
result = df.interpolate(axis=1)
expected = df.copy()
expected.loc[3, 1] = 5
expected.loc[0, 2] = 3
expected.loc[1, 3] = 3
expected[4] = expected[4].astype(np.float64)
tm.assert_frame_equal(result, expected)
result = df.interpolate(axis=1, method='values')
tm.assert_frame_equal(result, expected)
result = df.interpolate(axis=0)
expected = df.interpolate()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_interpolate.py:286 | Complexity: Advanced | Last updated: 2026-06-02*