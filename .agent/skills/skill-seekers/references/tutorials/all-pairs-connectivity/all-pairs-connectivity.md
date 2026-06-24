# How To: All Pairs Connectivity

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs connectivity

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

### Step 2: Assign nodes = value

```python
nodes = [0, 1, 2, 3]
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, nodes)
```

### Step 4: Assign A = value

```python
A = {n: {} for n in G}
```

### Step 5: Assign C = nx.all_pairs_node_connectivity(...)

```python
C = nx.all_pairs_node_connectivity(G)
```

**Verification:**
```python
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

### Step 6: Assign unknown, unknown = nx.node_connectivity(...)

```python
A[u][v] = A[v][u] = nx.node_connectivity(G, u, v)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
nodes = [0, 1, 2, 3]
nx.add_path(G, nodes)
A = {n: {} for n in G}
for u, v in itertools.combinations(nodes, 2):
    A[u][v] = A[v][u] = nx.node_connectivity(G, u, v)
C = nx.all_pairs_node_connectivity(G)
assert sorted(((k, sorted(v)) for k, v in A.items())) == sorted(((k, sorted(v)) for k, v in C.items()))
```

## Next Steps


---

*Source: test_connectivity.py:377 | Complexity: Intermediate | Last updated: 2026-06-02*