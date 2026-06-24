# How To: Pairwise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pairwise

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign nodes = range(...)

```python
nodes = range(4)
```

**Verification:**
```python
assert list(pairwise(nodes)) == node_pairs
```

### Step 2: Assign node_pairs = value

```python
node_pairs = [(0, 1), (1, 2), (2, 3)]
```

**Verification:**
```python
assert list(pairwise(iter(nodes))) == node_pairs
```

### Step 3: Assign node_pairs_cycle = value

```python
node_pairs_cycle = node_pairs + [(3, 0)]
```

**Verification:**
```python
assert list(pairwise(nodes, cyclic=True)) == node_pairs_cycle
```

### Step 4: Assign empty_iter = iter(...)

```python
empty_iter = iter(())
```

**Verification:**
```python
assert list(pairwise(empty_iter)) == []
```

### Step 5: Assign empty_iter = iter(...)

```python
empty_iter = iter(())
```

**Verification:**
```python
assert list(pairwise(empty_iter, cyclic=True)) == []
```


## Complete Example

```python
# Workflow
nodes = range(4)
node_pairs = [(0, 1), (1, 2), (2, 3)]
node_pairs_cycle = node_pairs + [(3, 0)]
assert list(pairwise(nodes)) == node_pairs
assert list(pairwise(iter(nodes))) == node_pairs
assert list(pairwise(nodes, cyclic=True)) == node_pairs_cycle
empty_iter = iter(())
assert list(pairwise(empty_iter)) == []
empty_iter = iter(())
assert list(pairwise(empty_iter, cyclic=True)) == []
```

## Next Steps


---

*Source: test_misc.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*