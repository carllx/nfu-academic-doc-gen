# How To: Rename Bug

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename bug

## Prerequisites

**Required Modules:**
- `collections`
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({0: ['foo', 'bar'], 1: ['bah', 'bas'], 2: [1, 2]})
```

### Step 2: Assign df = df.rename(...)

```python
df = df.rename(columns={0: 'a'})
```

### Step 3: Assign df = df.rename(...)

```python
df = df.rename(columns={1: 'b'})
```

### Step 4: Assign df = df.set_index(...)

```python
df = df.set_index(['a', 'b'])
```

### Step 5: Assign df.columns = value

```python
df.columns = ['2001-01-01']
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1], [2]], index=MultiIndex.from_tuples([('foo', 'bah'), ('bar', 'bas')], names=['a', 'b']), columns=['2001-01-01'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({0: ['foo', 'bar'], 1: ['bah', 'bas'], 2: [1, 2]})
df = df.rename(columns={0: 'a'})
df = df.rename(columns={1: 'b'})
df = df.set_index(['a', 'b'])
df.columns = ['2001-01-01']
expected = DataFrame([[1], [2]], index=MultiIndex.from_tuples([('foo', 'bah'), ('bar', 'bas')], names=['a', 'b']), columns=['2001-01-01'])
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_rename.py:195 | Complexity: Intermediate | Last updated: 2026-06-02*