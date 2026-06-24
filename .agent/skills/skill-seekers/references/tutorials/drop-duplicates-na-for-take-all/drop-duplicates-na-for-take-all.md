# How To: Drop Duplicates Na For Take All

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates NA for take all

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [None, None, 'foo', 'bar', 'foo', 'baz', 'bar', 'qux'], 'C': [1.0, np.nan, np.nan, np.nan, 1.0, 2.0, 3, 1.0]})
```

### Step 2: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('A')
```

### Step 3: Assign expected = value

```python
expected = df.iloc[[0, 2, 3, 5, 7]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('A', keep='last')
```

### Step 6: Assign expected = value

```python
expected = df.iloc[[1, 4, 5, 6, 7]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('A', keep=False)
```

### Step 9: Assign expected = value

```python
expected = df.iloc[[5, 7]]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('C')
```

### Step 12: Assign expected = value

```python
expected = df.iloc[[0, 1, 5, 6]]
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('C', keep='last')
```

### Step 15: Assign expected = value

```python
expected = df.iloc[[3, 5, 6, 7]]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('C', keep=False)
```

### Step 18: Assign expected = value

```python
expected = df.iloc[[5, 6]]
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [None, None, 'foo', 'bar', 'foo', 'baz', 'bar', 'qux'], 'C': [1.0, np.nan, np.nan, np.nan, 1.0, 2.0, 3, 1.0]})
result = df.drop_duplicates('A')
expected = df.iloc[[0, 2, 3, 5, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('A', keep='last')
expected = df.iloc[[1, 4, 5, 6, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('A', keep=False)
expected = df.iloc[[5, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('C')
expected = df.iloc[[0, 1, 5, 6]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('C', keep='last')
expected = df.iloc[[3, 5, 6, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('C', keep=False)
expected = df.iloc[[5, 6]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop_duplicates.py:292 | Complexity: Advanced | Last updated: 2026-06-02*