# How To: Assign Dependent

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assign dependent

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2], 'B': [3, 4]})
```

### Step 2: Assign result = df.assign(...)

```python
result = df.assign(C=df.A, D=lambda x: x['A'] + x['C'])
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 3, 1, 2], [2, 4, 2, 4]], columns=list('ABCD'))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.assign(...)

```python
result = df.assign(C=lambda df: df.A, D=lambda df: df['A'] + df['C'])
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 3, 1, 2], [2, 4, 2, 4]], columns=list('ABCD'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'A': [1, 2], 'B': [3, 4]})
result = df.assign(C=df.A, D=lambda x: x['A'] + x['C'])
expected = DataFrame([[1, 3, 1, 2], [2, 4, 2, 4]], columns=list('ABCD'))
tm.assert_frame_equal(result, expected)
result = df.assign(C=lambda df: df.A, D=lambda df: df['A'] + df['C'])
expected = DataFrame([[1, 3, 1, 2], [2, 4, 2, 4]], columns=list('ABCD'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_assign.py:75 | Complexity: Intermediate | Last updated: 2026-06-02*