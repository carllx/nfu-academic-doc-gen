# How To: Reconstruct Sort

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reconstruct sort

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([['A', 'A', 'B', 'B', 'B'], [1, 2, 1, 2, 3]])
```

**Verification:**
```python
assert mi.is_monotonic_increasing
```

### Step 2: Assign recons = mi._sort_levels_monotonic(...)

```python
recons = mi._sort_levels_monotonic()
```

**Verification:**
```python
assert recons.is_monotonic_increasing
```

### Step 3: Assign mi = MultiIndex.from_tuples(...)

```python
mi = MultiIndex.from_tuples([('z', 'a'), ('x', 'a'), ('y', 'b'), ('x', 'b'), ('y', 'a'), ('z', 'b')], names=['one', 'two'])
```

**Verification:**
```python
assert mi is recons
```

### Step 4: Assign recons = mi._sort_levels_monotonic(...)

```python
recons = mi._sort_levels_monotonic()
```

**Verification:**
```python
assert mi.equals(recons)
```

### Step 5: Assign mi = MultiIndex(...)

```python
mi = MultiIndex(levels=[['b', 'd', 'a'], [1, 2, 3]], codes=[[0, 1, 0, 2], [2, 0, 0, 1]], names=['col1', 'col2'])
```

**Verification:**
```python
assert Index(mi.values).equals(Index(recons.values))
```

### Step 6: Assign recons = mi._sort_levels_monotonic(...)

```python
recons = mi._sort_levels_monotonic()
```

**Verification:**
```python
assert not mi.is_monotonic_increasing
```


## Complete Example

```python
# Workflow
mi = MultiIndex.from_arrays([['A', 'A', 'B', 'B', 'B'], [1, 2, 1, 2, 3]])
assert mi.is_monotonic_increasing
recons = mi._sort_levels_monotonic()
assert recons.is_monotonic_increasing
assert mi is recons
assert mi.equals(recons)
assert Index(mi.values).equals(Index(recons.values))
mi = MultiIndex.from_tuples([('z', 'a'), ('x', 'a'), ('y', 'b'), ('x', 'b'), ('y', 'a'), ('z', 'b')], names=['one', 'two'])
assert not mi.is_monotonic_increasing
recons = mi._sort_levels_monotonic()
assert not recons.is_monotonic_increasing
assert mi.equals(recons)
assert Index(mi.values).equals(Index(recons.values))
mi = MultiIndex(levels=[['b', 'd', 'a'], [1, 2, 3]], codes=[[0, 1, 0, 2], [2, 0, 0, 1]], names=['col1', 'col2'])
assert not mi.is_monotonic_increasing
recons = mi._sort_levels_monotonic()
assert not recons.is_monotonic_increasing
assert mi.equals(recons)
assert Index(mi.values).equals(Index(recons.values))
```

## Next Steps


---

*Source: test_sorting.py:168 | Complexity: Intermediate | Last updated: 2026-06-02*