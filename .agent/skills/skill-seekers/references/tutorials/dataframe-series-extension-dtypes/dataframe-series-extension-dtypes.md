# How To: Dataframe Series Extension Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe series extension dtypes

## Prerequisites

**Required Modules:**
- `collections`
- `datetime`
- `enum`
- `functools`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.computation`
- `pandas.tests.frame.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(0, 100, (10, 3)), columns=['a', 'b', 'c'])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], index=['a', 'b', 'c'])
```

### Step 3: Assign expected = value

```python
expected = df.to_numpy('int64') + ser.to_numpy('int64').reshape(-1, 3)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected, columns=df.columns, dtype='Int64')
```

### Step 5: Assign df_ea = df.astype(...)

```python
df_ea = df.astype('Int64')
```

### Step 6: Assign result = value

```python
result = df_ea + ser
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = value

```python
result = df_ea + ser.astype('Int64')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).integers(0, 100, (10, 3)), columns=['a', 'b', 'c'])
ser = Series([1, 2, 3], index=['a', 'b', 'c'])
expected = df.to_numpy('int64') + ser.to_numpy('int64').reshape(-1, 3)
expected = DataFrame(expected, columns=df.columns, dtype='Int64')
df_ea = df.astype('Int64')
result = df_ea + ser
tm.assert_frame_equal(result, expected)
result = df_ea + ser.astype('Int64')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:1940 | Complexity: Advanced | Last updated: 2026-06-02*