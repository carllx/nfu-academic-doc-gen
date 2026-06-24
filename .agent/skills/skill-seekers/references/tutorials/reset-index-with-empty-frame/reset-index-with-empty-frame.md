# How To: Reset Index With Empty Frame

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reset index with empty frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: columns
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([], name='foo')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=columns)
```

### Step 3: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['foo'])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign index = Index(...)

```python
index = Index([1, 2, 3], name='foo')
```

### Step 7: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=columns)
```

### Step 8: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'foo': [1, 2, 3]})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([], names=['foo', 'bar'])
```

### Step 12: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=columns)
```

### Step 13: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 14: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['foo', 'bar'])
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples([(1, 2), (2, 3)], names=['foo', 'bar'])
```

### Step 17: Assign df = DataFrame(...)

```python
df = DataFrame(index=index, columns=columns)
```

### Step 18: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 19: Assign expected = DataFrame(...)

```python
expected = DataFrame({'foo': [1, 2], 'bar': [2, 3]})
```

### Step 20: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: columns

# Workflow
index = Index([], name='foo')
df = DataFrame(index=index, columns=columns)
result = df.reset_index()
expected = DataFrame(columns=['foo'])
tm.assert_frame_equal(result, expected)
index = Index([1, 2, 3], name='foo')
df = DataFrame(index=index, columns=columns)
result = df.reset_index()
expected = DataFrame({'foo': [1, 2, 3]})
tm.assert_frame_equal(result, expected)
index = MultiIndex.from_tuples([], names=['foo', 'bar'])
df = DataFrame(index=index, columns=columns)
result = df.reset_index()
expected = DataFrame(columns=['foo', 'bar'])
tm.assert_frame_equal(result, expected)
index = MultiIndex.from_tuples([(1, 2), (2, 3)], names=['foo', 'bar'])
df = DataFrame(index=index, columns=columns)
result = df.reset_index()
expected = DataFrame({'foo': [1, 2], 'bar': [2, 3]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:786 | Complexity: Advanced | Last updated: 2026-06-02*