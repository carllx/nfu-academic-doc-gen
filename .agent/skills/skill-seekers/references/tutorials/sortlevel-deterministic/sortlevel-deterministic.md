# How To: Sortlevel Deterministic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sortlevel deterministic

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.frozen`


## Step-by-Step Guide

### Step 1: Assign tuples = value

```python
tuples = [('bar', 'one'), ('foo', 'two'), ('qux', 'two'), ('foo', 'one'), ('baz', 'two'), ('qux', 'one')]
```

**Verification:**
```python
assert sorted_idx.equals(expected)
```

### Step 2: Assign index = MultiIndex.from_tuples(...)

```python
index = MultiIndex.from_tuples(tuples)
```

**Verification:**
```python
assert sorted_idx.equals(expected[::-1])
```

### Step 3: Assign unknown = index.sortlevel(...)

```python
sorted_idx, _ = index.sortlevel(0)
```

**Verification:**
```python
assert sorted_idx.equals(expected)
```

### Step 4: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples(sorted(tuples))
```

**Verification:**
```python
assert sorted_idx.equals(expected[::-1])
```

### Step 5: Assign unknown = index.sortlevel(...)

```python
sorted_idx, _ = index.sortlevel(0, ascending=False)
```

**Verification:**
```python
assert sorted_idx.equals(expected[::-1])
```

### Step 6: Assign unknown = index.sortlevel(...)

```python
sorted_idx, _ = index.sortlevel(1)
```

### Step 7: Assign by1 = sorted(...)

```python
by1 = sorted(tuples, key=lambda x: (x[1], x[0]))
```

### Step 8: Assign expected = MultiIndex.from_tuples(...)

```python
expected = MultiIndex.from_tuples(by1)
```

**Verification:**
```python
assert sorted_idx.equals(expected)
```

### Step 9: Assign unknown = index.sortlevel(...)

```python
sorted_idx, _ = index.sortlevel(1, ascending=False)
```

**Verification:**
```python
assert sorted_idx.equals(expected[::-1])
```


## Complete Example

```python
# Workflow
tuples = [('bar', 'one'), ('foo', 'two'), ('qux', 'two'), ('foo', 'one'), ('baz', 'two'), ('qux', 'one')]
index = MultiIndex.from_tuples(tuples)
sorted_idx, _ = index.sortlevel(0)
expected = MultiIndex.from_tuples(sorted(tuples))
assert sorted_idx.equals(expected)
sorted_idx, _ = index.sortlevel(0, ascending=False)
assert sorted_idx.equals(expected[::-1])
sorted_idx, _ = index.sortlevel(1)
by1 = sorted(tuples, key=lambda x: (x[1], x[0]))
expected = MultiIndex.from_tuples(by1)
assert sorted_idx.equals(expected)
sorted_idx, _ = index.sortlevel(1, ascending=False)
assert sorted_idx.equals(expected[::-1])
```

## Next Steps


---

*Source: test_sorting.py:50 | Complexity: Advanced | Last updated: 2026-06-02*