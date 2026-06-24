# How To: Drop Duplicates For Take All

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates for take all

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
df = DataFrame({'AAA': ['foo', 'bar', 'baz', 'bar', 'foo', 'bar', 'qux', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': [1, 1, 2, 2, 2, 2, 1, 2], 'D': range(8)})
```

### Step 2: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('AAA')
```

### Step 3: Assign expected = value

```python
expected = df.iloc[[0, 1, 2, 6]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('AAA', keep='last')
```

### Step 6: Assign expected = value

```python
expected = df.iloc[[2, 5, 6, 7]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates('AAA', keep=False)
```

### Step 9: Assign expected = value

```python
expected = df.iloc[[2, 6]]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(['AAA', 'B'])
```

### Step 12: Assign expected = value

```python
expected = df.iloc[[0, 1, 2, 3, 4, 6]]
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 14: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(['AAA', 'B'], keep='last')
```

### Step 15: Assign expected = value

```python
expected = df.iloc[[0, 1, 2, 5, 6, 7]]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(['AAA', 'B'], keep=False)
```

### Step 18: Assign expected = value

```python
expected = df.iloc[[0, 1, 2, 6]]
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'AAA': ['foo', 'bar', 'baz', 'bar', 'foo', 'bar', 'qux', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': [1, 1, 2, 2, 2, 2, 1, 2], 'D': range(8)})
result = df.drop_duplicates('AAA')
expected = df.iloc[[0, 1, 2, 6]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('AAA', keep='last')
expected = df.iloc[[2, 5, 6, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates('AAA', keep=False)
expected = df.iloc[[2, 6]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates(['AAA', 'B'])
expected = df.iloc[[0, 1, 2, 3, 4, 6]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates(['AAA', 'B'], keep='last')
expected = df.iloc[[0, 1, 2, 5, 6, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates(['AAA', 'B'], keep=False)
expected = df.iloc[[0, 1, 2, 6]]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop_duplicates.py:133 | Complexity: Advanced | Last updated: 2026-06-02*