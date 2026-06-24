# How To: Decomposition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test decomposition

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (1, 3), (1, 4), (2, 5), (5, 10), (6, 8)]
```

**Verification:**
```python
assert len(chains) == len(expected)
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(edges)
```

### Step 3: Assign expected = value

```python
expected = [[(1, 3), (3, 2), (2, 1)], [(1, 4), (4, 3)], [(2, 5), (5, 3)], [(5, 10), (10, 9), (9, 5)], [(6, 8), (8, 7), (7, 6)]]
```

### Step 4: Assign chains = list(...)

```python
chains = list(nx.chain_decomposition(G, root=1))
```

**Verification:**
```python
assert len(chains) == len(expected)
```


## Complete Example

```python
# Workflow
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (1, 3), (1, 4), (2, 5), (5, 10), (6, 8)]
G = nx.Graph(edges)
expected = [[(1, 3), (3, 2), (2, 1)], [(1, 4), (4, 3)], [(2, 5), (5, 3)], [(5, 10), (10, 9), (9, 5)], [(6, 8), (8, 7), (7, 6)]]
chains = list(nx.chain_decomposition(G, root=1))
assert len(chains) == len(expected)
```

## Next Steps


---

*Source: test_chains.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*