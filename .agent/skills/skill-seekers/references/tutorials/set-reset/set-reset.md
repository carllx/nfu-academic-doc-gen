# How To: Set Reset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set reset

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10], name='foo')
```

**Verification:**
```python
assert result['foo'].dtype == np.dtype('uint64')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [0, 1, 2]}, index=idx)
```

### Step 3: Assign result = df.reset_index(...)

```python
result = df.reset_index()
```

**Verification:**
```python
assert result['foo'].dtype == np.dtype('uint64')
```

### Step 4: Assign df = result.set_index(...)

```python
df = result.set_index('foo')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, idx)
```


## Complete Example

```python
# Workflow
idx = Index([2 ** 63, 2 ** 63 + 5, 2 ** 63 + 10], name='foo')
df = DataFrame({'A': [0, 1, 2]}, index=idx)
result = df.reset_index()
assert result['foo'].dtype == np.dtype('uint64')
df = result.set_index('foo')
tm.assert_index_equal(df.index, idx)
```

## Next Steps


---

*Source: test_reset_index.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*