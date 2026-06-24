# How To: Clip Mixed Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clip mixed numeric

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, 3], 'B': [1.0, np.nan, 3.0]})
```

### Step 2: Assign result = df.clip(...)

```python
result = df.clip(1, 2)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 2, 2], 'B': [1.0, np.nan, 2.0]})
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3.4], [3, 4, 5.6]], columns=['foo', 'bar', 'baz'])
```

### Step 6: Assign expected = value

```python
expected = df.dtypes
```

### Step 7: Assign result = value

```python
result = df.clip(upper=3).dtypes
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2, 3], 'B': [1.0, np.nan, 3.0]})
result = df.clip(1, 2)
expected = DataFrame({'A': [1, 2, 2], 'B': [1.0, np.nan, 2.0]})
tm.assert_frame_equal(result, expected)
df = DataFrame([[1, 2, 3.4], [3, 4, 5.6]], columns=['foo', 'bar', 'baz'])
expected = df.dtypes
result = df.clip(upper=3).dtypes
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_clip.py:46 | Complexity: Advanced | Last updated: 2026-06-02*