# How To: Align Series Condition

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align series condition

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 2: Assign result = value

```python
result = df[df['a'] == 2]
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[2, 5]], index=[1], columns=['a', 'b'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.where(...)

```python
result = df.where(df['a'] == 2, 0)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [0, 2, 0], 'b': [0, 5, 0]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
result = df[df['a'] == 2]
expected = DataFrame([[2, 5]], index=[1], columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
result = df.where(df['a'] == 2, 0)
expected = DataFrame({'a': [0, 2, 0], 'b': [0, 5, 0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_align.py:147 | Complexity: Intermediate | Last updated: 2026-06-02*