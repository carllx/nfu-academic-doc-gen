# How To: Mask Callable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mask callable

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

### Step 2: Assign result = df.mask(...)

```python
result = df.mask(lambda x: x > 4, lambda x: x + 1)
```

### Step 3: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 2, 3], [4, 6, 7], [8, 9, 10]])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.mask(df > 4, df + 1))
```

### Step 6: Assign result = df.mask(...)

```python
result = df.mask(lambda x: (x % 2 == 0).values, lambda x: 99)
```

### Step 7: Assign exp = DataFrame(...)

```python
exp = DataFrame([[1, 99, 3], [99, 5, 99], [7, 99, 9]])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df.mask(df % 2 == 0, 99))
```

### Step 10: Assign result = unknown.mask(...)

```python
result = (df + 2).mask(lambda x: x > 8, lambda x: x + 10)
```

### Step 11: Assign exp = DataFrame(...)

```python
exp = DataFrame([[3, 4, 5], [6, 7, 8], [19, 20, 21]])
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, (df + 2).mask(df + 2 > 8, df + 2 + 10))
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = df.mask(lambda x: x > 4, lambda x: x + 1)
exp = DataFrame([[1, 2, 3], [4, 6, 7], [8, 9, 10]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, df.mask(df > 4, df + 1))
result = df.mask(lambda x: (x % 2 == 0).values, lambda x: 99)
exp = DataFrame([[1, 99, 3], [99, 5, 99], [7, 99, 9]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, df.mask(df % 2 == 0, 99))
result = (df + 2).mask(lambda x: x > 8, lambda x: x + 10)
exp = DataFrame([[3, 4, 5], [6, 7, 8], [19, 20, 21]])
tm.assert_frame_equal(result, exp)
tm.assert_frame_equal(result, (df + 2).mask(df + 2 > 8, df + 2 + 10))
```

## Next Steps


---

*Source: test_mask.py:66 | Complexity: Advanced | Last updated: 2026-06-02*