# How To: Make Max Clique Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Tests that the maximal clique graph is the same as the bipartite
clique graph after being projected onto the nodes representing the
cliques.

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Tests that the maximal clique graph is the same as the bipartite\n        clique graph after being projected onto the nodes representing the\n        cliques.\n\n        '

```python
'Tests that the maximal clique graph is the same as the bipartite\n        clique graph after being projected onto the nodes representing the\n        cliques.\n\n        '
```

**Verification:**
```python
assert H1.adj == H2.adj
```

### Step 2: Assign G = value

```python
G = self.G
```

### Step 3: Assign B = nx.make_clique_bipartite(...)

```python
B = nx.make_clique_bipartite(G)
```

### Step 4: Assign H1 = nx.projected_graph(...)

```python
H1 = nx.projected_graph(B, range(-5, 0))
```

### Step 5: Assign H1 = nx.relabel_nodes(...)

```python
H1 = nx.relabel_nodes(H1, {-v: v - 1 for v in range(1, 6)})
```

### Step 6: Assign H2 = nx.make_max_clique_graph(...)

```python
H2 = nx.make_max_clique_graph(G)
```

**Verification:**
```python
assert H1.adj == H2.adj
```


## Complete Example

```python
# Workflow
'Tests that the maximal clique graph is the same as the bipartite\n        clique graph after being projected onto the nodes representing the\n        cliques.\n\n        '
G = self.G
B = nx.make_clique_bipartite(G)
H1 = nx.projected_graph(B, range(-5, 0))
H1 = nx.relabel_nodes(H1, {-v: v - 1 for v in range(1, 6)})
H2 = nx.make_max_clique_graph(G)
assert H1.adj == H2.adj
```

## Next Steps


---

*Source: test_clique.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*