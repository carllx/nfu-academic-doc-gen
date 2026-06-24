# How To: Diff Axis1 Mixed Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test diff axis1 mixed dtypes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': range(3), 'B': 2 * np.arange(3, dtype=np.float64)})
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [np.nan, np.nan, np.nan], 'B': df['B'] / 2})
```

### Step 3: Assign result = df.diff(...)

```python
result = df.diff(axis=1)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'a': np.arange(3, dtype='float32'), 'b': np.arange(3, dtype='float64')})
```

### Step 6: Assign result = df.diff(...)

```python
result = df.diff(axis=1)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': df['a'] * np.nan, 'b': df['b'] * 0})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': range(3), 'B': 2 * np.arange(3, dtype=np.float64)})
expected = DataFrame({'A': [np.nan, np.nan, np.nan], 'B': df['B'] / 2})
result = df.diff(axis=1)
tm.assert_frame_equal(result, expected)
df = DataFrame({'a': np.arange(3, dtype='float32'), 'b': np.arange(3, dtype='float64')})
result = df.diff(axis=1)
expected = DataFrame({'a': df['a'] * np.nan, 'b': df['b'] * 0})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_diff.py:199 | Complexity: Advanced | Last updated: 2026-06-02*