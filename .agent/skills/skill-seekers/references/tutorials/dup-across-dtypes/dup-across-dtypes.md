# How To: Dup Across Dtypes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dup across dtypes

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
df = DataFrame([[1, 1, 1.0, 5], [1, 1, 2.0, 5], [2, 1, 3.0, 5]], columns=['foo', 'bar', 'foo', 'hello'])
```

### Step 2: Assign unknown = 7.0

```python
df['foo2'] = 7.0
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1, 1.0, 5, 7.0], [1, 1, 2.0, 5, 7.0], [2, 1, 3.0, 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign result = value

```python
result = df['foo']
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 1.0], [1, 2.0], [2, 3.0]], columns=['foo', 'foo'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign unknown = 'string'

```python
df['foo'] = 'string'
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame([['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=['bar', 'hello', 'foo2'])
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 1, 1.0, 5], [1, 1, 2.0, 5], [2, 1, 3.0, 5]], columns=['foo', 'bar', 'foo', 'hello'])
df['foo2'] = 7.0
expected = DataFrame([[1, 1, 1.0, 5, 7.0], [1, 1, 2.0, 5, 7.0], [2, 1, 3.0, 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
tm.assert_frame_equal(df, expected)
result = df['foo']
expected = DataFrame([[1, 1.0], [1, 2.0], [2, 3.0]], columns=['foo', 'foo'])
tm.assert_frame_equal(result, expected)
df['foo'] = 'string'
expected = DataFrame([['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0], ['string', 1, 'string', 5, 7.0]], columns=['foo', 'bar', 'foo', 'hello', 'foo2'])
tm.assert_frame_equal(df, expected)
del df['foo']
expected = DataFrame([[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=['bar', 'hello', 'foo2'])
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:120 | Complexity: Advanced | Last updated: 2026-06-02*