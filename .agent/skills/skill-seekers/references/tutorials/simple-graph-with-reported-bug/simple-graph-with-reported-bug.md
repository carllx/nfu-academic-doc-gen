# How To: Simple Graph With Reported Bug

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple graph with reported bug

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert len(cc) == 26
```

### Step 2: Assign edges = value

```python
edges = [(0, 2), (0, 3), (1, 0), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 0), (4, 1), (4, 5), (5, 0), (5, 1), (5, 2), (5, 3)]
```

**Verification:**
```python
assert len(cc) == len(rcc)
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(edges)
```

**Verification:**
```python
assert any((self.is_cyclic_permutation(c, rc) for rc in rcc))
```

### Step 4: Assign cc = sorted(...)

```python
cc = sorted(nx.simple_cycles(G))
```

**Verification:**
```python
assert any((self.is_cyclic_permutation(rc, c) for c in cc))
```

### Step 5: Assign rcc = sorted(...)

```python
rcc = sorted(nx.recursive_simple_cycles(G))
```

**Verification:**
```python
assert len(cc) == len(rcc)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
edges = [(0, 2), (0, 3), (1, 0), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 0), (4, 1), (4, 5), (5, 0), (5, 1), (5, 2), (5, 3)]
G.add_edges_from(edges)
cc = sorted(nx.simple_cycles(G))
assert len(cc) == 26
rcc = sorted(nx.recursive_simple_cycles(G))
assert len(cc) == len(rcc)
for c in cc:
    assert any((self.is_cyclic_permutation(c, rc) for rc in rcc))
for rc in rcc:
    assert any((self.is_cyclic_permutation(rc, c) for c in cc))
```

## Next Steps


---

*Source: test_cycles.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*