# How To: Rename Axis Style

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename axis style

## Prerequisites

**Required Modules:**
- `collections`
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2], 'B': [1, 2]}, index=['X', 'Y'])
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2], 'b': [1, 2]}, index=['X', 'Y'])
```

### Step 3: Assign result = df.rename(...)

```python
result = df.rename(str.lower, axis=1)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.rename(...)

```python
result = df.rename(str.lower, axis='columns')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = df.rename(...)

```python
result = df.rename({'A': 'a', 'B': 'b'}, axis=1)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.rename(...)

```python
result = df.rename({'A': 'a', 'B': 'b'}, axis='columns')
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1, 2], 'B': [1, 2]}, index=['x', 'y'])
```

### Step 12: Assign result = df.rename(...)

```python
result = df.rename(str.lower, axis=0)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = df.rename(...)

```python
result = df.rename(str.lower, axis='index')
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign result = df.rename(...)

```python
result = df.rename({'X': 'x', 'Y': 'y'}, axis=0)
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 18: Assign result = df.rename(...)

```python
result = df.rename({'X': 'x', 'Y': 'y'}, axis='index')
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 20: Assign result = df.rename(...)

```python
result = df.rename(mapper=str.lower, axis='index')
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2], 'B': [1, 2]}, index=['X', 'Y'])
expected = DataFrame({'a': [1, 2], 'b': [1, 2]}, index=['X', 'Y'])
result = df.rename(str.lower, axis=1)
tm.assert_frame_equal(result, expected)
result = df.rename(str.lower, axis='columns')
tm.assert_frame_equal(result, expected)
result = df.rename({'A': 'a', 'B': 'b'}, axis=1)
tm.assert_frame_equal(result, expected)
result = df.rename({'A': 'a', 'B': 'b'}, axis='columns')
tm.assert_frame_equal(result, expected)
expected = DataFrame({'A': [1, 2], 'B': [1, 2]}, index=['x', 'y'])
result = df.rename(str.lower, axis=0)
tm.assert_frame_equal(result, expected)
result = df.rename(str.lower, axis='index')
tm.assert_frame_equal(result, expected)
result = df.rename({'X': 'x', 'Y': 'y'}, axis=0)
tm.assert_frame_equal(result, expected)
result = df.rename({'X': 'x', 'Y': 'y'}, axis='index')
tm.assert_frame_equal(result, expected)
result = df.rename(mapper=str.lower, axis='index')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rename.py:250 | Complexity: Advanced | Last updated: 2026-06-02*