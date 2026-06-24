# How To: Set Column With Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set column with index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), idx.values)
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([1, 2, 3])
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'd'), arr)
```

### Step 3: Assign unknown = idx

```python
df['c'] = idx
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'c'), idx.values)
```

### Step 4: Assign idx = RangeIndex(...)

```python
idx = RangeIndex(1, 4)
```

### Step 5: Assign arr = value

```python
arr = idx.values
```

### Step 6: Assign unknown = idx

```python
df['d'] = idx
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'd'), arr)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
idx = Index([1, 2, 3])
df['c'] = idx
assert not np.shares_memory(get_array(df, 'c'), idx.values)
idx = RangeIndex(1, 4)
arr = idx.values
df['d'] = idx
assert not np.shares_memory(get_array(df, 'd'), arr)
```

## Next Steps


---

*Source: test_setitem.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*