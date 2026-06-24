# How To: All Pairs Connectivity Nbunch Combinations

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs connectivity nbunch combinations

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

### Step 2: Assign nbunch = value

```python
nbunch = [0, 2, 3]
```

### Step 3: Assign A = value

```python
A = {n: {} for n in nbunch}
```

### Step 4: Assign C = nx.all_pairs_node_connectivity(...)

```python
C = nx.all_pairs_node_connectivity(G, nbunch=nbunch)
```

**Verification:**
```python
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

### Step 5: Assign unknown, unknown = nx.node_connectivity(...)

```python
A[u][v] = A[v][u] = nx.node_connectivity(G, u, v)
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(5)
nbunch = [0, 2, 3]
A = {n: {} for n in nbunch}
for u, v in itertools.combinations(nbunch, 2):
    A[u][v] = A[v][u] = nx.node_connectivity(G, u, v)
C = nx.all_pairs_node_connectivity(G, nbunch=nbunch)
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

## Next Steps


---

*Source: test_connectivity.py:401 | Complexity: Intermediate | Last updated: 2026-06-02*