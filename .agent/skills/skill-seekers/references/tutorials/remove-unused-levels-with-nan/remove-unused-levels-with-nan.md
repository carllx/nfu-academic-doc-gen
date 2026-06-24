# How To: Remove Unused Levels With Nan

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test remove unused levels with nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign idx = Index.rename(...)

```python
idx = Index([(1, np.nan), (3, 4)]).rename(['id1', 'id2'])
```

**Verification:**
```python
assert str(result) == str(expected)
```

### Step 2: Assign idx = idx.set_levels(...)

```python
idx = idx.set_levels(['a', np.nan], level='id1')
```

### Step 3: Assign idx = idx.remove_unused_levels(...)

```python
idx = idx.remove_unused_levels()
```

### Step 4: Assign result = value

```python
result = idx.levels
```

### Step 5: Assign expected = FrozenList(...)

```python
expected = FrozenList([['a', np.nan], [4]])
```

**Verification:**
```python
assert str(result) == str(expected)
```


## Complete Example

```python
# Workflow
idx = Index([(1, np.nan), (3, 4)]).rename(['id1', 'id2'])
idx = idx.set_levels(['a', np.nan], level='id1')
idx = idx.remove_unused_levels()
result = idx.levels
expected = FrozenList([['a', np.nan], [4]])
assert str(result) == str(expected)
```

## Next Steps


---

*Source: test_sorting.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*