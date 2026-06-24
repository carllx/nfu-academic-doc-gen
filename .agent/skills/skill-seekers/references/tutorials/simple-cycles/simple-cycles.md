# How To: Simple Cycles

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple cycles

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
```

**Verification:**
```python
assert len(cc) == len(ca)
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert any((self.is_cyclic_permutation(c, rc) for rc in ca))
```

### Step 3: Assign cc = sorted(...)

```python
cc = sorted(nx.simple_cycles(G))
```

### Step 4: Assign ca = value

```python
ca = [[0], [0, 1, 2], [0, 2], [1, 2], [2]]
```

**Verification:**
```python
assert len(cc) == len(ca)
```


## Complete Example

```python
# Workflow
edges = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)]
G = nx.DiGraph(edges)
cc = sorted(nx.simple_cycles(G))
ca = [[0], [0, 1, 2], [0, 2], [1, 2], [2]]
assert len(cc) == len(ca)
for c in cc:
    assert any((self.is_cyclic_permutation(c, rc) for rc in ca))
```

## Next Steps


---

*Source: test_cycles.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*