# How To: Compare Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare frame

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = ['a', 'b', 2, 'a']
```

### Step 2: Assign cat = Categorical(...)

```python
cat = Categorical(data)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(cat)
```

### Step 4: Assign result = value

```python
result = cat == df.T
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([[True, True, True, True]])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = cat[::-1] != df.T
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame([[False, True, True, False]])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = ['a', 'b', 2, 'a']
cat = Categorical(data)
df = DataFrame(cat)
result = cat == df.T
expected = DataFrame([[True, True, True, True]])
tm.assert_frame_equal(result, expected)
result = cat[::-1] != df.T
expected = DataFrame([[False, True, True, False]])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_operators.py:144 | Complexity: Advanced | Last updated: 2026-06-02*