# How To: Concat Astype Dup Col

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat astype dup col

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
df = DataFrame([{'a': 'b'}])
```

### Step 2: Assign df = concat(...)

```python
df = concat([df, df], axis=1)
```

### Step 3: Assign result = df.astype(...)

```python
result = df.astype('category')
```

### Step 4: Assign expected = DataFrame.astype(...)

```python
expected = DataFrame(np.array(['b', 'b']).reshape(1, 2), columns=['a', 'a']).astype('category')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([{'a': 'b'}])
df = concat([df, df], axis=1)
result = df.astype('category')
expected = DataFrame(np.array(['b', 'b']).reshape(1, 2), columns=['a', 'a']).astype('category')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_dataframe.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*