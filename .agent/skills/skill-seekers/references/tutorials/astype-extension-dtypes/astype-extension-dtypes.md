# How To: Astype Extension Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype extension dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], columns=['a', 'b'])
```

### Step 2: Assign expected1 = DataFrame(...)

```python
expected1 = DataFrame({'a': pd.array([1, 3, 5], dtype=dtype), 'b': pd.array([2, 4, 6], dtype=dtype)})
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.astype(dtype), expected1)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.astype('int64').astype(dtype), expected1)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.astype(dtype).astype('float64'), df)
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], columns=['a', 'b'])
```

### Step 7: Assign unknown = unknown.astype(...)

```python
df['b'] = df['b'].astype(dtype)
```

### Step 8: Assign expected2 = DataFrame(...)

```python
expected2 = DataFrame({'a': [1.0, 3.0, 5.0], 'b': pd.array([2, 4, 6], dtype=dtype)})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected2)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.astype(dtype), expected1)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df.astype('int64').astype(dtype), expected1)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
df = DataFrame([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], columns=['a', 'b'])
expected1 = DataFrame({'a': pd.array([1, 3, 5], dtype=dtype), 'b': pd.array([2, 4, 6], dtype=dtype)})
tm.assert_frame_equal(df.astype(dtype), expected1)
tm.assert_frame_equal(df.astype('int64').astype(dtype), expected1)
tm.assert_frame_equal(df.astype(dtype).astype('float64'), df)
df = DataFrame([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], columns=['a', 'b'])
df['b'] = df['b'].astype(dtype)
expected2 = DataFrame({'a': [1.0, 3.0, 5.0], 'b': pd.array([2, 4, 6], dtype=dtype)})
tm.assert_frame_equal(df, expected2)
tm.assert_frame_equal(df.astype(dtype), expected1)
tm.assert_frame_equal(df.astype('int64').astype(dtype), expected1)
```

## Next Steps


---

*Source: test_astype.py:329 | Complexity: Advanced | Last updated: 2026-06-02*