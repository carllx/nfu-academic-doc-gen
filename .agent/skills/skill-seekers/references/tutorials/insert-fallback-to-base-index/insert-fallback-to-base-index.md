# How To: Insert Fallback To Base Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert fallback to base index

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = CustomIndex(...)

```python
idx = CustomIndex([1, 2, 3])
```

### Step 2: Assign result = idx.insert(...)

```python
result = idx.insert(0, 'string')
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(['string', 1, 2, 3], dtype=object)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((2, 3)), columns=idx, index=Index([1, 2], name='string'))
```

### Step 6: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, expected)
```


## Complete Example

```python
# Workflow
idx = CustomIndex([1, 2, 3])
result = idx.insert(0, 'string')
expected = Index(['string', 1, 2, 3], dtype=object)
tm.assert_index_equal(result, expected)
df = DataFrame(np.random.default_rng(2).standard_normal((2, 3)), columns=idx, index=Index([1, 2], name='string'))
result = df.reset_index()
tm.assert_index_equal(result.columns, expected)
```

## Next Steps


---

*Source: test_subclass.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*