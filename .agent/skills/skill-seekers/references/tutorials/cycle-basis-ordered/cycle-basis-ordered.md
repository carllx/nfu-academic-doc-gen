# How To: Cycle Basis Ordered

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cycle basis ordered

## Prerequisites

**Required Modules:**
- `random`
- `itertools`
- `math`
- `pytest`
- `networkx`
- `networkx.algorithms.traversal.edgedfs`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(5)
```

**Verification:**
```python
assert cbG == cbH
```

### Step 2: Call G.update()

```python
G.update(nx.cycle_graph(range(3, 8)))
```

### Step 3: Assign cbG = nx.cycle_basis(...)

```python
cbG = nx.cycle_basis(G)
```

### Step 4: Assign perm = value

```python
perm = {1: 0, 0: 1}
```

### Step 5: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, perm)
```

### Step 6: Assign cbH = value

```python
cbH = [[perm.get(n, n) for n in cyc] for cyc in nx.cycle_basis(H)]
```

**Verification:**
```python
assert cbG == cbH
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(5)
G.update(nx.cycle_graph(range(3, 8)))
cbG = nx.cycle_basis(G)
perm = {1: 0, 0: 1}
H = nx.relabel_nodes(G, perm)
cbH = [[perm.get(n, n) for n in cyc] for cyc in nx.cycle_basis(H)]
assert cbG == cbH
```

## Next Steps


---

*Source: test_cycles.py:70 | Complexity: Intermediate | Last updated: 2026-06-02*