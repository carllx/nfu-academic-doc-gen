# How To: Quotient Graph Complete Bipartite

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the quotient graph of the complete bipartite graph under
the "same neighbors" node relation is `K_2`.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Tests that the quotient graph of the complete bipartite graph under\n    the "same neighbors" node relation is `K_2`.\n\n    '

```python
'Tests that the quotient graph of the complete bipartite graph under\n    the "same neighbors" node relation is `K_2`.\n\n    '
```

**Verification:**
```python
assert nx.is_isomorphic(expected, actual)
```

### Step 2: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(2, 3)
```

### Step 3: Assign expected = nx.complete_graph(...)

```python
expected = nx.complete_graph(2)
```

### Step 4: Assign actual = nx.quotient_graph(...)

```python
actual = nx.quotient_graph(G, same_neighbors)
```

**Verification:**
```python
assert nx.is_isomorphic(expected, actual)
```


## Complete Example

```python
# Workflow
'Tests that the quotient graph of the complete bipartite graph under\n    the "same neighbors" node relation is `K_2`.\n\n    '
G = nx.complete_bipartite_graph(2, 3)

def same_neighbors(u, v):
    return u not in G[v] and v not in G[u] and (G[u] == G[v])
expected = nx.complete_graph(2)
actual = nx.quotient_graph(G, same_neighbors)
assert nx.is_isomorphic(expected, actual)
```

## Next Steps


---

*Source: test_contraction.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*