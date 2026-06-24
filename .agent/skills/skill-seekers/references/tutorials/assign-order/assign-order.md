# How To: Assign Order

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assign order

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
```

### Step 2: Assign result = df.assign(...)

```python
result = df.assign(D=df.A + df.B, C=df.A - df.B)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3, -1], [3, 4, 7, -1]], columns=list('ABDC'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.assign(...)

```python
result = df.assign(C=df.A - df.B, D=df.A + df.B)
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, -1, 3], [3, 4, -1, 7]], columns=list('ABCD'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
result = df.assign(D=df.A + df.B, C=df.A - df.B)
expected = DataFrame([[1, 2, 3, -1], [3, 4, 7, -1]], columns=list('ABDC'))
tm.assert_frame_equal(result, expected)
result = df.assign(C=df.A - df.B, D=df.A + df.B)
expected = DataFrame([[1, 2, -1, 3], [3, 4, -1, 7]], columns=list('ABCD'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_assign.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*